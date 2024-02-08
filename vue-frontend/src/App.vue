<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>Automated Form Submission</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/">Home</v-btn>
      <v-btn text to="/form-submissions">Form Submissions</v-btn>
      <v-btn text to="/data-collection-form">Data Collection Form</v-btn>
    </v-app-bar>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'App'
};
</script>