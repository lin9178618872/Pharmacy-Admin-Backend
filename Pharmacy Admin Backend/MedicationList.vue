<template>
  <div>
    <h1>Medication List</h1>
    <button @click="showCreateForm = !showCreateForm">Add New Medication</button>

    <!-- Create Form -->
    <div v-if="showCreateForm">
      <h2>Create Medication</h2>
      <form @submit.prevent="createMedication">
        <input v-model="newMedication.name" placeholder="Medication Name" required />
        <input v-model="newMedication.dosage" placeholder="Dosage" required />
        <input v-model="newMedication.quantity" type="number" placeholder="Quantity" required />
        <input v-model="newMedication.expiration_date" type="date" required />
        <button type="submit">Create</button>
      </form>
    </div>

    <!-- Medication List -->
    <ul>
      <li v-for="medication in medications" :key="medication.id">
        <div>
          {{ medication.name }} - {{ medication.dosage }} - {{ medication.quantity }}
          <button @click="editMedication(medication)">Edit</button>
          <button @click="deleteMedication(medication.id)">Delete</button>
        </div>

        <!-- Edit Form -->
        <div v-if="editing && editing.id === medication.id">
          <h2>Edit Medication</h2>
          <form @submit.prevent="updateMedication">
            <input v-model="editing.name" placeholder="Medication Name" required />
            <input v-model="editing.dosage" placeholder="Dosage" required />
            <input v-model="editing.quantity" type="number" placeholder="Quantity" required />
            <input v-model="editing.expiration_date" type="date" required />
            <button type="submit">Update</button>
          </form>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      medications: [],
      newMedication: {
        name: '',
        dosage: '',
        quantity: '',
        expiration_date: ''
      },
      editing: null,
      showCreateForm: false
    };
  },
  mounted() {
    this.fetchMedications();
  },
  methods: {
    // Fetch all medications from the API
    async fetchMedications() {
      try {
        const response = await fetch('http://localhost:8000/api/medications/');
        this.medications = await response.json();
      } catch (error) {
        console.error('Error fetching medications:', error);
      }
    },

    // Create a new medication
    async createMedication() {
      try {
        const response = await fetch('http://localhost:8000/api/medications/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newMedication),
        });
        if (response.ok) {
          const createdMedication = await response.json();
          this.medications.push(createdMedication);
          this.newMedication = { name: '', dosage: '', quantity: '', expiration_date: '' }; // Reset form
        } else {
          console.error('Error creating medication');
        }
      } catch (error) {
        console.error('Error creating medication:', error);
      }
    },

    // Edit an existing medication
    editMedication(medication) {
      this.editing = { ...medication };
    },

    // Update an existing medication
    async updateMedication() {
      try {
        const response = await fetch(`http://localhost:8000/api/medications/${this.editing.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.editing),
        });
        if (response.ok) {
          const updatedMedication = await response.json();
          const index = this.medications.findIndex(med => med.id === updatedMedication.id);
          this.$set(this.medications, index, updatedMedication);
          this.editing = null; // Close the edit form
        } else {
          console.error('Error updating medication');
        }
      } catch (error) {
        console.error('Error updating medication:', error);
      }
    },

    // Delete a medication
    async deleteMedication(id) {
      try {
        const response = await fetch(`http://localhost:8000/api/medications/${id}/`, {
          method: 'DELETE',
        });
        if (response.ok) {
          this.medications = this.medications.filter(med => med.id !== id);
        } else {
          console.error('Error deleting medication');
        }
      } catch (error) {
        console.error('Error deleting medication:', error);
      }
    }
  }
};
</script>
