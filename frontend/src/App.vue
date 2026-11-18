<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Ingredients from './components/Ingredients.vue'
import Recipes from './components/Recipes.vue'

const ingredientsSearched = ref([])
const recipes = ref([])
const hasSearched = ref(false)

function handleSearch(ingredients) {
  ingredientsSearched.value = ingredients
  

  axios.get('/api/recipes/', {
    params: {
      ingredients: ingredientsSearched.value.join(',')
    }
  }).then(response => {
        console.log(response.data);
        recipes.value = [...recipes.value, ...response.data]; // response.data must be an array of recipes
        hasSearched.value = true;
        // do something with response.data
      })
      .catch(error => {
        console.error(error);
      });
}
</script>

<template>
  <Ingredients
    v-if="!hasSearched" 
    @search="handleSearch" 
  />

  <Recipes
    v-else 
    :recipes="recipes" 
    :ingredients="ingredientsSearched"
    @back="hasSearched = false" 
  />
</template>
