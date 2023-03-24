<template>
  <section class="productos-mas container col-md-12">
    <div class="row featurette">
      <div class="col-md-3 order-md-1">
        <h2 class="featurette-heading" v-html="Title"></h2>
        <img
          class="img-fluid separador"
          src="/img/separador.svg"
          alt="separador"
        />
        <p>
          <NuxtLink
            class="btn btn-lg btn-primary"
            :to="localePath('/productos')"
            >{{ $t("Buttons.GoProducts") }}</NuxtLink
          >
        </p>
      </div>
      <div class="col-md-9 order-md-2 row">
        <!-- articulo 1  -->
        <div
          class="col-md-6 articulo"
          v-for="(producto, index) in MasVendidos.slice(0, 4)"
          :key="producto.id"
          :class="{
            'seg-row': checkrow(index),
            's-stock': producto.quantity < 1,
          }"
        >
        <div class="sin-stock col-md-4" v-if="producto.quantity < 1">{{ $t('Tag.Nostock')}}</div>
          <div class="datos-art">
            <h1 class="n-articulo" v-html="titleFormat(producto.name)"></h1>
            <h4 class="precio">
              <strong>
                   {{ $n(producto.price, "currency") }}
               </strong>
            </h4>
            <p v-if="producto.quantity > 0">
              <NuxtLink
                class="btn btn-lg btn-secondary"
                :to="localePath('/productos/' + producto.id)"
              >
                {{ $t("Buttons.buy") }}
              </NuxtLink>
            </p>
             <p v-if="producto.quantity < 1"><NuxtLink class="btn btn-lg btn-secondary disabled" :to="localePath('/productos/'+ producto.id)" aria-disabled="true">{{ $t('Buttons.OutStock')}}</NuxtLink></p>
          </div>
          <div class="">
            <img
              class="img-fluid"
              :src="Img_product(producto.product_images)"
              :alt="producto.name"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  data() {
    return {
      sendrow: false,
    };
  },
  props: {
    MasVendidos: Array,
  },
  methods: {
    checkrow: function (index) {
      if (index > 1) {
        this.sendrow = true;
      }
    },
    titleFormat(name) {
      var short = name.toString().split(" ");
      var title = "";
      var secondPart = "";
      for (var index = 0; index < 4; index++) {
        title += short[index] + " ";
      }
      title += "<br>";
      for (var index = 4; index < short.length; index++) {
        secondPart += short[index] + " ";
      }
      title += '<span class="pero-art">' + secondPart + "</span>";
      return title;
    },
    Img_product(images) {
      for (var i = 0; i < images.length; i++) {
        if (images[i].type == "front") {
          var url = images[i].image_url;
        }
      }
      return url;
    },
  },
  computed: {
    Title() {
      return this.$t("TheMostSalesModule.Title");
    },
  },
};
</script>
<style scoped>
.productos-mas {
  background-color: #fff;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
.seg-row {
  color: #fff;
}
img.img-fluid.separador {
  padding-bottom: 35px;
}
.articulo-des {
  font-weight: 300 !important;
}
.articulo {
  padding: 10px !important;
  margin: 0 !important;
}
.left-it {
  border-right: 1px solid #000;
  padding: 0 15px 0 0 !important;
}
.datos-art {
  position: absolute;
  padding: 20px 0 0 20px;
}
.datos-art a {
  text-transform: uppercase;
  position: relative;
  top: 50px;
  left: -20px;
  font-size: 0.8em;
}
.precio strong {
  color: #000;
}
.seg-row > .datos-art > .precio strong {
  color: #fff;
}
.seg-row > .datos-art > .n-articulo {
  font-size: 1.1rem !important;
  color: #fff;
}
.seg-row > .datos-art > .n-articulo span {
  font-size: 1.1rem !important;
  color: #fff;
  font-weight: 200;
}
.n-articulo {
  font-size: 1.1rem !important;
  color: #000;
}
.n-articulo span {
  font-size: 1.1rem !important;
  color: #000;
  font-weight: 200;
}
.sin-stock {
    background-color: #fff;
    position: absolute !important;
    text-align: center;
    right: 15px;
    color: #000;
    z-index: 10;
    top: 20px;
}
</style>