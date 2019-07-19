import {Model, Collection} from 'vue-mc'
import {getAPIURL, convertDatabaseDate} from './Helpers'

export class ExamSource extends Model {
  defaults() {
    return {
      id: null,
      name: '',
      file: '',
      course_id: null,
      exam_id: null,
      created: '',
      modified: ''
    }
  }

  // sort of a sanitize/preprocess step that attributes goes through
  // before being set in the model, really only using this for type
  // coercion right now
  mutations() {
    return {
      id:   (id) => Number(id) || null,
      course_id:   (id) => Number(id) || null,
      created: (created) => convertDatabaseDate(created),
      modified: (modified) => convertDatabaseDate(modified)
    }
  }

  validation() {
    return {}
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/exams/{exam_id}/sources/{id}'),
      delete: getAPIURL('/courses/{course_id}/exams/{exam_id}/sources/{id}')
    }
  }
}

export class ExamSourceList extends Collection {
  defaults() {
    return {
      course_id: null,
      exam_id: null
    }
  }

  model() {
    return ExamSource
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/exams/{exam_id}/sources'),
    }
  }
}
