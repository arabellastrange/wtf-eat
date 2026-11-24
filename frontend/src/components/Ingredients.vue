<script setup>
import { ref } from 'vue'

const ingredientInput = ref('')
const ingredients = ref([])

const emit = defineEmits(['search'])

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

function search() {
  if (ingredients.value.length > 0) {
    // Emit the search event with the ingredients array
    emit('search', ingredients.value)
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
        @keydown="handleIngredientKeydown"
        class="ingredient-input"
      />
      <!--TODO: MAX 3-4 INGREDIENTS-->
      <div class="ingredient-tags">
        <span
          v-for="(ingredient, index) in ingredients"
          :key="`${ingredient}-${index}`"
          class="tag-text"
        >
          {{ ingredient + ';' }} <!-- sanitizes input by default-->
        </span>
      </div>
    </div>
    <button type="button" class="search-button" @click="search" :disabled="ingredients.length === 0">
      Search!
    </button>
  </section>
</template>