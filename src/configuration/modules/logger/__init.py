"""Logging"""
from functools import wraps
import sys
import json
from queue import Queue
from logging import getLogger
from logging.config import ConvertingDict, ConvertingList, valid_ident, dictConfig
from logging.handlers import QueueHandler, QueueListener
from atexit import register as register_on_exit
from flask import g
from werkzeug.serving import WSGIRequestHandler, _log
from .settings import get_configuration

def resolve_handlers(handlers):
    """Resolve log handlers provided in settings"""
    if not isinstance(handlers, ConvertingList):
        return handlers
    return [handlers[i] for i in range(len(handlers))]

def resolve_queue(queue):
    """Resolves classes provided in settings"""
    if not isinstance(queue, ConvertingDict):
        return queue
    if '__resolved_value__' in queue:
        return queue['__resolved_value__']

    cname = queue.pop('class')
    queue_class = queue.configurator.resolve(cname)
    params = {
        key: queue[key] for key in queue if valid_ident(key)}
    result = queue_class(**params)

    queue['__resolved_value__'] = result
    return result

class QueueListenerHandler(QueueHandler):
    """
    Runs on a separate thread and reads the messages in the shared
    queue and passes them to their relevant handlers
    """

    def __init__(self, handlers, respect_handler_level=False, queue=Queue(-1)):
        """
        Creates a queue listener, passes it all the log handlers and starts
        the listener. Finally, an exit handler is registered to stop the
        listener when the process ends.
        """
        try:
            queue = resolve_queue(queue)
            super().__init__(queue)
            handlers = resolve_handlers(handlers)
            self._listener = QueueListener(
                self.queue,
                *handlers,
                respect_handler_level=respect_handler_level)
            self._listener.start()
            register_on_exit(self._listener.stop)
        except (TypeError) as error:
            print(error)
        except (Exception) as error:  # pylint: disable=broad-except
            print(error)


class RequestHandlerLoggerOverride(WSGIRequestHandler):
    """Overrides the default request log format"""

    def log(self, type, message, *args):  # pylint: disable=redefined-builtin
        _log(type, '%s %s\n' % (self.address_string(), message % args))

def setup_logger(config):
    """Initialize the logger with the configured settings"""
    try:
        dictConfig(get_configuration(
            config['NAME'],
            config['LOG_CONSOLE_LEVEL'],
            config['LOG_DEBUG_FILE_LEVEL'],
            config['LOG_DEBUG_FILE_TO'],
            config['LOG_ERROR_FILE_LEVEL'],
            config['LOG_ERROR_FILE_TO']))
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        sys.exit(1)
