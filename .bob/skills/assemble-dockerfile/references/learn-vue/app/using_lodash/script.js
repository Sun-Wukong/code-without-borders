const app = Vue.createApp({

})

app.component("submitButton", {
    created() {
        this.debouncedClick = _.debounce
        (this.click, 300)
    },
    unmounted() {
        this.debouncedClick.cancel()
    }
})