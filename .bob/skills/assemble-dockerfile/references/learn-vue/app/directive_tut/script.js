const ReactiveBehavior = {
    data() {
        return {
            onHoverText: "Reactive hover+---"
        }
    }
}

Vue.createApp(ReactiveBehavior).mount("#to-hover-element")