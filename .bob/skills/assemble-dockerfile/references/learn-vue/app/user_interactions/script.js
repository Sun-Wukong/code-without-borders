// Create a RootComponent object as an entrypoint to the web app
const RootComponent = {
    data() {
        return {
            text: "Hiiiiiiiiiiii"
        }
    },
    methods: {
        checkPalindrome() {
            this.text = this.text.split("").reverse().join("")
        }
    }
};
// Treat "app" as a Singleton... as in invoke it for nearly everything
const app = Vue.createApp(RootComponent);
// Attach | Mount app obj to DOM element(usually a div) 
const appInst = app.mount("#textToReverse");
console.log(appInst.text)
