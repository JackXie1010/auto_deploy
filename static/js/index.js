new Vue({
        el: "#root",
        data() {
            return {
                msg: "hello vue",
                token: localStorage.getItem('token'),
                tableData: [],
                // base_url: "http://localhost:8880",
                base_url: location.origin,
                showAddDialog: false,
                addData: {
                    name: '',
                    host: '',
                    password: '',
                    projectDir: '',
                    isOnline: '',
                    status: '',
                }
            }
        },
        methods: {
            getData() {
                // var token = localStorage.getItem('token');
                fly.get(this.base_url + '/getConf?token=' + this.token).then(res => {
                    console.log(res)
                    var res = res.data
                    if (res.code == 200) {
                        this.tableData = res.data
                    } else {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'error'
                        });
                    }
                })
            },
            //--------------------------------------------------------------
            deploy(row) {
                console.log(row)
                fly.post(this.base_url + '/deploy', row).then(res => {
                    var res = res.data
                    if (res.code == 200) {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'error'
                        });
                    }
                })
            },
            //--------------------------------------------------------------
            updateConf(row) {
                row.token = this.token
                console.log(row)
                fly.post(this.base_url + '/updateConf', row).then(res => {
                    var res = res.data
                    if (res.code == 200) {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'error'
                        });
                    }
                })
            },
            // ---------------------------------------------------------------------------
            delConf(id) {
                console.log(id)
                this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    fly.post(this.base_url + '/delConf', {'id': id, 'token': this.token}).then(res => {
                        var res = res.data
                        if (res.code == 200) {
                            this.$message({
                                showClose: true,
                                message: res.msg,
                                type: 'success'
                            });
                            this.getData()
                        } else {
                            this.$message({
                                showClose: true,
                                message: res.msg,
                                type: 'error'
                            });
                        }
                    })

                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });


            },

            // ----------------------------------------------------------------------------------
            add() {
                this.addData.token = this.token
                console.log(this.addData)
                fly.post(this.base_url + '/addConf', this.addData).then(res => {
                    var res = res.data
                    if (res.code == 200) {
                        this.showAddDialog = false
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'success'
                        })
                        this.getData()
                    } else {
                        this.$message({
                            showClose: true,
                            message: res.msg,
                            type: 'error'
                        });
                    }
                })
            }
        },
        mounted() {
            this.getData()
        }
    })