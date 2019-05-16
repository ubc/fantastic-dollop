import {Model, Collection} from 'vue-mc'
import {empty, equal, integer, min, required, string} from 'vue-mc/validation'
import {getAPIURL} from './Helpers'

export class User extends Model {
  defaults() {
    return {
      id: null,
      username: '',
      password: '',
      name: '',
      preferredName: '',
      email: '',
      studentNumber: ''
    }
  }

  // sort of a sanitize/preprocess step that attributes goes through
  // before being set in the model, really only using this for type
  // coercion right now
  mutations() {
    return {
      id:   (id) => Number(id) || null,
      username: String,
      password: String,
      name: String,
      preferredName: String,
      email: String,
      studentNumber: String
    }
  }

  validation() {
    return {
      id:   integer.and(min(1)).or(equal(null)),
      username: string.and(required),
    }
  }

  routes() {
    return {
      fetch: getAPIURL('/users/{id}'),
      save: getAPIURL('/users')
    }
  }
}

export class UserList extends Collection {
  model() {
    return User
  }

  routes() {
    return {
      fetch: getAPIURL('/users'),
    }
  }
}
