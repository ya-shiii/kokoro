<template>
  <section class="container col-md-12 section" :class="class_section">
    <div class="row featurette">
      <div class="col-md-3 order-md-1 left-col"></div>
      <div class="col-md-3 order-md-3 float-text-comprar">
        <h2 class="featurette-heading" v-html="title"></h2>
        <img
          class="img-fluid separador"
          src="img/separador.svg"
          alt="separador"
        />
        <p>
          <NuxtLink class="btn btn-lg btn-primary" :to="localePath(Button_link)">{{
            Button_text
          }}</NuxtLink>
        </p>
      </div>
      <div class="col-md-9 order-md-2 right-col">
        <img class="img-fluid" :src="Image_URL" alt="información 1" />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    title: String,
    Button_text: String,
    Image_URL: String,
    Button_link: String,
    class_section: String,
  },
};
</script>

<style scoped>
.donde-comprar {
  background-color: #f6f0ee;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
.float-text-comprar {
  position: absolute !important;
  z-index: 10;
  background-color: #f4f5e6;
  padding: 30px 5px 20px 5px;
  left: 150px;
}
</style>