<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Snake></Snake>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Snake from '@/components/Snake.vue';

@Component({
  components: {
   Snake
  },
})
export default class HomeView extends Vue {}
</script>
