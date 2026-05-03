// Create hook functions that respond to reaching app
// lifecycle stages
const app = Vue.createApp({
    // Arbitrary hook
    data() {
        return {
            aValue: "Made"
        }
    },
    // Hook for "created" stage / state
    created() {
        console.log(this.aValue)
    }
}).mount("#app");
