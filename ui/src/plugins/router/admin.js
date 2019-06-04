export default {
  path: '/admin',
  name: 'admin',
  meta: { breadcrumb: 'Admin' },
  component: () => import('../../views/admin/Admin.vue'),
  children: [
    {
      path: '/admin/courses',
      component: () => import('../../views/DefaultRouterView.vue'),
      children: [
        {
          path: '',
          meta: { breadcrumb: 'Courses List' },
          name: 'adminCourse',
          component: () => import('../../views/courses/CourseTable.vue')
        },
        {
          path: '/admin/courses/add',
          name: 'adminCourseAdd',
          meta: { breadcrumb: 'Add Course' },
          component: () => import('../../views/courses/CourseForm.vue')
        },
        {
          path: '/admin/courses/:courseId/edit',
          name: 'adminCourseEdit',
          meta: { breadcrumb: 'Edit Course' },
          component: () => import('../../views/courses/CourseForm.vue'),
          props(route) { return {courseId: Number(route.params.courseId)}}
        }
      ]
    },
    {
      path: '/admin/users',
      component: () => import('../../views/DefaultRouterView.vue'),
      children: [
        {
          path: '',
          name: 'adminUserTable',
          meta: { breadcrumb: 'Users List' },
          component: () => import('../../views/users/UserTable.vue')
        },
        {
          path: '/admin/users/add',
          name: 'adminAddUser',
          meta: { breadcrumb: 'Add User' },
          component: () => import('../../views/users/UserForm.vue'),
          props: {isNewUser: true}
        },
        {
          path: '/admin/users/:userId',
          name: 'adminViewUser',
          meta: { breadcrumb: 'View User' },
          component: () => import('../../views/users/UserInfo.vue'),
          // userId is expected to be a number, but by default, router passes all
          // params as a string, so we need to use a function here to cast it
          props(route) { return {userId: Number(route.params.userId)} }
        },
        {
          path: '/admin/users/:userId/edit',
          name: 'adminEditUser',
          meta: { breadcrumb: 'Edit User' },
          component: () => import('../../views/users/UserForm.vue'),
          // userId is expected to be a number, but by default, router passes all
          // params as a string, so we need to use a function here to cast it
          props(route) { return {userId: Number(route.params.userId)} }
        },
      ]
    }
  ]
}
