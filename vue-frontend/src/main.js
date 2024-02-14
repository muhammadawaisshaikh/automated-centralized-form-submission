/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'
import { createClient } from '@supabase/supabase-js';
// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import router from './router';

const supabaseUrl = 'https://yfmoyatjmqtgkybbfwtc.supabase.co';
const supabaseKey = process.env.SUPABASE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

const app = createApp(App)

registerPlugins(app)
app.use(router)
app.provide('supabase', supabase)
app.mount('#app')
