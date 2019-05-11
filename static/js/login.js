new Vue({
        el: '#app',
        data() {
            return {
                username: "",
                password: "",
                // base_url: "http://localhost:8880",
                base_url: location.origin,
            }
        },
        methods: {
            login() {
                var arg = {'username': this.username, 'password': this.password}
                fly.post(this.base_url + '/login', arg).then(res => {
                    var res = res.data
                    console.log(res)
                    if (res.code == 200) {
						localStorage.setItem('token',res.data)
						window.location.href='./index.html'
                    } else {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'error'
                        });
                    }
                })
            }
        }
    })