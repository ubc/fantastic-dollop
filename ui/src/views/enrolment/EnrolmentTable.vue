<template>
	<div>
		<h4 class='text-xl font-medium mb-2'>Enrolment</h4>

		<button class='btnRegular mb-2'>
			<LabelledIcon label='Add'>
				<AddIcon title='Enrol a user into course' />
			</LabelledIcon>
		</button>

		<div v-if='!enrolments.models.length && !enrolments.loading'>No one enroled in course!</div>
		<Loading v-if='enrolments.loading || roles.loading' />

		<div v-for='enrolment in enrolments.models' :key='enrolment.id'
			class='flex border-t border-gray-400 py-2'>
			<div class='flex-auto flex flex-col break-all md:break-normal'>
				<div class='flex-auto'>
					{{ enrolment.$.username }}
					<a v-show='enrolment.$.email' :href='"mailto:" + enrolment.$.email'
						class='ml-4'>
					{{ enrolment.$.email }}
					</a>
				</div>
				<div v-show='enrolment.$.preferredName || enrolment.$.name'
					class='flex-auto text-gray-600'>
					<span v-show='enrolment.$.name' class='mr-2'>
						{{ enrolment.$.name }}
					</span>
					<span v-show='enrolment.$.preferredName'>
						&lpar;{{ enrolment.$.preferredName }}&rpar;
					</span>
				</div>
			</div>
			<div class='flex-initial md:mr-2'>
				<select v-model='enrolment.role_id'>
					<option v-for='role in roles.models' :key='role.name' :value='role.id'>
					{{ role.$.name }}
					</option>
				</select>
			</div>
			<div class='flex-initial'>
				<button class='btnRegular'>
					<LabelledIcon label='Remove'>
						<RemoveIcon title='Remove user from this course' />
					</LabelledIcon>
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import AddIcon from 'icons/AccountPlus'
import RemoveIcon from 'icons/AccountRemove'

import LabelledIcon from '@/components/util/LabelledIcon'
import Loading from '@/components/util/status/Loading'

import {EnrolmentList} from '@/models/Enrolment'
import {RoleList} from '@/models/Role'

export default {
	name: "EnrolmentTable",
	components: {
		AddIcon,
		RemoveIcon,
		LabelledIcon,
		Loading
	},
	data() { return {
		enrolments: new EnrolmentList(),
		roles: new RoleList(),
	}},
	methods: {
		getEnrolments() {
			this.enrolments.set('course_id', this.$route.params.courseId)
			this.enrolments.fetch().then().catch((error) => {
				this.$store.commit('error/add',
					{error: error, message: 'Failed to get enrolments.'})
			})
		},
		getRoles() {
			this.roles.fetch().then(() => {
			}).catch((error) => {
				this.$store.commit('error/add',
					{error: error, message: 'Failed to get user roles.'})
			})
		},
		setEventListeners() {
			this.enrolments.on('add', (event) => {
				// automatic save when user's role type gets changed
				event.model.on('change', (event) => {
					if (event.attribute == 'role_id') {
						event.target.save().then(() => {
							this.$notify({
								title: "User '" + event.target.username + "' changed to " +
												event.target.role,
								type: 'success'
							})
						}).catch((error) => {
							event.target.role_id = event.previous
							this.$store.commit('error/add', {error: error,
								message: 'Failed to change user role.'})
						})
					}
				})
			})
		},
		init() {
			this.getEnrolments()
			this.getRoles()
			this.setEventListeners()
		}
	},
	mounted() {
		this.init()
	}
}
</script>

<style scoped>
</style>
