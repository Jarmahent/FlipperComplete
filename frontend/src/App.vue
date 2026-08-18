<template>
  <div id="app" class="container py-5 my-5" style="font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;">
    <h1 class="mb-4 text-primary" style="cursor:pointer" @click="$router.push('/')">Flipper (Prototype) </h1>
    <p class="mb-4 text-primary">By Kevin </p>
    <div v-if="$route.path === '/'" class="landing-options card shadow-sm p-4">
      <ul class="list-group">
        <router-link to="/vehicles" class="text-decoration-none" custom v-slot="{ navigate, href, isActive, isExactActive }">
          <li class="list-group-item list-group-item-action" :class="{ active: isActive }" @click="navigate" role="button" tabindex="0">
            View Vehicles
          </li>
        </router-link>
        <router-link to="/parts" class="text-decoration-none" custom v-slot="{ navigate, href, isActive, isExactActive }">
          <li class="list-group-item list-group-item-action" :class="{ active: isActive }" @click="navigate" role="button" tabindex="0">
            View Parts Inventory
          </li>
        </router-link>
        <router-link to="/view-listing" class="text-decoration-none" custom v-slot="{ navigate, href, isActive, isExactActive }">
          <li class="list-group-item list-group-item-action" :class="{ active: isActive }" @click="navigate" role="button" tabindex="0">
            View Listings
          </li>
        </router-link>
      </ul>
    </div>
    <router-view v-else />
  </div>
</template>

<script setup>
</script>

<style scoped>
h1 {
  color: #0d6efd;
  font-weight: 700;
  cursor: pointer;
}
.landing-options {
  max-width: 400px;
  margin: 2rem auto;
  text-align: center;
  background: #fff;
  border-radius: 1rem;
}
.list-group-item {
  font-size: 1.2rem;
  cursor: pointer;
  transition: background 0.2s;
}
.list-group-item:hover {
  background: #f0f8ff;
}
</style>