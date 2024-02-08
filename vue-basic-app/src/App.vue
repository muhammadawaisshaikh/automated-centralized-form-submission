<template>
  <a href="#/">Home</a> |
  <a href="#/form-submissions">Form Submissions</a> |
  <a href="#/data-collection-form">Data Collection Form</a>
  <component :is="currentView" />
</template>

<script setup>

import { ref, computed } from 'vue'
import Home from './components/Home.vue'
import FormSubmissions from './components/FormSubmissions.vue'
import DataCollectionForm from './components/data-collection-form.vue'
import NotFound from './components/NotFound.vue'

const routes = {
  '/': Home,
  '/form-submissions': FormSubmissions,
  '/data-collection-form': DataCollectionForm
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>