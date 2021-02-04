import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuelidate from 'vuelidate'
// import Vuetify from 'vuetify' Not compatible with Vue 3!
// import 'vuetify/dist/vuetify.min.css'
import Primevue from 'primevue/config'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Toast from 'primevue/toast'
import ToastService from 'primevue/toastservice'
import Card from 'primevue/card';

import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // icons
import 'primeflex/primeflex.css' // CSS Utility Library

// createApp(App).use(store).use(router).use(Primevue).mount('#app')
const app = createApp(App)
app.use(store).use(router).use(Vuelidate).use(Primevue).use(ToastService)

app.component('InputText', InputText)
app.component('Button', Button)
app.component('Toast', Toast)
app.component('Card', Card)

app.mount('#app')
