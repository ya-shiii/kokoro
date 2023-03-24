<template>
  <section class="productos-dest container col-12">
    <div class="row featurette">
      <div class="col-12 order-1">
        <h2 class="featurette-heading" v-html="ModuleName"></h2>
        <img class="separador" src="/img/separador.svg" alt="separador" />
        <div v-html="CTA_text"></div>
      </div>
      <div class="col-12 order-2 row">
        <!-- articulo 1  -->
        <div
          class="col-12 articulo row"
          v-for="producto in MasDestacado.slice(0, 1)"
          :key="producto.id"
          :class="{ 's-stock': producto.quantity < 1 }"
        >
        <div class="sin-stock col-5" v-if="producto.quantity < 1">{{ $t('Tag.Nostock')}}</div>
          <div class="order-1 col-12">
            <img
              class="img-fluid"
              :src="Img_product(producto.product_images)"
              :alt="producto.name"
            />
          </div>
          <div class="datos-art-dest order-2 col-12 row">
            <div class="col-6 left-it">
              <p>{{ producto.name }}</p>
              <p class="articulo-des" v-html="producto.short_description">
               
              </p>
            </div>
            <div class="col-6">
              <div class="precio-dest">
                <div class="precio-oferta col-6">
                  <h3>${{ producto.price }}</h3>
                </div>
                <div
                  class="precio-normal col-6"
                  v-if="producto.precio_comparacion != 0"
                >
                  <p>
                    antes<br /><span>${{ producto.precio_comparacion }}</span>
                  </p>
                </div>
              </div>
              <p v-if="producto.quantity > 0">
                <NuxtLink
                  class="btn btn-lg btn-secondary"
                  :to="localePath('/productos/' + producto.id)"
                  >{{ $t("Buttons.buy") }}</NuxtLink
                >
              </p>
               <p v-if="producto.quantity < 1"><NuxtLink class="btn btn-lg btn-secondary disabled" :to="localePath('/productos/'+ producto.id)" aria-disabled="true">{{ $t('Buttons.OutStock')}}</NuxtLink></p>
            </div>
          </div>
        </div>

        <!-- articulo 4 sin stock -->
        <div class="col-12 articulo row">
          <div
            class="col-6"
            v-for="producto in MasDestacado.slice(1, 3)"
            :key="producto.id"
            :class="{ 's-stock': producto.quantity < 1 }"
          >
            <div class="sin-stock col-5" v-if="producto.quantity < 1">{{ $t('Tag.Nostock')}}</div>
            <div class="articulo col-12">
              <img
                class="img-fluid"
                :src="Img_product(producto.product_images)"
                :alt="producto.name"
              />
            </div>
            <div class="datos-art-dest col-12 row">
              <div class="col-12 articulo">
                <p class="n-articulo">{{ producto.name }}</p>
                <div class="precio-dest row">
                  <div
                    class="precio-normal col-6"
                    v-if="producto.precio_comparacion != 0"
                  >
                    <p>
                      <span>${{ producto.precio_comparacion }}</span>
                    </p>
                  </div>
                  <div class="precio-oferta col-6">
                    <p>
                      <span>${{ producto.price }}</span>
                    </p>
                  </div>
                </div>
                <p v-if="producto.quantity > 0">
                  <NuxtLink
                    class="btn btn-lg btn-secondary"
                    :to="localePath('/productos/' + producto.id)"
                    >{{ $t("Buttons.buy") }}</NuxtLink>
                </p>
                <p v-if="producto.quantity < 1"><NuxtLink class="btn btn-lg btn-secondary disabled" :to="localePath('/productos/'+ producto.id)" aria-disabled="true">{{ $t('Buttons.OutStock')}}</NuxtLink></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  props: {
    MasDestacado: Array,
    CTA_text: String,
    ModuleName: String,
    ButtonON: Boolean,
  },
  data() {
    return {
      sendrow: false,
    };
  },
  methods: {
    Img_product(images) {
      for (var i = 0; i < images.length; i++) {
        if (images[i].type == "front_mobile") {
          var url = images[i].image_url;
        }
      }
      return url;
    },
  },
};
</script>

<style scoped>
@import "~/assets/css/mobile.css";
</style>