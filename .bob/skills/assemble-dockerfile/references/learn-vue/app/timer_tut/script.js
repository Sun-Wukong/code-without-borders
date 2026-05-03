const app = {
    data() {
        return {
            timer: 0
        }
    },
    mounted() {
        setInterval(() => {
            this.timer++
        }, 1000)
    }
}

const timerApp = Vue.createApp(app).mount("#app")