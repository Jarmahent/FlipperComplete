<template>
  <div class="container py-4">
    <h2 class="mb-4 text-primary">Listings Page</h2>
    <button class="btn btn-success mb-3" @click="showModal = true">
      + Add Listing
    </button>
    <!-- Modal -->
    <div v-if="showModal" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.5);">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add New Listing</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <form @submit.prevent="submitListing">
            <div class="modal-body">
              <div class="mb-2">
                <label class="form-label">Part ID</label>
                <input v-model.number="form.part_id" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Platform</label>
                <input v-model="form.platform" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">External ID</label>
                <input v-model="form.external_id" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">URL</label>
                <input v-model="form.url" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Price ($)</label>
                <input v-model.number="form.price_c" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Fees ($)</label>
                <input v-model.number="form.fees_c" type="number" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Status</label>
                <input v-model="form.status" class="form-control" required />
              </div>
              <div class="mb-2">
                <label class="form-label">Listed Date/Time</label>
                <input v-model="form.listed_datetime" type="datetime-local" class="form-control" />
              </div>
              <div class="mb-2">
                <label class="form-label">Sold Date/Time</label>
                <input v-model="form.sold_datetime" type="datetime-local" class="form-control" />
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
      <table v-if="listings.length" class="table table-striped table-bordered align-middle">
        <thead class="table-light">
          <tr>
            <th>ID</th>
            <th>Part ID</th>
            <th>Platform</th>
            <th>External ID</th>
            <th>URL</th>
            <th>Price ($)</th>
            <th>Fees ($)</th>
            <th>Status</th>
            <th>Listed Date/Time</th>
            <th>Sold Date/Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="listing in listings" :key="listing.id">
            <td>{{ listing.id }}</td>
            <td>{{ listing.part_id }}</td>
            <td>{{ listing.platform }}</td>
            <td>{{ listing.external_id }}</td>
            <td><a :href="listing.url" target="_blank">Link</a></td>
            <td>{{ listing.price_c }}</td>
            <td>{{ listing.fees_c }}</td>
            <td>{{ listing.status }}</td>
            <td>{{ formatDateTime(listing.listed_datetime) }}</td>
            <td>{{ formatDateTime(listing.sold_datetime) }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else class="alert alert-info">No listings found.</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import superagent from 'superagent'
import { apiUrl } from '../api'

const listings = ref([])
const loading = ref(true)
const showModal = ref(false)
const form = ref({
  part_id: '',
  platform: 'EBAY',
  external_id: '',
  url: '',
  price_c: '',
  fees_c: '',
  status: 'DRAFT',
  listed_datetime: '',
  sold_datetime: ''
})

function closeModal() {
  showModal.value = false
  Object.assign(form.value, {
    part_id: '', platform: 'EBAY', external_id: '', url: '', price_c: '', fees_c: '', status: 'DRAFT', listed_datetime: '', sold_datetime: ''
  })
}

async function submitListing() {
  try {
    const payload = { ...form.value }
    // Convert datetimes to ISO string if not empty
    if (payload.listed_datetime) {
      payload.listed_datetime = new Date(payload.listed_datetime).toISOString()
    }
    if (payload.sold_datetime) {
      payload.sold_datetime = new Date(payload.sold_datetime).toISOString()
    }
    await superagent.post(apiUrl('/listings/v1')).send(payload)
    // Refresh list
    await fetchListings()
    closeModal()
  } catch (err) {
    alert('Failed to add listing.')
  }
}

async function fetchListings() {
  loading.value = true
  try {
    const res = await superagent.get(apiUrl('/listings/v1'))
    listings.value = Array.isArray(res.body) ? res.body : []
  } catch (err) {
    listings.value = []
  } finally {
    loading.value = false
  }
}

onMounted(fetchListings)

function formatDateTime(dateStr) {
  if (!dateStr) return ''
  return new Date(dateStr).toLocaleString()
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
