const InterpolateApp = {
    data() {
        return {
            html: "<span style='color: blue'>Interpolated text</span>"
        }
    }
}

Vue.createApp(InterpolateApp).mount("#app")