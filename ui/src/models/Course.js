import {Model, Collection} from 'vue-mc'
import {equal, integer, min, required, string} from 'vue-mc/validation'
import {getAPIURL} from './Helpers'

export class Course extends Model {
  defaults() {
    return {
      id: null,
      name: '',
      description: ''
    }
  }

  mutations() {
    return {
      id:   (id) => Number(id) || null,
      name: String
    }
  }

  validation() {
    return {
      id:   integer.and(min(1)).or(equal(null)),
      name: string.and(required),
    }
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{id}'),
      save: getAPIURL('/courses'),
      update: getAPIURL('/courses/{id}'),
      delete: getAPIURL('/courses/{id}')
    }
  }
}

export class CourseList extends Collection {
  model() {
    return Course
  }

  routes() {
    return {
      fetch: getAPIURL('/courses'),
    }
  }
}
