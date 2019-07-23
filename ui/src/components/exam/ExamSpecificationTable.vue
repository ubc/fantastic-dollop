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

		<draggable v-model='components.models'>
			<div v-for='(component, index) in components.models' :key='component.name'
				class='border border-gray-400 p-3 flex'>

				<!-- Component sequence number -->
				<div class='flex-initial px-2 font-bold'>
				{{ index+1 }}
				</div>

				<!-- Component Type -->
				<div class='flex-1 px-2'>
				{{ component.exam_component_type }}
				</div>

				<!-- Page Start/End -->
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

				<!-- Sources -->
				<div class='flex-1 px-2'>
					<h5>Sources</h5>
					<div v-if='component.id in componentSources'>
						<div v-if='!componentSources[component.id].models.length'
							class='text-red-600 italic'>
							No Sources Defined
						</div>
						<div v-for='componentSource in componentSources[component.id].models'
							:key='componentSource.id'>
							<span class='italic'>{{ componentSource.exam_source_name }}</span>
							<button class='text-gray-600 hover:text-red-600 ml-1 p-1 text-lg'
								v-on:click='componentSource.delete'><RemoveIcon /></button>
						</div>
						<AddExamComponentSource
						:componentSources='componentSources[component.id].models'
						:componentId='component.id'
						v-on:add-component-source='addComponentSource' />
					</div>
				</div>

				<!-- Thumbnails -->
				<div class='flex-1 px-2'>
				thumbnails
				</div>

				<!-- Mark -->
				<div class='flex-1 px-2 text-center'>
					<div class='' v-if='component.exam_component_type=="Question"'>
						<label>Mark</label>
						<input type='number' min='0' v-model='component.mark' required />
					</div>
				</div>

				<!-- Comment -->
				<div class='flex-1 px-2'>
					<label>Comment</label>
					<textarea v-model='component.comment' />
				</div>

				<!-- Delete -->
				<div class='flex-initial self-center'>
					<button class='btnRegular' v-on:click='deleteComponent(component)'>
						<LabelledIcon label='Delete'>
							<DeleteIcon/>
						</LabelledIcon>
					</button>
				</div>
			</div>
		</draggable>

		<button class='btnPrimary my-3' v-on:click='save'>
			<LabelledIcon label='Save'>
				<SaveIcon />
			</LabelledIcon>
		</button>
	</div>
</template>

<script>
import draggable from 'vuedraggable'
import AddIcon from 'icons/Plus'
import DeleteIcon from 'icons/Delete'
import RemoveIcon from 'icons/MinusCircleOutline'
import SaveIcon from 'icons/Check'


import LabelledIcon from '@/components/util/LabelledIcon'
import AddExamComponentSource from '@/components/exam/AddExamComponentSource'

import {ExamComponent, ExamComponentList} from '@/models/ExamComponent'
import {ExamComponentSource, ExamComponentSourceList} from '@/models/ExamComponentSource'
import {ExamComponentTypeList} from '@/models/ExamComponentType'

export default {
	name: 'ExamSourceTable',
	components: {
		draggable,
		AddExamComponentSource,
		AddIcon,
		DeleteIcon,
		LabelledIcon,
		RemoveIcon,
		SaveIcon
	},
	computed: {
		sourceMaxPageCount() {
			return this.$store.getters['exam/getSourceMaxPageCount']
		}
	},
	data() { return {
		components: new ExamComponentList(),
		componentTypes: new ExamComponentTypeList(),
		componentSources: {},
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

		addComponentSource(data) {
			let newComponentSource = new ExamComponentSource()
			newComponentSource.set('course_id', this.$route.params.courseId)
			newComponentSource.set('exam_id', this.$route.params.examId)
			newComponentSource.set('exam_component_id', data.componentId)
			newComponentSource.set('exam_source_id', data.addSourceId)
			newComponentSource.save().then(() => {
				this.componentSources[data.componentId].add(newComponentSource)
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to add exam component source."})
			})
		},

		save() {
			let promises = []
			this.components.models.forEach((value, i) => {
				value.sequence = i+1
				promises.push(value.save())
			})
			Promise.all(promises).then(() => {
				//this.$notify({title: "Saved exam components.", type: 'success'})
				this.$emit('save')
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to save exam component.'})
			})
		},

		deleteComponent(component) {
			component.delete().then(() => {
				this.$notify({title: "Component deleted.", type: 'success'})
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to delete exam component."})
			})
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
		this.components.fetch().then(() => {
			this.components.models.forEach((value) => {
				// get each component's sources
				let sourceList = new ExamComponentSourceList()
				sourceList.set('course_id', courseId)
				sourceList.set('exam_id', examId)
				sourceList.set('exam_component_id', value.id)
				sourceList.fetch().then(() => {
					this.$set(this.componentSources, value.id, sourceList)
				}).catch((error) => {
					this.$store.commit('error/add', {error: error,
						message: "Failed to get exam component sources."})
				})
			})
		}).catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: "Failed to get exam components."})
		})
	}
}
</script>
