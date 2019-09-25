// Postgres saves all time in UTC by default. Unfortunately, when python
// converts the datetime to string, it doesn't add the 'Z' or '+00' for UTC,
// so javascript's Date() parsing fails, so we have to add it manually.
export function convertDatabaseDate(dbDate) {
  let newDate = new Date(dbDate + 'Z')
  return newDate.toLocaleString()
}
