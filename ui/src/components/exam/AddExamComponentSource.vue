<template>
	<div v-if='sources && sources.length'>
		<select class='mt-3' v-model='addSourceId'>
			<option v-for='source in sources' :key='source.id'
			:value='source.id'>
			{{ source.name }}
			</option>
		</select>
		<button class='btnRegular mt-1' v-on:click='addComponentSource'>
			<LabelledIcon label='Add'>
				<AddIcon />
			</LabelledIcon>
		</button>
	</div>
</template>

<script>
import AddIcon from 'icons/Plus'

import LabelledIcon from '@/components/util/LabelledIcon'

export default {
	name: 'AddExamComponentSource',
	components: {
		AddIcon,
		LabelledIcon
	},
	computed: {
		allSources() {
			return this.$store.state.exam.sources
		},
		excludeSourceIds() {
			let excludeIds = {}
			this.componentSources.forEach((value) => {
				excludeIds[value.exam_source_id] = true
			})
			return excludeIds
		},
		sources() {
			let ret = []
			this.allSources.forEach((source) => {
				if (!(source.id in this.excludeSourceIds))
					ret.push(source)
			})
			return ret
		}
	},
	data() { return {
		addSourceId: 0
	}},
	props: ['componentSources', 'componentId'],
	methods: {
		addComponentSource() {
			this.$emit('add-component-source', 
				{
					addSourceId: this.addSourceId,
					componentId: this.componentId
				}
			)
		},
		updateDefaultSourceId() {
			if (this.sources.length) this.addSourceId = this.sources[0].id
		}
	},
	mounted() {
		this.updateDefaultSourceId()
	},
	watch: {
		sources: function() {
			this.updateDefaultSourceId()
		}
	}
}
</script>

<style>
</style>
