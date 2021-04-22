<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
var Vue = require('vue');
var VueRouter = require('vue-router');
var Home = require('./Home.vue');

var routes = [
    {path: '/',
    name: 'home',
    component: Home,
    },
];
var router = new VueRouter({routes:routes});

module.exports = Vue.extend({
    router:router
})
</script>