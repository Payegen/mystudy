<template>
  <div class="about">
    <h1>贪吃蛇</h1>
    <Snake></Snake>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Snake from '../components/Snake.vue';

@Component({
  components: {
   Snake
  },
})
export default class HomeView extends Vue {}
</script>