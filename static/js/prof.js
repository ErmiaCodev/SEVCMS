const app = Vue.createApp({
	data() {
		return {
			avatars: [],
			avator: '',
			ajax: 'getuser',
			baseMedia: '/media/',
			username: '',
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
			.then(response => (this.username = response.data.name));
		
	},
	computed: {
		Avatar() {
			return this.avatars.filter(avatar => avatar.avatar == this.avator)
		}
	}
	
}).mount("#app");
