<template>
  <section class="info-contenido container col-12 section-slider seccion">
    <div class="row featurette">
      <div class="col-12 order-1 left-col"></div>
      <div class="col-12 order-1 float-text info-mobile">
        <h2 class="featurette-heading" v-html="Title"></h2>
        <img class="separador" src="/img/separador.svg" alt="separador" />
      </div>
      <div class="col-12 order-2 right-col">
        <img
          class="img-fluid"
          src="/img/mobile/img-3-info.jpg"
          alt="información 1"
        />
      </div>
    </div>
    <div class="info-text info-cont-mob">
      <img
        src="/img/mobile/top-donde-comprar.png"
        alt=""
        class="top-img img-fluid"
      />
      <div class="col-12">
        <h4 class="featurette-title">
          {{ $t("TextArticleModule.Title_small") }}
        </h4>
      </div>
      <div class="col-12">
        <p class="col-12 articulo">
          {{ $t("TextArticleModule.body_1") }}
          <NuxtLink
            class="btn btn-lg btn-secondary mx-auto mt-5 center-button-2"
            :to="localePath('/ajonegro')"
            >{{ $t("TextArticleModule.mobile_button") }}</NuxtLink
          >
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  computed: {
    Title() {
      return this.$t("TextArticleModule.Title");
    },
  },
};
</script>

<style scoped>
@import "~/assets/css/mobile.css";
</style>