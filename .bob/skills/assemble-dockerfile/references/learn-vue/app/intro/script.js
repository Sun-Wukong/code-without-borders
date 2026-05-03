import {createApp} from 'vue';

// Create a RootComponent object as an entrypoint to the web app
const RootComponent = {
    data: () => {
        return {
            valueToReturn: "Hiiiiiiiiiiii"
        }
    }
};
// Treat "app" as a Singleton... as in invoke it for nearly everything
const app = createApp(RootComponent);
// Attach | Mount app obj to DOM element(usually a div) 
const appInst = app.mount("#app");
console.log(appInst.valueToReturn)
/* 
// Define UI Component
app.component("UserInput", UserInputComponent)
// Define UI action
app.directive("blur", BlurDirective)
// Load Vue Plugin
app.use(LocalPlugin)
 */