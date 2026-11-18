<script setup>
import { ref } from 'vue'

</script>

<template>
    <section class="search-results">
        <child v-bind:results_from_parent="recipes"></child>
    </section>
</template>