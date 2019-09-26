// Kind of a permission system. I don't see a need for a proper ACL yet, so
// this is just a simple role based permission checking. The most complicated we
// get is that users can have different roles in different courses.
//
// Since this thing just tells you what role a user have, I'm calling it 'access'.
// This will let us put in a separate actual 'permission' module later if needed.
import axios from 'axios'

export const access = {
  namespaced: true,
  state: {
    user: {},
    courses: {}
  },
  getters: {
    isAdmin: (state) => {
      return state.user.isAdmin
    },
    isInstructor: (state, getters) => (courseId) => {
      // admins need to be able to do anything instructors can
      if (getters.isAdmin) return true
      if (courseId in state.courses) {
        if (state.courses[courseId].role == 'Instructor') return true
      }
      return false
    },
    isStudent: (state) => (courseId) => {
      if (courseId in state.courses) {
        console.log(state.courses[courseId].role)
        if (state.courses[courseId].role == 'Student') return true
      }
      return false
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setCourses(state, courses) {
      state.courses = courses
    }
  },
  actions: {
    init(context) {
      if (context.rootGetters['auth/isSignedIn']) {
        context.dispatch('getSignedInUser')
        context.dispatch('getEnroledCourses')
      }
    },
    reset(context) {
      context.commit('setUser', {})
      context.commit('setCourses', {})
    },
    getSignedInUser(context) {
      axios.get('/users/me').then( (response) => {
        context.commit('setUser', response.data)
      }).catch( (error) => {
        context.commit('error/add', {error: error,
          message: 'Failed to retrieve signed in user info.'}, {root: true})
      })
    },
    getEnroledCourses(context) {
      axios.get('/users/me/courses').then( (response) => {
        let courses = {}
        response.data.forEach((item)=> {
          courses[item.id] = item
        })
        context.commit('setCourses', courses)
      }).catch( (error) => {
        context.commit('error/add', {error: error,
          message: "Failed to retrieve signed in user's courses."}, {root: true})
      })
    }
  }
}
