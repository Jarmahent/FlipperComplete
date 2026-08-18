<template>
    <div class="hello">
        <input v-model="msg" placeholder="Enter a message" />
        <p>{{ msg }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('')
</script>

<style scoped>
.hello {
    font-size: 1.2rem;
}
</style>