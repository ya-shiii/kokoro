<template>
  <section class="informacion container col-12">
    <div class="row featurette">
      <div class="col-12 order-1">
        <h2 class="featurette-heading" v-html="Title"></h2>

        <img
          class="img-fluid"
          src="/img/mobile/img-2-info.png"
          alt="información 1"
        />
        <p class="lead">{{ $t("InnovationModule.body") }}</p>
        <p>
          <NuxtLink
            class="btn btn-lg btn-secondary mx-auto center-btn" :to="localePath('/productos')" 
            >{{ $t("Buttons.GoProducts") }}</NuxtLink
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
      return this.$t("InnovationModule.Title");
    },
  },
};
</script>

<style scoped="css">
@import "~/assets/css/mobile.css";
</style>