//import {Model, Collection} from 'vue-mc'
//import {email, equal, empty, integer, min, required, string} from 'vue-mc/validation'
//import {getAPIURL, convertDatabaseDate} from './Helpers'
import { Model } from '@vuex-orm/core'

export class User extends Model {
  static entity = 'users'

  static fields() {
    return {
      id: this.increment(),
      username: this.attr(''),
      password: this.attr(''),
      name: this.attr(''),
      preferredName: this.attr(''),
      email: this.attr(''),
      studentNumber: this.attr(''),
      created: this.attr(null),
      modified: this.attr(null),
    }
  }

  // sort of a sanitize/preprocess step that attributes goes through
  // before being set in the model, really only using this for type
  // coercion right now
  /*
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
      fetch: getAPIURL('/users/{id}'),
      save: getAPIURL('/users'), // creating new
      update: getAPIURL('/users/{id}'), // editing existing
      delete: getAPIURL('/users/{id}')
    }
  }
  */
}

/*
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
*/
