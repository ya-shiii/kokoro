<template>
    <main role="main">
    <div v-if="StoreErrorModal">
    <transition class="modal" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" >Error Tienda no permitida</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
          <p> Al parecer estas intentando agregar un producto de otra tienda que no corresponde a tu pais </p>
          <p> Porfavor cambia tu tienda y agrega el producto adecuado</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="CloseModal">OK</button>
          </div>
        </div>
      </div>
  </transition>
  </div>
        <section class="recetas container col-md-12" v-if="!mobile">
  <div class="row featurette">
    <div class="col-md-7 order-md-2 px-5">
      <div v-html="ProductData.description"></div>
        <p v-if="ProductData.quantity > 0"><button class="btn btn-cart" @click="addProductToCart({product: ProductData, quantity: 1, store: Store_Check})">{{ $t('Buttons.addtocart')}}</button></p>
        <p v-if="ProductData.quantity < 1"><button class="btn btn-cart disabled" >{{ $t('Buttons.addtocart')}}</button></p>
      <div class="row info-block"> <!--row1-->
        <div class="col-md-12 border-top">
        </div>
        <!-- <div class="col-md-12 row px-0 py-5 m-0 tabla-producto-art">
        </div> -->
        <div class="col-md-12 border-bottom">
        
        </div> 
      </div>
      <div class="row info-block"><!--row2-->
        <div class="col-md-12 row py-5" v-html="this.$t('ProductPage.Benefits')">
        </div>
      </div>
    </div>
    <div class="col-md-5 order-md-1">
      <p><NuxtLink class="btn btn-lg btn-primary" :to="localePath('/productos')">{{$t('Buttons.Back')}}</NuxtLink></p>
      <h2 class="featurette-heading pr-3 py-3 pl-0">{{ ProductData.name }}</h2>
      <p class="precio"><strong> {{$t('general.price')}}: <span>{{ $n(ProductData.price, 'currency') }}</span></strong></p>
      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item single-art" v-for="(img, index) in ProductImage" :key="img.id" :class="['slide'+index, {'active': ActiveCalc(index)}]">
          <img :src="img.image_url" class="d-block w-50" :alt="ProductData.name">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    </div>
  </div>
  
        </section>
        <section class="recetas container col-md-12 mt-5 p-0" v-if="mobile">
  <div class="row featurette p-0">
    <div class="col-12 p-0">
      <h2 class="featurette-heading pt-5 pl-4 pr-5">{{ ProductData.name }}</h2>
      <p class="precio pl-4 pr-5">{{$t('ProductPage.price')}}: <span>${{ $n(ProductData.price, 'currency') }}</span></p>

      <div class="col-12 order-2">
        <div id="Carousel-mob-pr" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#Carousel-mob-pr" data-slide-to="0" class=""></li>
            <li data-target="#Carousel-mob-pr" data-slide-to="1" class=""></li>
            <li data-target="#Carousel-mob-pr" data-slide-to="2" class="active"></li>
          </ol>
          <div class="carousel-inner">
    
              <!-- Slide1 -->
            <div class="carousel-item p-5" v-for="(img, index) in ProductImage" :key="img.id" :class="['slide'+index, {'active': ActiveCalc(index)}]">
                <div class="col-12">
                    <div class="">
                      <img :src="img.image_url" class="img-fluid " :alt="ProductData.name">
                    </div>
                </div>
            </div>
              <!-- Fin Slides -->
          </div>
           
          <a class="carousel-control-prev" href="#Carousel-mob-pr" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#Carousel-mob-pr" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div> <!-- Fin carrusel -->
      </div>
        <div class="col-12 p-0 info-articulo pt-3">
          <p v-if="ProductData.quantity > 0"><button class="btn btn-lg btn-light center-button-2 mt-3 mb-3" @click="addProductToCart({product: ProductData, quantity: 1, store: Store_Check})">{{$t('Buttons.addtocart')}}</button></p>
          <p v-if="ProductData.quantity < 1 "><button class="btn btn-lg btn-light center-button-2 mt-3 mb-3 disabled" >{{$t('Buttons.addtocart')}}</button></p>
      <div class="n-articulo-lg pl-4 pr-4" v-html="ProductData.description"></div> 
      <p class="n-articulo-lg pl-4 pr-4 pb-5"></p>
        </div>

      <div class="row info-block mt-5 mb-5"> <!--row1-->
        <div class="col-12">
        </div>
      </div>
      <div class="row info-block"><!--row2-->
        <div class="col-12 row p-4" v-html="this.$t('ProductPage.BenefitsMobile')">
        </div>
      </div>
      
      <p><NuxtLink class="btn btn-lg btn-primary center-button-2 mt-3 mb-3" :to="localePath('/productos')">{{$t('Buttons.Back')}}</NuxtLink></p>
    </div>
  </div>
  </section>
    </main>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
    name: 'index',
    auth: 'guest',
    head() { return {
      title: 'Venta de ' + this.ProductData.name,
    meta: [
      {
          hid: "description",
          name: "description",
          content:
            this.ProductData.description
        },
        {
          hid: "og:title",
          name: "og:title",
          content:
            this.ProductData.name,
        },
        {
          hid: "og:description",
          name: "og:description",
          content:
            this.ProductData.description 
        },
        {
          hid: "og:image",
          name: "og:image",
          content: this.ProductData.product_images[0].image_url,
        },
        {
          hid: "og:url",
          name: "og:url",
          content: "https://kokorofoods.cl/es/productos/" + this.ProductData.id,
        },
    ]
  }
  },
    async asyncData( { $axios, params }) {
        const ProductData = await $axios.$get('/api/main/product/' + params.id + '/')
        return { ProductData }
    },
    data () {
      return {
        mobile: false,
        store_check: 0,
        image_seo: null,
        Product_Image: []
      }
    },
    mounted: function() {
      if (screen.width < 769 ){
        this.mobile = true
      }
    },
    methods: {
      ...mapActions('cart', ['addProductToCart', 'CloseModal']),
      ActiveCalc(index){
        if (index == 0) {
          return true
        } else {
          return false
        }
      }
    },
    computed: {
      ...mapGetters('cart', ['StoreErrorModal']),
      ProductImage() {
        var images = this.ProductData.product_images
        for (var i=0; i < images.length; i++){
          if (images[i].type == 'product' || images[i].type == 'main' ) {
             this.Product_Image.push(images[i])
          }
        }
        return this.Product_Image
      },
      Store_Check(){
        this.store_check = this.$store.getters.GetStore
        return this.store_check
      }
    }
}
</script>

<style>
@import "~/assets/css/mobile.css";
@import "~/assets/css/carousel.css";
@media screen and (min-width: 769px) {
  .recetas {
    background-color: #fff;
    padding-left: 80px !important;
    padding-right: 80px !important;
  }
  .info-block ul {
    list-style: none !important;
    padding: 0;
  }
  .btn-cart {
    background-color: #cbd402 !important;
    text-transform: uppercase;
  }
  .tabla-producto-art {
    display: flex;
    align-content: center;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
  }
  /* Carousel base class */
  .carousel {
    margin-bottom: 4rem;
  }
  /* Since positioning the image, we need to help out the caption */
  .carousel-caption {
    bottom: 3rem;
    z-index: 10;
  }

  /* Declare heights because of positioning of img element */
  .carousel-item {
    height: 32rem;
  }
  .carousel-item > img {
    position: absolute;
    top: 0;
    left: 0;
    min-width: 100%;
    height: 32rem;
  }
  .art-list li {
    list-style: circle;
  }
  .carousel-control-next-icon {
    background-image: url(~/static/img/arrow-carousel.svg) !important;
  }
  .carousel-control-prev-icon {
    background-image: url(.~/static/img/arrow-l.svg) !important;
  }
}
</style>