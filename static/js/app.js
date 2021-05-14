const app = Vue.createApp({
	data() {
		return {
			avatars: [],
			avator: '',
			PrimaryAV: '',
			ajax: 'getuser',
			baseMedia: '/media/'
		}
	},
	created() {
		axios
			.get('/api/' + this.ajax)
			.then(response => (this.avator = response.data.avatar));
		axios
			.get('/api/avatar/')
			.then(response => (this.avatars = response.data.avatars));
		axios
			.get('/api/' + this.ajax)
			.then(response => (this.PrimaryAV = response.data.avatar));
	},
	computed: {
		Avatar() {
			return this.avatars.filter(avatar => avatar.avatar == this.avator)
		},
		Choices() {
			return this.avatars.filter(avatar => avatar.avatar != this.PrimaryAV)
		}
	}
	
}).mount("#app");
