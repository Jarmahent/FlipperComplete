<template>
  <div class="container py-4">
    <h2 class="mb-4 text-primary">Parts Page</h2>
    <button class="btn btn-secondary mb-3" @click="goBackToVehicle">
      ← Back to Vehicle
    </button>
    <button class="btn btn-success mb-3 ms-2" @click="showModal = true">
      + Add Part
    </button>
    <!-- Modal -->
    <div v-if="showModal" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.5);">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add New Part</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <form @submit.prevent="submitPart">
            <div class="modal-body">
              <div class="mb-2">
                <label class="form-label">Name</label>
                <input v-model="form.name" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">OEM Number</label>
                <input v-model="form.oem_number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Vehicle ID</label>
                <input v-model.number="form.vehicle_id" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Condition Note</label>
                <input v-model="form.condition_note" class="form-control" />
              </div>
              <div class="mb-2">
                <label class="form-label">Locker</label>
                <input v-model="form.loc_locker" class="form-control" />
              </div>
              <div class="mb-2">
                <label class="form-label">Bin</label>
                <input v-model="form.loc_bin" class="form-control" />
              </div>
              <div class="mb-2">
                <label class="form-label">Est. Value ($)</label>
                <input v-model.number="form.est_value_c" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Status</label>
                <input v-model="form.status" class="form-control" required />
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
      <table v-if="parts.length" class="table table-striped table-bordered align-middle">
        <thead class="table-light">
          <tr>
            <th>ID</th>
            <th>Vehicle ID</th>
            <th>Name</th>
            <th>OEM Number</th>
            <th>Condition Note</th>
            <th>Locker</th>
            <th>Bin</th>
            <th>Est. Value ($)</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="part in parts" :key="part.id">
            <td>{{ part.id }}</td>
            <td>{{ part.vehicle_id }}</td>
            <td>{{ part.name }}</td>
            <td>{{ part.oem_number }}</td>
            <td>{{ part.condition_note }}</td>
            <td>{{ part.loc_locker }}</td>
            <td>{{ part.loc_bin }}</td>
            <td>{{ part.est_value_c }}</td>
            <td>{{ part.status }}</td>
            <td>
              <button class="btn btn-outline-warning btn-sm" @click="goToListItem(part)">List Item</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-else class="alert alert-info">No parts found for this vehicle.</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import superagent from 'superagent'
import { apiUrl } from '../api'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const parts = ref([])
const loading = ref(true)
const showModal = ref(false)
const form = ref({
  vehicle_id: route.query.vehicle_id ? Number(route.query.vehicle_id) : '',
  name: '',
  oem_number: '',
  condition_note: '',
  loc_locker: '',
  loc_bin: '',
  est_value_c: '',
  status: 'IN_BIN'
})

function closeModal() {
  showModal.value = false
  Object.assign(form.value, {
    vehicle_id: route.query.vehicle_id ? Number(route.query.vehicle_id) : '', name: '', oem_number: '', condition_note: '', loc_locker: '', loc_bin: '', est_value_c: '', status: 'IN_BIN'
  })
}

async function submitPart() {
  try {
    const vehicleId = route.query.vehicle_id ? Number(route.query.vehicle_id) : Number(form.value.vehicle_id)
    if (!vehicleId) return alert('No vehicle selected!')
    const payload = { ...form.value, vehicle_id: vehicleId }
    await superagent.post(apiUrl('/parts/v1')).send(payload)
    await fetchParts()
    closeModal()
  } catch (err) {
    alert('Failed to add part.')
  }
}

async function fetchParts() {
  loading.value = true
  try {
    const vehicleId = route.query.vehicle_id
    let url = apiUrl('/parts/v1')
    if (vehicleId) {
      const res = await superagent.get(`${url}?vehicle_id=${vehicleId}`)
      parts.value = Array.isArray(res.body) ? res.body : []
    } else {
      const res = await superagent.get(url)
      parts.value = Array.isArray(res.body) ? res.body : []
    }
  } catch (err) {
    parts.value = []
  } finally {
    loading.value = false
  }
}

function goBackToVehicle() {
  router.push('/vehicles')
}

function goToListItem(part) {
  router.push({ path: '/listing', query: { part_id: part.id } })
}

onMounted(fetchParts)
</script>

<style scoped>
.modal {
  display: block;
}
.table {
  background: #fff;
}
</style>
