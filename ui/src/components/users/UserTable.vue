<!-- Table that lists users in the database -->
<template>
	<div>
		<h3>Users List</h3>
		<router-link :to="{name: 'addUser'}" tag="button">
			<ion-icon name='add'></ion-icon>
			Add
		</router-link>
		<Loading v-if='users.loading' />
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
							tag="button">
							<ion-icon name='create'></ion-icon>
							Edit
						</router-link>
					</td>
					<td>{{ user.$.username }}</td>
					<td>{{ user.$.preferredName }}</td>
					<td>{{ user.$.name }}</td>
					<td>{{ user.$.email }}</td>
					<td>{{ user.$.studentNumber }}</td>
					<td>
						<button>Delete</button>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import Loading from '@/components/util/Loading'
import {UserList} from '@/models/User'

export default {
	name: 'UserTable',
	components: {
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
</style>
