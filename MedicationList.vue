<template>
  <div>
    <h1>Medication List</h1>
    <ul>
      <li v-for="medication in medications" :key="medication.id">
        {{ medication.name }} - {{ medication.dosage }} - {{ medication.quantity }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      medications: []
    };
  },
  mounted() {
    this.fetchMedications();
  },
  methods: {
    async fetchMedications() {
      try {
        const response = await fetch('http://localhost:8000/api/medications/');
        this.medications = await response.json();
      } catch (error) {
        console.error('Error fetching medications:', error);
      }
    }
  }
};
</script>
