<template>
  <section class="productos container col-md-12">
    <div class="row featurette">
      <div class="col-3 order-md-2">
        <h2 class="featurette-heading" v-html="Title"></h2>
        <img
          class="img-fluid separador"
          src="/img/separador.svg"
          alt="separador"
        />
        <div class="precio row">
          <h3 class="precio-oferta">$10.000</h3>
          <div class="precio-normal"></div>
        </div>

        <p class="lead">{{ $t("ProductModule.body") }}</p>
        <p>
          <NuxtLink
            class="btn btn-lg btn-primary"
            :to="localePath('/productos/3')">
            {{ $t("Buttons.buy") }}
          </NuxtLink>
        </p>
      </div>
      <div class="col-9 order-md-1">
        <img class="img-fluid" src="/img/pasta_home.png" alt="producto 1" />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  computed: {
    Title() {
      return this.$t("ProductModule.Title");
    },
  },
  props: {
    MasVendidos: Array,
  },
};
</script>

<style scoped>
img.img-fluid.separador {
  padding-bottom: 35px;
}
.featurette-heading {
  margin-top: 0 !important;
  color: #000 !important;
  font-weight: bold !important;
  font-size: 2.5em !important;
}
.featurette-heading span {
  font-weight: normal !important;
  color: #000 !important;
}
h4.featurette-title {
  color: #000;
  font-weight: 400;
}
.info-text p {
  color: #000;
  font-weight: 400;
}
.productos {
  background-color: #f4f5e6;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
</style>