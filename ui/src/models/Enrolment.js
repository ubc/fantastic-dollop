import {Model, Collection} from 'vue-mc'
import {getAPIURL, convertDatabaseDate} from './Helpers'

export class Enrolment extends Model {
  defaults() {
    return {
      id: null,
      username: '',
      password: '',
      name: '',
      preferredName: '',
      email: '',
      studentNumber: '',
      role_id: null,
      course_id: null,
      user_id: null,
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
      user_id:   (id) => Number(id) || null,
      created: (created) => convertDatabaseDate(created),
      modified: (modified) => convertDatabaseDate(modified)
    }
  }

  validation() {
    return {}
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/users/{user_id}'),
      save: getAPIURL('/courses/{course_id}/users'), // creating new
      update: getAPIURL('/courses/{course_id}/users/{user_id}'),
      delete: getAPIURL('/courses/{course_id}/users/{user_id}')
    }
  }
}

export class EnrolmentList extends Collection {
  defaults() {
    return {
      course_id: null
    }
  }

  model() {
    return Enrolment
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/users'),
    }
  }
}
