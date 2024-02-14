<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-form @submit.prevent="submitForm">
        <v-row>
          <v-col xl="12">
            <h1>Data Collection Form</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col xl="12">
            <v-text-field v-model="formData.firstName" label="Vorname" required hide-details class="mb-6"></v-text-field>
            <v-text-field v-model="formData.lastName" label="Nachname" required hide-details class="mb-6"></v-text-field>
            <v-text-field v-model="formData.street" label="Strasse" required hide-details class="mb-6"></v-text-field>
            <v-text-field v-model="formData.housenr" label="Hausnr." required hide-details class="mb-6"></v-text-field>
            <v-text-field v-model="formData.zipcode" label="PLZ" required hide-details class="mb-6"></v-text-field>
            <v-text-field v-model="formData.city" label="Stadt" required hide-details class="mb-6"></v-text-field>
          </v-col>
        </v-row>
        <v-btn type="submit">Submit</v-btn>
      </v-form>
    </v-responsive>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const formData = ref({
  firstName: '',
  lastName: '',
  street: '',
  housenr: '',
  zipcode: '',
  city: ''
});

const submitForm = () => {
  console.log(formData.value);

  // consume API to hit Python Selenium script to automate the form filling 
  axios.post('http://127.0.0.1:5000/execute', formData.value)
    .then(response => {
      console.log(response);
      alert('Data sent Successfully!');
    })
    .catch(error => {
      console.error(error);
      alert(error);
    });
};
</script>
