import VuexORM from '@vuex-orm/core'
import VuexORMAxios from '@vuex-orm/plugin-axios'
import { TOKEN_KEY } from '@/plugins/store/auth'
import { User } from '@/models/User'

// register all models
const database = new VuexORM.Database()
database.register(User)

// configure orm axios plugin
const ormAxiosConfig = {
  baseURL: process.env.VUE_APP_API,
  url: '/',
  access_token: () => localStorage.getItem(TOKEN_KEY),
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
}
VuexORM.use(VuexORMAxios, { database, http:  ormAxiosConfig })

export default VuexORM.install(database)
