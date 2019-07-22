import {Model, Collection} from 'vue-mc'
import {getAPIURL, convertDatabaseDate} from './Helpers'

export class ExamComponent extends Model {
  defaults() {
    return {
      id: null,
      course_id: null,
      exam_id: null,
      exam_component_type_id: null,
      exam_component_type: '',
      sequence: null,
      page_start: 0,
      page_end: 0,
      mark: 0,
      comment: '',
      created: '',
      modified: ''
    }
  }

  mutations() {
    return {
      id:   (id) => Number(id) || null,
      created: (created) => convertDatabaseDate(created),
      modified: (modified) => convertDatabaseDate(modified)
    }
  }

  validation() {
    return {}
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{id}'),
      create: getAPIURL('/courses/{course_id}/exams/{exam_id}/components'),
      save: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{id}'),
      delete: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{id}')
    }
  }
}

export class ExamComponentList extends Collection {
  defaults() {
    return {
      course_id: null,
      exam_id: null
    }
  }

  model() {
    return ExamComponent
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/exams/{exam_id}/components'),
    }
  }
}
