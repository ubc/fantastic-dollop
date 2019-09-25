import {Model, Collection} from 'vue-mc'
import {email, equal, empty, integer, min, required, string} from 'vue-mc/validation'
import {convertDatabaseDate} from './Helpers'

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
      created: (created) => convertDatabaseDate(created),
      modified: (modified) => convertDatabaseDate(modified)
    }
  }

  validation() {
    return {
      id:   integer.and(min(1)).or(equal(null)),
      username: string.and(required),
      email: email.or(empty)
    }
  }

  routes() {
    return {
      fetch: '/users/{id}',
      save: '/users', // creating new
      update: '/users/{id}', // editing existing
      delete: '/users/{id}'
    }
  }
}

export class UserList extends Collection {
  model() {
    return User
  }

  routes() {
    return {
      fetch: '/users'
    }
  }
}
