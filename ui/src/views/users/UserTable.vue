<!-- Table that lists users in the database -->
<template>
	<div class='w-full'>
		<router-link :to="{name: 'adminAddUser'}" tag="button" class='btnRegular mb-4' v-show='!errMsg'>
			<LabelledIcon label='Add'><AddIcon title='Add a new user' /></LabelledIcon>
		</router-link>

		<Error :msg='errMsg' v-if='errMsg'>
			<button type='button' v-on:click='getUsers' class='btn btnPrimary'>Retry</button>
		</Error>

		<div v-for="user in users.models" :user="user" :key="user.id" class='userCard md:flex md:flex-row md:items-center'>
			<div class='flex'>
				<div class='w-1/2 md:hidden'>Username</div>
				<div class='w-1/2 md:w-auto'>{{ user.$.username }}</div>
			</div>
			<div class='flex'>
				<div class='w-1/2 md:hidden'>Preferred Name</div>
				<div class='w-1/2 md:w-auto'>{{ user.$.preferredName }}</div>
			</div>
			<!--
			<div class='flex'>
				<div class='w-1/2'>Name</div>
				<div class='w-1/2'>{{ user.$.name }}</div>
			</div>
			<div class='flex'>
				<div class='w-1/2'>Email</div>
				<div class='w-1/2'>{{ user.$.email }}</div>
			</div>
			<div class='flex'>
				<div class='w-1/2'>Student Number</div>
				<div class='w-1/2'>{{ user.$.studentNumber }}</div>
			</div>
			-->
			<div class='flex'>
				<div class='flex-1'>
					<router-link :to="{name: 'adminEditUser', params:{userId: user.$.id}}"
			tag="button" class='btnRegular'>
						<LabelledIcon label='Edit'>
						<EditIcon title='Edit user' />
						</LabelledIcon>
					</router-link>
				</div>
				<div class='flex-initial'>
					<button class='btnRegular'>
						<LabelledIcon label='Delete'>
						<DeleteIcon title='Delete user' />
						</LabelledIcon>
					</button>
				</div>
			</div>
		</div>

		<div class='flex justify-center'>
			<Loading v-if='users.loading' class='text-center' />
		</div>
	</div>
</template>

<script>
import AddIcon from 'icons/AccountPlus'
import EditIcon from 'icons/Pencil'
import DeleteIcon from 'icons/Delete'

import {UserList} from '@/models/User'

import Error from '@/components/util/status/Error'
import LabelledIcon from '@/components/util/LabelledIcon'
import Loading from '@/components/util/status/Loading'

export default {
	name: 'UserTable',
	components: {
		AddIcon,
		EditIcon,
		Error,
		DeleteIcon,
		LabelledIcon,
		Loading
	},
	data() { return {
		users: new UserList(),
		errMsg: ''
	}},
	methods: {
		getUsers() {
			this.users.fetch().then(() => {
				this.errMsg = ""
			}).catch((error) => {
				this.errMsg = "Failed to get users list: " + error.message
				if (error.response.response.status == 401) {
					this.errMsg = "Session expired, please sign in again and then click retry."
				}
			})
		}
	},
	mounted() {
		this.getUsers()
	}
}
</script>

<style scoped>
.userCard {
	@apply border border-gray-400 rounded mb-4;
	& .flex {
		@apply px-2 py-1;
	}
}
</style>
