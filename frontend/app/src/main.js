import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// axios
import axios from 'axios'
import VueAxios from 'vue-axios'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'


const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'dark'
  }
})

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.use(VueAxios, axios)

app.mount('#app')