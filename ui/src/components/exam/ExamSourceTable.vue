<template>
	<div>
		<FileUpload :target="uploadSourceUrl" alias="file" v-on:error='uploadError'
			v-on:finish='uploadFinish' v-on:progress='uploadProgress'></FileUpload>
		<span class='mx-2'>{{ uploadStatus }}</span>


		<div class='border-gray-400 border-t mb-3'>
			<!-- source card -->
			<div v-for='source in sources.models' :key='source.id'
				class='py-2 border-b border-gray-400 flex'>
				<!-- source info -->
				<div class='flex-auto mr-3'>
					<router-link to='/courses/1/sources/1'>
						<h4 class='break-all'>
							{{ source.name }}
						</h4>
					</router-link>
				</div>
				<!-- source controls -->
				<div class='flex-initial self-center flex'>
					<button class='btnRegular' type='button'
						v-on:click='deleteSource($event, source)'>
						<LabelledIcon label='Delete'>
							<DeleteIcon title='Delete source' />
						</LabelledIcon>
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import DeleteIcon from 'icons/Delete'

import FileUpload from '@/components/util/FileUpload'
import LabelledIcon from '@/components/util/LabelledIcon'

import {ExamSource, ExamSourceList} from '@/models/ExamSource'

export default {
	name: 'ExamSourceTable',
	components: {
		DeleteIcon,
		FileUpload,
		LabelledIcon,
	},
	data() { return {
		sources: new ExamSourceList(),
		uploadSourceUrl: "",
		uploadStatus: ""
	}},
	methods: {
		deleteSource(event, source) {
			let sourceName = source.name
			source = this.sources.remove(source)
			source.delete().then(() => {
				this.$notify({title: "Exam source file '"+ sourceName +"' was deleted.",
					type: 'success'})
				this.$store.commit('exam/setSources', this.sources.models)
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to delete exam source file "' + sourceName + '".'})
			})
		},

		uploadError() {
			this.uploadStatus = "Upload Failed"
		},

		uploadFinish(e) {
			let source = new ExamSource(e.data)
			this.sources.add(source)
			setTimeout(() => { this.uploadStatus = "" }, 500)
			this.$store.commit('exam/setSources', this.sources.models)
		},

		uploadProgress(e) {
			this.uploadStatus = e + "%"
		}
	},
	mounted() {
		let examId = this.$route.params.examId
		let courseId = this.$route.params.courseId

		this.uploadSourceUrl = '/courses/'+ courseId +'/exams/'+ examId +'/sources'

		this.sources.set('course_id', courseId)
		this.sources.set('exam_id', examId)
		this.sources.fetch().then(() => {
			this.$store.commit('exam/setSources', this.sources.models)
		}).catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: "Failed to get exam sources."})
		})
	}
}
</script>
