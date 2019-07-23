import {Model, Collection} from 'vue-mc'
import {getAPIURL, convertDatabaseDate} from './Helpers'

export class ExamComponentSource extends Model {
  defaults() {
    return {
      id: null,
      course_id: null,
      exam_id: null,
      exam_component_id: null,
      exam_source_id: null,
      exam_source_name: '',
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
      fetch: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{exam_component_id}/sources/{id}'),
      save: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{exam_component_id}/sources'),
      update: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{exam_component_id}/sources/{id}'),
      delete: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{exam_component_id}/sources/{id}')
    }
  }
}

export class ExamComponentSourceList extends Collection {
  defaults() {
    return {
      course_id: null,
      exam_id: null,
      exam_component_id: null
    }
  }

  model() {
    return ExamComponentSource
  }

  routes() {
    return {
      fetch: getAPIURL('/courses/{course_id}/exams/{exam_id}/components/{exam_component_id}/sources'),
    }
  }
}
