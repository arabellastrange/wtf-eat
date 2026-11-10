<script setup>
import { ref } from 'vue'

const ingredientInput = ref('')
const ingredients = ref([])

function addIngredient() {
  const ingredient = ingredientInput.value.trim()

  if (!ingredient) {
    ingredientInput.value = ''
    return
  }

  ingredients.value.push(ingredient)
  ingredientInput.value = ''
}

function handleIngredientKeydown(event) {
  if (['Enter', ',', ' '].includes(event.key)) {
    event.preventDefault()
    addIngredient()
  }
}
</script>

<template>
  <section class="search-splash">
    <div>
      <h1>What Should I Eat For Dinner?</h1>
      <input
        v-model="ingredientInput"
        type="text"
        placeholder="Add an ingredient"
        aria-label="Add an ingredient"
        @keydown="handleIngredientKeydown"
        class="ingredient-input"
      />
      <div class="ingredient-tags" aria-label="Ingredients" aria-live="polite">
        <span
          v-for="(ingredient, index) in ingredients"
          :key="`${ingredient}-${index}`"
          class="ingredient-tag"
        >
          {{ ingredient + ';' }} <!-- sanitizes input by default-->
        </span>
      </div>
    </div>
    <button type="button" class="search-button" @click="">
      Search!
    </button>
  </section>
</template>