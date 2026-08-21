<template>
  <svg class="app-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path v-for="(path, index) in paths[name] || paths.box" :key="index" :d="path" />
  </svg>
</template>

<script setup>
defineProps({ name: { type: String, default: 'box' } })

const paths = {
  dashboard: ['M3 13h8V3H3z', 'M13 21h8V11h-8z', 'M13 3h8v6h-8z', 'M3 15h8v6H3z'],
  car: ['M5 17H3v-5l2-5h14l2 5v5h-2', 'M5 17h14v-5H5z', 'M7 17v2', 'M17 17v2', 'M7 13h.01', 'M17 13h.01'],
  box: ['M21 8l-9 5-9-5', 'M3 8l9-5 9 5v8l-9 5-9-5z', 'M12 13v8'],
  tag: ['M20 13l-7 7-9-9V4h7z', 'M8.5 8.5h.01'],
  plus: ['M12 5v14', 'M5 12h14'],
  sun: ['M12 2v2', 'M12 20v2', 'M4.93 4.93l1.42 1.42', 'M17.66 17.66l1.41 1.41', 'M2 12h2', 'M20 12h2', 'M4.93 19.07l1.42-1.42', 'M17.66 6.34l1.41-1.41', 'M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0'],
  moon: ['M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z'],
  arrow: ['M5 12h14', 'M13 6l6 6-6 6'],
  back: ['M19 12H5', 'M11 18l-6-6 6-6'],
  external: ['M14 3h7v7', 'M10 14L21 3', 'M21 14v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5'],
  close: ['M18 6L6 18', 'M6 6l12 12'],
  check: ['M20 6L9 17l-5-5'],
  search: ['M21 21l-4.35-4.35', 'M19 11a8 8 0 1 1-16 0 8 8 0 0 1 16 0'],
  menu: ['M4 6h16', 'M4 12h16', 'M4 18h16']
}
</script>
