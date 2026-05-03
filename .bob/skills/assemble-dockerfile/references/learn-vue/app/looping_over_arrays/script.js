const app = Vue.createApp({
    data() {
        return {
            items: [
                { content: "Item a" },
                { content: "Item c" }
            ]
        }
    }
}).mount("#to-loop-array")