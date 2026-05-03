// Create a RootComponent object as an entrypoint to the web app
const RootComponent = {
    data() {
        return {
            visible: true
        }
    }
    // methods: {
    //     checkPalindrome() {
    //         this.text = this.text.split("").reverse().join("")
    //     }
    // }
};
// Treat "app" as a Singleton... as in invoke it for nearly everything
const app = Vue.createApp(RootComponent);
// Attach | Mount app obj to DOM element(usually a div) 
const appInst = app.mount("#conditionalVisibility");
console.log(appInst.visible)
/* 
// Define UI Component
app.component("UserInput", UserInputComponent)
// Define UI action
app.directive("blur", BlurDirective)
// Load Vue Plugin
app.use(LocalPlugin)
 */