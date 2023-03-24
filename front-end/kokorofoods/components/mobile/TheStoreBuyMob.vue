<template>
  <section class="container col-12 section-slider" :class="class_section">
    <div class="row featurette">
      <img
        src="img/mobile/top-donde-comprar-2.jpg"
        alt=""
        class="top-img-secc"
      />
      <div class="col-12 order-3 float-text-comprar">
        <h2 class="featurette-heading" v-html="title"></h2>
        <img class="separador" src="/img/separador.svg" alt="separador" />
        <p>
          <NuxtLink
            class="btn btn-lg btn-primary"
            :to="localePath(Button_link)"
            >{{ Button_text }}</NuxtLink
          >
        </p>
      </div>
      <div class="col-12 order-2 right-col">
        <img class="img-fluid" :src="Image_URL_mob" alt="información 1" />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    title: String,
    Button_text: String,
    Image_URL_mob: String,
    Button_link: String,
    class_section: String,
  },
};
</script>

<style scoped>
@import "~/assets/css/mobile.css";
</style>