<template>
  <div class="row featurette">
    <div class="col-12 order-1 left-col"></div>
    <div class="col-12 order-3 float-text">
      <h2 class="featurette-heading" v-html="title"></h2>
      <img class="separador" src="/img/separador.svg" alt="separador" />
    </div>
  </div>
</template>


<script>
export default {
  props: {
    title: String,
  },
};
</script>

<style scoped>
@import "~/assets/css/mobile.css";
</style>