<template>
	<div>
		<form class='formSingle mb-3 border-gray-400 border rounded pl-2 py-2
			inline-block' @submit.prevent='addComponent'>
			<label for='addComponent'>Add Component</label>
			<select id='addComponent' v-model.number='addComponentType'>
				<option v-for='componentType in componentTypes.models'
					:key='componentType.id' :value='componentType.id'>
					{{ componentType.name }}
				</option>
			</select>
			<button class='btnRegular ml-2'>
				<LabelledIcon label='Add'>
					<AddIcon title='Add a new exam component' />
				</LabelledIcon>
			</button>
		</form>

		<div v-for='source in sources' :key='source.id'>
			{{ source.name }}
		</div>

		<draggable v-model='components.models'>
			<div v-for='(component, index) in components.models' :key='component.name'
				class='border border-gray-400 p-3 flex'>
				<div class='flex-1 px-2'>
				{{ index+1 }}
				</div>

				<div class='flex-1 px-2'>
				{{ component.exam_component_type }}
				</div>

				<div class='flex-1 flex flex-col px-2'>
					<div class='flex mb-2'>
						<label :for='component.id+"pageEnd"' class='pr-1'>Start</label>
						<select :id='component.id+"pageEnd"' required
							v-model.number='component.page_start'>
							<option v-for='n in sourceMaxPageCount' :key='n' :value='n'>
								{{ n }}</option>
						</select>
					</div>
					<div class='flex'>
						<label :for='component.id+"pageEnd"' class='pr-1'>End</label>
						<select :id='component.id+"pageEnd"' required
							v-model.number='component.page_end'>
							<option v-for='n in sourceMaxPageCount' :key='n' :value='n'>
								{{ n }}</option>
						</select>
					</div>
				</div>

				<div class='flex-1 px-2'>
				{{ component.id }}
				Sources
				</div>
				<div class='flex-1 px-2'>
				thumbnails
				</div>
				<div class='flex-1 px-2 text-center'>
					<div class='' v-if='component.exam_component_type=="Question"'>
						<label>Mark</label>
						<input type='number' min='0' v-model='component.mark' required />
					</div>
				</div>
				<div class='flex-1 px-2'>
					<label>Comment</label>
					<textarea v-model='component.comment' />
				</div>
			</div>
		</draggable>
		<button class='btnPrimary my-3' v-on:click='save'>Save</button>
	</div>
</template>

<script>
import draggable from 'vuedraggable'
import AddIcon from 'icons/Plus'

import LabelledIcon from '@/components/util/LabelledIcon'

import {ExamComponent, ExamComponentList} from '@/models/ExamComponent'
import {ExamComponentTypeList} from '@/models/ExamComponentType'

export default {
	name: 'ExamSourceTable',
	components: {
		draggable,
		AddIcon,
		LabelledIcon,
	},
	computed: {
		sources() {
			return this.$store.state.exam.sources
		},
		sourceMaxPageCount() {
			return this.$store.getters['exam/getSourceMaxPageCount']
		}
	},
	data() { return {
		components: new ExamComponentList(),
		componentTypes: new ExamComponentTypeList(),
		addComponentType: 3
	}},
	methods: {
		addComponent() {
			let component = new ExamComponent()
			component.exam_component_type_id = this.addComponentType
			component.course_id = this.$route.params.courseId
			component.exam_id = this.$route.params.examId
			component.sequence = this.components.models.length
			component.save().then(() => {
				this.$notify({title: "Added new '" + component.exam_component_type +
					"' component.", type: 'success'})
				this.components.add(component)
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to add exam component."})
			})
		},
		save() {
			let error = null
			this.components.models.forEach((value, i) => {
				value.sequence = i+1
				value.save().catch((e) => {
					if (!error) error = e
				})
			})
			if (error)
				this.$store.commit('error/add', {error: error,
					message: 'Failed to save exam component.'})
			else
				this.$notify({title: "Saved exam components.", type: 'success'})
		}
	},
	mounted() {
		let courseId = this.$route.params.courseId
		let examId = this.$route.params.examId

		this.components.set('course_id', courseId)
		this.components.set('exam_id', examId)

		this.componentTypes.fetch().catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: "Failed to get exam component types."})
		})
		this.components.fetch().catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: "Failed to get exam components."})
		})
	}
}
</script>
