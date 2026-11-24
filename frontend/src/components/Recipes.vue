<script setup>
import { ref } from 'vue'

defineProps({
  recipes: { type: Array, default: () => [] },
  ingredients: { type: Array, default: () => [] }
})

function parseArray(value) {
    // TODO drop c with c( but not all c in  string
  return value.split(',').map(ingredient => ingredient.replaceAll(/["()]/gm, '').trim())
}

</script>

<template>
    <section class="search-results">
        <h3>Recipes found for {{ ingredients.join(', ') }}</h3>
        <div class="recipe-cards">
            <template v-for="recipe in recipes">
            <div class="recipe-card">
                <h4>{{ recipe.Name }}</h4>
                <span class="tag-text">tagged: {{ parseArray(recipe.Keywords) }}</span>
                <ul>
                    <li v-for="ingredient in parseArray(recipe.RecipeIngredientParts)">
                        {{ ingredient }}
                    </li>
                </ul>
            </div>
        </template>
        </div>
        
    </section>
</template>