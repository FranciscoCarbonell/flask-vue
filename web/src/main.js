var Vue = require('vue');
Vue.use(require('vue-router'));

var Main = require('./Main.vue');
var app = new Main().$mount('#app');