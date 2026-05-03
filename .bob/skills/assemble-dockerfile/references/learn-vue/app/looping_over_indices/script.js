import {createApp} from 'vue';

const app = createApp({
    data() {
        return {
            items: [
                {content: "This "},
                {content: "mfa "},
                {content: "spittin"}
            ]
        }
    }
}).mount("#app")