import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/home/Home.vue'

Vue.use(Router)

/* Each route entry can have optional metadata configuration, see root page for
 * example.
 * Available meta config options:
 * - isPublic: if set to true, this page can be viewed without signing in.
 *    Defaults to false.
 * - layout: use a different layout (from layouts/ directory) to render the page.
 *    Defaults to DefaultLayout. Currently, no alternative layout other than
 *    default exists. Keeping the system around for a bit to see if we need it.
 * */

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      meta: { isPublic: true },
      component: Home
    },
    {
      path: '/home',
      name: 'signedInHome',
      // route level code-splitting
      // this generates a separate chunk (signedInHome.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import('../views/home/SignedInHome.vue')//webpackChunkName: "signedInHome"
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/admin/Admin.vue'),
      children: [
        {
          path: '/admin/courses',
          name: 'adminCourseTable',
          component: () => import('../views/courses/CourseTable.vue')
        },
        {
          path: '/admin/users',
          name: 'adminUserTable',
          component: () => import('../views/users/UserTable.vue')
        },
        {
          path: '/admin/users/add',
          name: 'adminAddUser',
          component: () => import('../views/users/UserInfoForm.vue'),
          props: {isNewUser: true}
        },
        {
          path: '/admin/users/:userId',
          name: 'adminViewUser',
          component: () => import('../views/users/UserInfo.vue'),
          // userId is expected to be a number, but by default, router passes all
          // params as a string, so we need to use a function here to cast it
          props(route) { return {userId: Number(route.params.userId)} }
        },
        {
          path: '/admin/users/:userId/edit',
          name: 'adminEditUser',
          component: () => import('../views/users/UserInfoForm.vue'),
          // userId is expected to be a number, but by default, router passes all
          // params as a string, so we need to use a function here to cast it
          props(route) { return {userId: Number(route.params.userId)} }
        },
      ]
    },
    {
      path: '/signed-out',
      name: 'signedOut',
      meta: { isPublic: true },
      component: () => import('../views/SignedOut.vue')
    }
  ]
})
