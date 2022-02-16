module.exports = {
  // publicPath :'/vue/'
  outputDir: '../backend/dist',
  // productionSourceMap: true,
  configureWebpack: {
    devtool: 'source-map'
  },
  devServer: {
    proxy:{
      '/api':{
        target: 'http://' + process.env.PROXY,
        changeOrigin:true,
      }
    }

  },

}