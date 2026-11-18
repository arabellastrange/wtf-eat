<script setup>
import { ref } from 'vue'
defineProps({
  recipes: { type: Array, default: () => [] },
  ingredients: { type: Array, default: () => [] }
})

</script>

<template>
    <section class="search-results">
        <h3>Recipes found for {{ ingredients.join(', ') }}</h3>
        <p v-for="recipe in recipes" :key="recipe.Name">
            {{ recipe.Name }}
        </p>
    </section>
</template>