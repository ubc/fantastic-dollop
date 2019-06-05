export default {
  path: '/courses/:courseId/exams',
  meta: { breadcrumb: 'Exams List' },
  component: () => import('../../views/DefaultRouterView.vue'),
  props(route) { return {courseId: Number(route.params.courseId)}},
  children: [
    {
      path: '',
      name: 'examsList',
      component: () => import('../../views/exams/ExamTable.vue'),
    },
    {
      path: '/courses/:courseId/exams/add',
      name: 'addExam',
      meta: { breadcrumb: 'Add Exam' },
      component: () => import('../../views/exams/ExamForm.vue'),
    },
    {
      path: '/courses/:courseId/exams/:examId',
      component: () => import('../../views/DefaultRouterView.vue'),
      props(route) { return {
        examId: Number(route.params.examId),
        courseId: Number(route.params.courseId)
      }},
      children: [
        {
          path: '',
          meta: { breadcrumb: 'Exam' },
          name: 'viewExam',
          component: () => import('../../views/exams/ExamGenerator.vue')
        },
        {
          path: '/courses/:courseId/exams/:examId/edit',
          name: 'editExam',
          meta: { breadcrumb: 'Edit Exam' },
          component: () => import('../../views/exams/ExamForm.vue')
        },
        {
          path: '/courses/:courseId/exams/:examId/sources/:sourceId/edit',
          meta: { breadcrumb: 'Configure Exam Source' },
          name: 'configureSource',
          component: () => import('../../views/exams/SourceEdit.vue'),
          props(route) { return {sourceId: Number(route.params.sourceId)}}
        },
        {
          path: '/courses/:courseId/exams/:examId/generators',
          name: 'listPapers',
          meta: { breadcrumb: 'Papers' },
          component: () => import('../../views/exams/GeneratedPapersTable.vue')
        },
        {
          path: '/courses/:courseId/exams/:examId/generators/add',
          name: 'addExamGenerator',
          meta: { breadcrumb: 'Generators' },
          component: () => import('../../views/exams/AddExamGenerator.vue')
        }
      ]
    }
  ]
}
