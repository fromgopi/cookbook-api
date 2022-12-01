const path = require('path');   
const HtmlWebPackPlugin = require('html-webpack-plugin');
const ENTRY_POINT = path.resolve(__dirname, 'src/index.js')
const DIST_FOLDER = path.resolve(__dirname, 'dist')
module.exports = {
	entry: ENTRY_POINT,
	output: {
		path: DIST_FOLDER 
	},
	devServer: {
		publicPath: '/',
		contentBase: './dist',
		hot: true,
		open: true,
		watchOptions: {
			
		}
	}
};










