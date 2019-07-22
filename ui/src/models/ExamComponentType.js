import {Model, Collection} from 'vue-mc'
import {getAPIURL, convertDatabaseDate} from './Helpers'

export class ExamComponentType extends Model {
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

export class ExamComponentTypeList extends Collection {
  model() {
    return ExamComponentType
  }

  routes() {
    return {
      fetch: getAPIURL('/exam_component_types'),
    }
  }
}
