<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-table>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">First Name</th>
            <th class="text-left">Last Name</th>
            <th class="text-left">Street</th>
            <th class="text-left">House</th>
            <th class="text-left">Zip Code</th>
            <th class="text-left">City</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in data" :key="item.id">
            <td class="text-left">{{ item.id }}</td>
            <td class="text-left">{{ item.firstName }}</td>
            <td class="text-left">{{ item.lastName }}</td>
            <td class="text-left">{{ item.street }}</td>
            <td class="text-left">{{ item.housenr }}</td>
            <td class="text-left">{{ item.zipcode }}</td>
            <td class="text-left">{{ item.city }}</td>
          </tr>
        </tbody>
      </v-table>
    </v-responsive>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

const data = ref([
  {
    id: 1,
    firstName: 'Dietrich',
    lastName: 'Coding',
    street: '324 Sample Street',
    housenr: '12',
    zipcode: '89978',
    city: 'Hamburg'
  },
  {
    id: 2,
    firstName: 'Dietrich',
    lastName: 'Coding',
    street: '324 Sample Street',
    housenr: '12',
    zipcode: '89978',
    city: 'Hamburg'
  },
]);
</script>
