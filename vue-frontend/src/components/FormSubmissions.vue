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
import { ref, onMounted, inject } from 'vue';
const supabase = inject('supabase');

const data = ref([]);

// Fetch data from Supabase
const fetchData = async () => {
  try {
    const { data: records, error } = await supabase
      .from('data-logs')
      .select('*');

    if (error) {
      throw new Error(error.message);
    }

    data.value = records;
  } catch (error) {
    console.error('Error fetching data from Supabase:', error.message);
  }
};

// Fetch data when the component is mounted
onMounted(fetchData);
</script>
