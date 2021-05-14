/*
TO AJAX
<hook>() {
		axios
			.get('/api')
			.then(response => (this.msg = response.data.var));
	
*/

const app = Vue.createApp({
	data() {
		return {
			posts: [],
			cat: "All",
			PostUrl: '/blog/post/',
			url: '/static/assets/img/',
			fr: '.jpg'
		}
	},
	mounted() {
		axios
			.get('/api/posts')
			.then(response => (this.posts = response.data.posts));
	},
	computed: {
		Categorized() {
			if (this.cat == 'All') {
				return this.posts
			} else {
				return this.posts.filter(post => post.cat == this.cat)
			}
		}
	}
	
}).mount("#app");
