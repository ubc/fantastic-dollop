<!-- Table that lists users in the database -->
<template>
	<div>
		<h3>Users List</h3>
		<router-link :to="{name: 'addUser'}" tag="button" class='btnRegular'>
			<LabelledIcon label='Add'><AddIcon title='Add a new user' /></LabelledIcon>
		</router-link>
		<table>
			<caption>Users List</caption>
			<thead>
				<tr>
					<th class='invisible'>Edit</th>
					<th>Username</th>
					<th>Preferred Name</th>
					<th>Name</th>
					<th>Email</th>
					<th>Student Number</th>
					<th class='invisible'>Delete</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="user in users.models" :user="user" :key="user.id">
					<td>
						<router-link :to="{name: 'editUser', params:{userId: user.$.id}}"
							tag="button" class='btnRegular'>
							<LabelledIcon label='Edit'>
								<EditIcon title='Edit user' />
							</LabelledIcon>
						</router-link>
					</td>
					<td>{{ user.$.username }}</td>
					<td>{{ user.$.preferredName }}</td>
					<td>{{ user.$.name }}</td>
					<td>{{ user.$.email }}</td>
					<td>{{ user.$.studentNumber }}</td>
					<td>
						<button class='btnRegular'>
							<LabelledIcon label='Delete'>
								<DeleteIcon title='Delete user' />
							</LabelledIcon>
						</button>
					</td>
				</tr>
			</tbody>
		</table>
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
	data() { return {
		users: new UserList()
	}},
	mounted() {
		console.log("################### GETTING USER LIST")
		this.users.fetch().then((response) => {
			console.log("Get users success")
			console.log(response)
		}).catch((error) => {
			console.log("Get users list failed")
			console.log(error)
		})
	}
}
</script>

<style>
th, td {
	@apply px-2 py-1 m-1 text-left;
}
</style>
