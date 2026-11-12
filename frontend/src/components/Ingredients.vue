<script setup>
import { ref } from 'vue'
import axios from 'axios'

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

function handleSearch() {
  if (ingredients.value.length > 0) {
    axios.get('/api/recipes/', {
      params: {
        ingredients: ingredients.value.join(',')
      }
    }).then(response => {
          console.log(response.data);
          // do something with response.data
        })
        .catch(error => {
          console.error(error);
        });
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
      <!--TODO: MAX 3-4 INGREDIENTS-->
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
    <button type="button" class="search-button" @click="handleSearch">
      Search!
    </button>
  </section>
</template>