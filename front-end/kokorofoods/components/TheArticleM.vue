<template>
  <section class="informacion container col-md-12">
    <div class="row featurette">
      <div class="col-3 order-md-1">
        <h2 class="featurette-heading" v-html="Title"></h2>
        <img
          class="img-fluid separador"
          src="img/separador.svg"
          alt="separador"
        />
        <p>
          <NuxtLink class="btn btn-lg btn-primary" :to="localePath('/productos')">{{
            $t("Buttons.GoProducts")
          }}</NuxtLink>
        </p>
      </div>
      <div class="col-9 order-md-2">
        <img class="img-fluid" src="img/img-info-1.jpg" alt="información 1" />
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
.informacion {
  background-color: #f4f5e6;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
</style>