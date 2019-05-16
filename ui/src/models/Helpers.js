export function getAPIURL(path) {
  let apiPrefix = process.env.VUE_APP_API
  return apiPrefix + path
}
