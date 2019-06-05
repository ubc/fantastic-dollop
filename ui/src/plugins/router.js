import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/home/Home.vue'

import AdminRoutes from '@/plugins/router/admin'

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
      component: () => import('../views/home/SignedInHome.vue')
    },
    {
      path: '/signed-out',
      name: 'signedOut',
      meta: { isPublic: true },
      component: () => import('../views/SignedOut.vue')
    },
    {
      path: '/courses/:courseId',
      name: 'courseHome',
      meta: { breadcrumb: 'Course' },
      component: () => import('../views/courses/CourseHome.vue'),
      props(route) { return {courseId: Number(route.params.courseId)}},
      children: [
        {
          path: '/courses/:courseId/users',
          name: 'enrolment',
          meta: { breadcrumb: 'Enrolment' },
          component: () => import('../views/enrolment/EnrolmentTable.vue'),
          props(route) { return {courseId: Number(route.params.courseId)}}
        }
      ]
    },
    AdminRoutes
  ]
})
