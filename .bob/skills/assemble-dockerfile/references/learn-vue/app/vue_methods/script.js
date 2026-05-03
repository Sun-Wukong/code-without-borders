const app = Vue.createApp({
    data() {
        return {
            sampleStr: "Hello "
        }
    },
    // custom functions for Vue Component
    methods: {
        addToString() {
            this.sampleStr += " Haiii"
        }
    }
})

const componentInst = app.mount("#app")