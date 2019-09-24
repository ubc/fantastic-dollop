<!-- Form for entering course information -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Add Enrolment</h3>

		<Loading v-if='course.loading' />

		<form @submit.prevent='saveEnrolment' class='formVertical' v-show='!course.loading'>
			<!-- Required Fields -->
			<label for='user'>User</label>
			<select id='user' name='user' v-model='userId' required>
				<option v-for='user in users.models' :key='user.id' :value='user.id'>
					{{ user.$.username }}
				</option>
			</select>

			<label for='role'>Role</label>
			<select id='role' name='role' v-model='roleId' required>
				<option v-for='role in roles.models' :key='role.id' :value='role.id'>
					{{ role.$.name }}
				</option>
			</select>

			<button type='submit' class='btnPrimary my-3'>Save</button>
		</form>
	</div>
</template>

<script>
import Loading from '@/components/util/status/Loading'
import {Enrolment} from '@/models/Enrolment'
import {RoleList} from '@/models/Role'
import {UserList} from '@/models/User'


export default {
	name: 'EnrolmentForm',
	components: {
		Loading
	},
	props: {
		courseId: {
			type: Number,
			default: null
		}
	},
	data() { return {
		course: new Enrolment(),
		roles: new RoleList(),
		users: new UserList(),
		roleId: null,
		userId: null 
	}},
	mounted() {
		this.roles.fetch().then().catch((error) => {
			this.$store.commit('error/add',
				{error: error, message: 'Failed to get user roles.'})
		})
		this.users.fetch().then().catch((error) => {
			this.$store.commit('error/add',
				{error: error, message: 'Failed to get user users.'})
		})
	},
	methods: {
		saveEnrolment: function() {
			let enrolment = new Enrolment()
			enrolment.set('course_id', this.$route.params.courseId)
			enrolment.set('user_id', this.userId)
			enrolment.set('role_id', this.roleId)
			enrolment.save().then( () => {
				this.$notify({
					title: "User added to course",
					type: 'success'
				})
				this.$router.push({'name': 'adminCourseEnrolment'})
			}).catch( (error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to add user to course."})
			})
		}
	}
}
</script>

<style>
</style>
