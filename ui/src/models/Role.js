import {Model, Collection} from 'vue-mc'
import {convertDatabaseDate} from './Helpers'

export class Role extends Model {
  defaults() {
    return {
      id: null,
      name: '',
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
}

export class RoleList extends Collection {
  model() {
    return Role
  }

  routes() {
    return {
      fetch: '/roles'
    }
  }
}
