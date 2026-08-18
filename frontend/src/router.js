import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'Home', component: () => import('./views/Home.vue') },
  { path: '/vehicles', name: 'Vehicles', component: () => import('./views/Vehicles.vue') },
  { path: '/parts', name: 'Parts', component: () => import('./views/Parts.vue') },
  { path: '/view-listing', name: 'ViewListing', component: () => import('./views/ViewListing.vue') },
  { path: '/listing', name: 'Listing', component: () => import('./views/Listing.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
