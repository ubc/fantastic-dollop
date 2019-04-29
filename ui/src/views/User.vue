<template>
  <div>
		<h1>Add New User</h1>
    <UserInfoForm v-bind:is-new-user='true' />

		<h1>Edit Existing User</h1>
    <UserInfoForm/>
  </div>
</template>

<script>
// @ is an alias to /src
import UserInfoForm from '@/components/users/UserInfoForm.vue'

console.log(process.env.VUE_APP_API)

export default {
  name: 'home',
  components: {
    UserInfoForm
  }
}
</script>
