<template>
  <div class="container py-4">
    <h2 class="mb-4 text-primary">Vehicles Page</h2>
    <button class="btn btn-success mb-3" @click="showModal = true">
      + Add Vehicle
    </button>
    <!-- Modal -->
    <div v-if="showModal" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.5);">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add New Vehicle</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <form @submit.prevent="submitVehicle">
            <div class="modal-body">
              <div class="mb-2">
                <label class="form-label">Make</label>
                <input v-model="form.make" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Model</label>
                <input v-model="form.model" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Year</label>
                <input v-model.number="form.year" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">VIN</label>
                <input v-model="form.vin" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Purchase Price ($)</label>
                <input v-model.number="form.purchase_price_c" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Auction Fee ($)</label>
                <input v-model.number="form.auction_fee_c" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Status</label>
                <input v-model="form.status" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Purchase Date</label>
                <input v-model="form.purchase_date" type="date" class="form-control" required />
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="closeModal">Cancel</button>
              <button type="submit" class="btn btn-primary">Save</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div v-if="loading" class="text-center my-4">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <div v-else>
      <table v-if="vehicles.length" class="table table-striped table-bordered align-middle">
        <thead class="table-light">
          <tr>
            <th>ID</th>
            <th>Make</th>
            <th>Model</th>
            <th>Year</th>
            <th>VIN</th>
            <th>Purchase Price ($)</th>
            <th>Auction Fee ($)</th>
            <th>Status</th>
            <th>Purchase Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="vehicle in vehicles" :key="vehicle.id">
            <td>{{ vehicle.id }}</td>
            <td>{{ vehicle.make }}</td>
            <td>{{ vehicle.model }}</td>
            <td>{{ vehicle.year }}</td>
            <td>{{ vehicle.vin }}</td>
            <td>{{ vehicle.purchase_price_c }}</td>
            <td>{{ vehicle.auction_fee_c }}</td>
            <td>{{ vehicle.status }}</td>
            <td>{{ formatDate(vehicle.purchase_date) }}</td>
            <td>
              <button class="btn btn-outline-primary btn-sm" @click="goToParts(vehicle)">Parts</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-else class="alert alert-info">No vehicles found.</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import superagent from 'superagent'
import { apiUrl } from '../api'
import { useRouter } from 'vue-router'

const router = useRouter()
const vehicles = ref([])
const loading = ref(true)
const showModal = ref(false)
const form = ref({
  make: '',
  model: '',
  year: '',
  vin: '',
  purchase_price_c: '',
  auction_fee_c: '',
  status: 'PURCHASED',
  purchase_date: ''
})

function closeModal() {
  showModal.value = false
  Object.assign(form.value, {
    make: '', model: '', year: '', vin: '', purchase_price_c: '', auction_fee_c: '', status: 'PURCHASED', purchase_date: ''
  })
}

async function submitVehicle() {
  try {
    const payload = { ...form.value }
    // Convert date to ISO string if not empty
    if (payload.purchase_date) {
      payload.purchase_date = new Date(payload.purchase_date).toISOString()
    }
    await superagent.post(apiUrl('/vehicles/v1')).send(payload)
    // Refresh list
    await fetchVehicles()
    closeModal()
  } catch (err) {
    alert('Failed to add vehicle.')
  }
}

async function fetchVehicles() {
  loading.value = true
  try {
    const res = await superagent.get(apiUrl('/vehicles/v1'))
    vehicles.value = Array.isArray(res.body) ? res.body : []
  } catch (err) {
    vehicles.value = []
  } finally {
    loading.value = false
  }
}

onMounted(fetchVehicles)

function formatDate(dateStr) {
  if (!dateStr) return ''
  return new Date(dateStr).toLocaleDateString()
}

function goToParts(vehicle) {
  router.push({ path: '/parts', query: { vehicle_id: vehicle.id } })
}
</script>

<style scoped>
.modal {
  display: block;
}
.table {
  background: #fff;
}
</style>
