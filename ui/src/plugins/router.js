import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      meta: { layout: 'NoSidebar' },
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */'../views/About.vue')
    },
    {
      path: '/login',
      name: 'login',
      meta: { layout: 'NoSidebar' },
      component: () => import('../views/Login.vue')
    },
    {
      path: '/users',
      component: () => import('../views/users/Users.vue'),
      children: [
        {
          path: '',
          name: 'userHome',
          component: () => import('../views/users/UserTable.vue')
        },
        {
          path: '/users/add',
          name: 'addUser',
          component: () => import('../views/users/UserInfoForm.vue'),
          props: {isNewUser: true}
        },
        {
          path: '/users/:userId/edit',
          name: 'editUser',
          component: () => import('../views/users/UserInfoForm.vue'),
          // userId is expected to be a number, but by default, router passes all
          // params as a string, so we need to use a function here to cast it
          props(route) { return {userId: Number(route.params.userId)} }
        }
      ]
    }
  ]
})
