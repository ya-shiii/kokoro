<template>
    <section class="productos-dest container col-md-12">
        <div class="row featurette">
        <div class="col-md-3 order-md-1">
            <h2 class="featurette-heading" v-html="ModuleName"></h2>
            <img class="img-fluid separador" src="img/separador.svg" alt="separador">
            <p v-if="ButtonON"><NuxtLink class="btn btn-lg btn-primary" :to="localePath('/productos')">{{ $t('Buttons.GoProducts')}}</NuxtLink></p>
            <p v-else v-html="CTA_text"></p>
        </div>
        <div class="col-md-9 order-md-2 row">
            <!-- articulo 1  -->
            <div class="col-md-6 articulo row" v-for="(producto) in MasDestacado.slice(0,2)" :key="producto.id" :class="{'s-stock': (producto.quantity < 1)}">
              <div class="sin-stock col-md-4" v-if="producto.quantity < 1">{{ $t('Tag.Nostock')}}</div>
                <div class="datos-art-dest order-md-2 col-md-12 row">
                    <div class="col-md-6 left-it">
                        <div class="precio-dest row">
                            <div class="precio-oferta col-md-6">
                                <h3>{{$n(producto.price, 'currency')}}</h3>
                            </div>    
                            <div class="precio-normal col-md-6" v-if="(producto.precio_comparacion != 0)">
                                <p>antes<br><span>${{producto.precio_comparacion}}</span></p>
                            </div>
                        </div>
                        <p v-if="producto.quantity > 0"><NuxtLink class="btn btn-lg btn-secondary" :to="localePath('/productos/'+ producto.id)">{{ $t('Buttons.buy')}}</NuxtLink></p>
                        <p v-if="producto.quantity < 1"><NuxtLink class="btn btn-lg btn-secondary disabled" :to="localePath('/productos/'+ producto.id)" aria-disabled="true">{{ $t('Buttons.OutStock')}}</NuxtLink></p>
                        </div>
                    <div class="col-md-6">
                        <p>{{producto.name}}</p>
                        <p class="articulo-des" v-html="producto.short_description"></p>
                    </div>
                </div>
                <div class="order-md-1">
                <img class="img-fluid" :src="Img_product(producto.product_images)" :alt="producto.name">
                </div>
            </div>
                <!-- articulo 3  -->
                <div class="col-md-6 articulo row" v-for="(producto) in MasDestacado.slice(2,4)" :key="producto.id" :class="{'s-stock': (producto.quantity < 1)}">
                    <div class="sin-stock col-md-4" v-if="producto.quantity < 1">{{ $t('Tag.Nostock')}}</div>
                    <div class="datos-art-dest order-md-1 col-md-6 row">
                        <div class="col-md-12">
                            <p class="n-articulo">{{producto.name}}</p>
                            <div class="precio-dest">
                            <div class="precio-normal col-md-6" v-if="(producto.precio_comparacion != 0)">
                                <p>{{$t('general.Befor_price')}}<br><span>${{producto.precio_comparacion}}</span></p>
                            </div>
                                <div class="precio-oferta col-md-6">
                                    <h3>{{$n(producto.price, 'currency')}}</h3>
                                </div>    
                                
                            </div>
                              <p v-if="producto.quantity > 0"><NuxtLink class="btn btn-lg btn-secondary" :to="localePath('/productos/'+ producto.id)">{{ $t('Buttons.buy')}}</NuxtLink></p>
                              <p v-if="producto.quantity < 1"><NuxtLink class="btn btn-lg btn-secondary disabled" :to="localePath('/productos/'+ producto.id)" aria-disabled="true">{{ $t('Buttons.OutStock')}}</NuxtLink></p>
                            </div>
                    </div>
                    <div class="order-md-2 col-md-6">
                    <img class="img-fluid" :src="Img_product_short(producto.product_images)" :alt="producto.name">
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
        if (images[i].type == "front") {
          var url = images[i].image_url;
        }
      }
      return url;
    },
    Img_product_short(images) {
      for (var i = 0; i < images.length; i++) {
        if (images[i].type == "front_short") {
          var url = images[i].image_url;
        }
      }
      return url;
    },
  },
};
</script>

<style scoped>
.productos-dest {
  background-color: #fff;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
.left-it {
  border-right: 1px solid #000;
  padding: 0 15px 0 0 !important;
}
.datos-art-dest {
  padding: 0 !important;
  margin: 20px 0 !important;
}
.datos-art-dest p {
  font-weight: 800;
}
.articulo-des {
  font-weight: 300 !important;
}
.articulo {
  padding: 10px !important;
  margin: 0 !important;
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