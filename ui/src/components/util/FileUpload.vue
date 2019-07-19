<!-- Based on vue-simple-upload, modified to use axios instead of xmlhttprequest,
CSS themed the upload button -->
<template>
	<label class='btnRegular inline-block mb-3'>
		<UploadIcon title='Upload a new exam' class='text-lg' /> Upload
		<input type="file" name="file" @change="onFileChange"
			class='hidden'>
	</label>
</template>

<script type="text/babel">
import UploadIcon from 'icons/Upload'

export default {
  name: 'fileupload',
	components: {
		UploadIcon
	},
  props: {
    target: {
      type: String
    },
    action: {
      type: String,
      default: 'POST'
    },
    alias: {
      type: String
    },
  },
  data () {
    return {
      file: null
    }
  },
  methods: {
    emitter (event, data) {
      this.$emit(event, data)
    },
    uploadProgress (oEvent) {
      let vm = this
      if (oEvent.lengthComputable) {
        let percentComplete = Math.round(oEvent.loaded * 100 / oEvent.total)
        vm.emitter('progress', percentComplete)
      } else {
        // Unable to compute progress information since the total size is unknown
        vm.emitter('progress', false)
      }
    },
    getCookie: function(name)
    {
        var arr,reg = new RegExp("(^| )"+name+"=([^;]*)(;|$)");
        if(arr==document.cookie.match(reg))
        {
            return unescape(arr[2]);
        }
        else
        {
            return null;
        }
    },
    onFileChange (e) {
      let vm = this

      if (!this.target || this.target === '') {
        console.log('Please provide the target url')
      } else if (!this.action || this.action === '') {
        console.log('Please provide file upload action ( POST / PUT )')
      } else if (this.action !== 'POST' && this.action !== 'PUT') {
        console.log('File upload component only allows POST and PUT Actions')
      } else {
        let files = e.target.files || e.dataTransfer.files

        if (!files.length) {
          return
        }

        this.file = files[0]
        let formData = new FormData()
        formData.append(this.alias, this.file)

				vm.emitter('start', e)
				this.axios.post(this.target,
					formData,
					{
						headers: {
							'Content-Type': 'multipart/form-data'
						},
						onUploadProgress: this.uploadProgress
					}
				).then(function(e){
          vm.emitter('finish', e)
				}).catch(function(e){
          vm.emitter('error', e)
					this.$store.commit('error/add', {error: e,
						message: 'Failed to upload file: ' + this.file.name})
				});
      }
    }
  }
}
</script>

