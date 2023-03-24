<template>
  <section class="productos container-fluid col-sm-12 section">
    <div class="row featurette">
      <div class="col-12">
        <h2 class="featurette-heading" v-html="Title"></h2>
        <img
          class="img-fluid"
          src="img/mobile/img-1-info.png"
          alt="producto 1"
        />

        <p class="lead">{{ $t("ProductModule.body") }}</p>
        <p>
          <NuxtLink
            class="btn btn-lg btn-secondary mx-auto center-btn"
            :to="localePath('/productos')"
            >{{ $t("Buttons.buy") }}</NuxtLink
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
      return this.$t("ProductModule.Title");
    },
  },
};
</script>

<style scope="css">
@import "~/assets/css/mobile.css";
img.img-fluid.separador {
  padding-bottom: 35px;
}
.center-btn {
  width: 200px;
  display: block !important;
  margin-bottom: 25px;
  margin-top: 25px;
  margin: 25px auto;
}
.container-fluid {
  margin: 0;
  padding: 0;
}
.featurette-heading {
  margin-top: 0 !important;
  color: #000 !important;
  font-weight: bold !important;
  font-size: 2.5em !important;
}
.featurette-heading-light {
  margin-top: 0 !important;
  color: #fff !important;
  font-weight: bold !important;
  font-size: 2.5em !important;
}
.featurette-heading-light .text-muted {
  margin-top: 0 !important;
  color: #fff !important;
  font-weight: bold !important;
  /* font-size: 2.5em !important; */
}
.float-text-comprar .featurette-heading {
  margin-top: 0 !important;
  color: #fff !important;
  font-weight: bold !important;
  /* font-size: 2.5em !important; */
}
.float-text-comprar .featurette-heading .text-muted {
  margin-top: 0 !important;
  color: #fff !important;
  font-weight: 500 !important;
  /* font-size: 2.5em !important; */
}
.float-text-comprar .separador {
  filter: invert(1);
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
  /* padding-left: 80px !important;
    padding-right: 80px !important; */
}
.section {
  padding-top: 50px;
  padding-bottom: 50px;
  padding-left: 15px;
  padding-right: 15px;
}
</style>