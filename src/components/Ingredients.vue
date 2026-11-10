<script setup>
import { ref } from 'vue'

</script>

<template>
  <section class="search-splash">
    <div>
      <h1>What Should I Eat For Dinner?</h1>
      <input type="text" placeholder="Enter an ingredient" />
    </div>
    <button type="button" class="search-button" @click="">
      Search!
    </button>
  </section>
</template>