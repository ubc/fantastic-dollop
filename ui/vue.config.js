var path = require('path')

module.exports = {
  configureWebpack: {
    resolve: {
      alias : {
        "icons": path.resolve(__dirname, "node_modules/vue-material-design-icons")
      },
      extensions: [
        ".vue"
      ]
    }
  },
  chainWebpack: config => {
    config.module.rule('eslint').use('eslint-loader')
      .tap(opts => ({ ...opts, emitWarning: false }));
  }
}
