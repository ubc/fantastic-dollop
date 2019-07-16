import {Model, Collection} from 'vue-mc'
import {getAPIURL, convertDatabaseDate} from './Helpers'

export class Exam extends Model {
  defaults() {
    return {
      id: null,
      name: '',
      print_id: '',
      course_id: null,
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
      fetch: getAPIURL('/courses/{course_id}/exams/{id}'),
      save: getAPIURL('/courses/{course_id}/exams'), // creating new
      update: getAPIURL('/courses/{course_id}/exams/{id}'),
      delete: getAPIURL('/courses/{course_id}/exams/{id}')
    }
  }
}

export class ExamList extends Collection {
  defaults() {
    return {
      course_id: null
    }
  }

  model() {
    return Exam
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/exams'),
    }
  }
}
