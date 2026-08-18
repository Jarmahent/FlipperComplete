<template>
  <div class="container py-5 my-5" style="font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;">
    <h1 class="mb-4 text-primary">List Part for Sale</h1>
    <div v-if="step === 1" class="card p-4 mb-4">
      <h3 class="mb-3">Step 1: Choose Platform</h3>
      <div class="d-flex flex-column gap-3">
        <button class="btn btn-outline-primary" @click="selectPlatform('EBAY')">eBay</button>
        <button class="btn btn-outline-info" @click="selectPlatform('FACEBOOK')">Facebook Marketplace</button>
        <button class="btn btn-outline-secondary" @click="selectPlatform('CRAIGSLIST')">Craigslist</button>
      </div>
    </div>
    <div v-else-if="step === 2" class="card p-4 mb-4">
      <h3 class="mb-3">Step 2: Enter Listing Details</h3>
      <form @submit.prevent="submitListing">
        <div class="mb-3">
          <label class="form-label">External ID</label>
          <input v-model="form.external_id" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Listing URL</label>
          <input v-model="form.url" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Price ($)</label>
          <input v-model.number="form.price_c" type="number" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Fees ($)</label>
          <input v-model.number="form.fees_c" type="number" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Status</label>
          <input v-model="form.status" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Listed Date/Time</label>
          <input v-model="form.listed_datetime" type="datetime-local" class="form-control" />
        </div>
        <div class="mb-3">
          <label class="form-label">Sold Date/Time (optional)</label>
          <input v-model="form.sold_datetime" type="datetime-local" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit Listing</button>
        <button type="button" class="btn btn-link ms-2" @click="step = 1">Back</button>
      </form>
    </div>
    <div v-else-if="step === 3" class="card p-4 mb-4 text-center">
      <h3 class="mb-3">Listing Submitted!</h3>
      <p>Your part has been submitted for listing on <b>{{ platformLabel() }}</b>.</p>
      <button class="btn btn-secondary mt-2" @click="reset">List Another Part</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import superagent from 'superagent'
import { apiUrl } from '../api'
import { useRoute } from 'vue-router'

const step = ref(1)
const platform = ref('')
const route = useRoute()
const form = ref({
  external_id: '',
  url: '',
  price_c: '',
  fees_c: '',
  status: 'DRAFT',
  listed_datetime: '',
  sold_datetime: ''
})

function selectPlatform(p) {
  platform.value = p
  step.value = 2
}

function platformLabel() {
  if (platform.value === 'EBAY') return 'EBAY'
  if (platform.value === 'FACEBOOK') return 'FACEBOOK'
  if (platform.value === 'CRAIGSLIST') return 'CRAIGSLIST'
  return ''
}

async function submitListing() {
  try {
    const part_id = route.query.part_id ? Number(route.query.part_id) : null
    if (!part_id) return alert('No part selected!')
    const payload = {
      part_id,
      platform: platform.value,
      ...form.value,
      listed_datetime: form.value.listed_datetime ? new Date(form.value.listed_datetime).toISOString() : null,
      sold_datetime: form.value.sold_datetime ? new Date(form.value.sold_datetime).toISOString() : null
    }
    await superagent.post(apiUrl('/listings/v1')).send(payload)
    step.value = 3
  } catch (err) {
    alert('Failed to submit listing (placeholder).')
  }
}

function reset() {
  step.value = 1
  platform.value = ''
  Object.assign(form.value, {
    external_id: '', url: '', price_c: '', fees_c: '', status: 'DRAFT', listed_datetime: '', sold_datetime: ''
  })
}
</script>

<style scoped>
.card {
  max-width: 500px;
  margin: 0 auto;
}
</style>