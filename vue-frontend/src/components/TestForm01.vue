<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-form @submit.prevent="submitForm">
        <v-row>
          <v-col xl="12">
            <h1>Test Form 01</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col xl="12">
            <v-text-field id="firstName" v-model="formData.firstName" label="Vorname" required hide-details class="mb-6"></v-text-field>
            <v-text-field id="lastName" v-model="formData.lastName" label="Nachname" required hide-details class="mb-6"></v-text-field>
            <v-text-field id="street" v-model="formData.street" label="Strasse" required hide-details class="mb-6"></v-text-field>
            <v-text-field id="housenr" v-model="formData.housenr" label="Hausnr." required hide-details class="mb-6"></v-text-field>
            <v-text-field id="zipcode" v-model="formData.zipcode" label="PLZ" required hide-details class="mb-6"></v-text-field>
            <v-text-field id="city" v-model="formData.city" label="Stadt" required hide-details class="mb-6"></v-text-field>
          </v-col>
        </v-row>
        <v-btn type="submit" id="submit_button">Submit</v-btn>
      </v-form>
    </v-responsive>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

const formData = ref({
  firstName: '',
  lastName: '',
  street: '',
  housenr: '',
  zipcode: '',
  city: ''
});

const submitForm = async () => {
  console.log('Automated form filled successfully!', formData.value);
};
</script>
