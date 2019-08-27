<!-- Table that lists users in the database -->
<template>
	<div>
		<router-link :to="{name: 'adminAddUser'}" tag="button" class='btnRegular mb-4' >
			<LabelledIcon label='Add'><AddIcon title='Add a new user' /></LabelledIcon>
		</router-link>

		<div class='flex flex-col md:table'>
			<div class='hidden md:table-row'>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Username</div>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Preferred Name</div>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Name</div>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Email</div>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Student Number</div>
				<div class='p-1 font-bold md:table-cell'>Actions</div>
			</div>
			<div v-for="user in users" :user="user" :key="user.id"
				class='border flex-auto p-1 border rounded mb-2 md:table-row'>
				<!-- info fields -->
				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Username</div>
					{{ user.username }}
				</div>

				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Preferred Name</div>
					{{ user.preferredName }}
				</div>

				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Name</div>
					{{ user.name }}
				</div>

				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Email</div>
					{{ user.email }}
				</div>

				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Student Number</div>
					{{ user.studentNumber }}
				</div>
				<!-- edit buttons -->
				<div class='flex mt-2 md:p-1 md:table-cell'>
					<div class='flex-1 md:inline-block'>
						<router-link :to="{name: 'adminEditUser',params:{userId: user.id}}"
							tag="button" class='btnRegular md:mr-2'>
							<LabelledIcon label='Edit'>
							<EditIcon title='Edit user' />
							</LabelledIcon>
						</router-link>
					</div>
					<div class='flex-initial md:inline-block'>
						<button class='btnRegular' type='button'
							v-on:click='deleteUser($event, user)'>
							<LabelledIcon label='Delete'>
							<DeleteIcon title='Delete user' />
							</LabelledIcon>
						</button>
					</div>
				</div>

			</div>
		</div>

		<div class='flex justify-center my-2' v-show='users.loading' >
			<Loading class='text-center' />
		</div>
	</div>
</template>

<script>
import AddIcon from 'icons/AccountPlus'
import EditIcon from 'icons/Pencil'
import DeleteIcon from 'icons/Delete'

import { User } from '@/models/User'

import LabelledIcon from '@/components/util/LabelledIcon'
import Loading from '@/components/util/status/Loading'

export default {
	name: 'UserTable',
	components: {
		AddIcon,
		EditIcon,
		DeleteIcon,
		LabelledIcon,
		Loading
	},
	computed: {
		users() {
			return User.all()
		}
	},
	data() { return {
	}},
	methods: {
		/*
		getUsers() {
			this.users.fetch().then().catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to get users list."})
			})
		},
		deleteUser(event, user) {
			user.delete().then().catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to delete user."})
			})
		}
		*/
	},
	mounted() {
		User.$fetch().then(()=> {
			console.log("Got Users")
			console.log(this.users)
		})
	}
}
</script>

<style scoped>
</style>
