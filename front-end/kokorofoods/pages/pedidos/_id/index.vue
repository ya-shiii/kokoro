<template>
    <section class="p-0 m-0 col-lg-12 row">
        <!-- MENU USUARIO IZQUIERDO -->
        <div class="info-left col-lg-4 p-0">
        <!-- user id - menu -->
            <div class="row featurette user-id">
                <div class="id-menu center-itms ">
                    <p><strong>{{name}}</strong></p><a href="#"><img class="user-icon"  src="/img/edit-icon.svg" alt=""></a>
                </div>
            </div>
            <!-- user id - menu -->
            <ul class="navbar-nav mr-auto usr-mn">
                <li class="nav-item border-bottom active">
                    <NuxtLink class="nav-link" :to="localePath('/pedidos')">{{ $t("orders.my_orders") }} <span><img src="/img/path.svg" alt=""></span><span class="sr-only">(current)</span></NuxtLink>
                </li>
                <!-- <li class="nav-item border-bottom">
                <a class="nav-link" href="recetas-favoritas.html">Recetas Favoritas <span><img src="img/path.svg" alt=""></span></a>
                </li>
                <li class="nav-item border-bottom">
                <a class="nav-link" href="tips.html" tabindex="-1">Tips Favoritos <span><img src="img/path.svg" alt=""></span></a>
                </li>
                <li class="nav-item border-bottom">
                <a class="nav-link" href="suscripcion.html" tabindex="-1">Suscripciones<span><img src="img/path.svg" alt=""></span></a>
                </li> -->
            </ul>
        </div>
        <!-- MENU USUARIO DERECHO -->
        <div class="info-right col-lg-8 p-0 usuario-der">
            <div class="row featurette title-id">
                <div class="center-itms">
                <h3><strong>MIS PEDIDOS</strong></h3>
                </div>
            </div>
            <!-- user id - menu -->
            <div class="row featurette title-pedido">
                <div class="center-itms col-12">
                <h3><strong>Pedido #<span> {{OrdersData.results[0].order_number}}</span></strong></h3>
                <p v-if="OrdersData.results[0].tracking_number">Seguimiento# <span> {{OrdersData.results[0].tracking_number}}</span></p>
                <p v-if="!OrdersData.results[0].tracking_number">Seguimiento# <span> En bodega</span></p>
                </div>
            </div>
            <div class="row featurette title-seguimiento">
                <div class="center-itms">
                    <p>Estado del Pedido</p>
                    <div class="seguimiento col-12">
                        <img src="/img/icon-origen.svg" alt="" class="origen on">
                        <img src="/img/linea-ico.svg" alt=""><img src="/img/ico-transito.svg" alt="" class="transito">
                        <img src="/img/linea-ico.svg" alt=""><img src="/img/ico-entregado.svg" alt="" class="entregado">
                    </div>
                    <h4 class="estado-envio" v-if="!OrdersData.results[0].tracking_number">EN ORIGEN</h4>
                    <h4 class="estado-envio" v-if="OrdersData.results[0].tracking_number">DESPACHADO</h4>
                </div>
            </div>
            <!-- user id - menu -->
            <div class="pedidos col-12 mt-3 mb-3 p-0">
                
                <ul class="p-3 lista-pedido">
                    <!-- Listado de items -->
                    <li><h4 class="titulo-pedido">Detalle del Pedido <span class="badge badge-secondary">{{OrdersData.results[0].status}}</span></h4></li>
                    <li class="pedido-item p-0 pb-3 col-12 border-bottom" v-for="item in OrdersData.results[0].products" :key="item">
                        <div class="col-12 p-0 m-0 row">
                            <div class="col-6 p-0 mt-0 mb-0">
                            <img :src="image(item.product.product_images)" alt="" class="img-art-pedidos">
                            </div>
                        <div class="col-6 p-0 mt-0 mb-0">
                            <div class="col-12 articulo row">
                            <div class="col-12">
                                <p class="n-articulo">{{item.product.name}}</p>
                                <div class="precio-oferta col-12 row">
                                    <h4><span><strong>${{item.product.price}}</strong></span></h4>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </li>
                    <!-- <li class="row">
                        <h4 class="titulo-pedido">Forma de envío</h4>
                    </li>
                    <li class="input-seguimiento mt-3">
                        <input type="radio" name="envio" id="">
                        <p>Standard (16 days)</p><p>Gratis</p>
                    </li> -->
                </ul>
            </div>
            <div class="item-total">
                <ul class="lista-total">
                    <li><p>Subtotal</p><p>${{OrdersData.results[0].total_gross}}</p></li>
                    <li><p>Envío</p><p>${{OrdersData.results[0].shipping_cost}}</p></li>
                    <li><h5 class="numero-total">Total</h5><h5>${{OrdersData.results[0].total_net}}</h5></li>
                </ul>
            <!-- <p><a class="btn btn-outline-secondary center-itms" href="#">pedir de nuevo</a></p> -->
            </div>
            <div class="info-suscripcion">
            
            </div>
        </div>
  </section>
</template>
<script>
export default {
    data() {
              return {
              }
          },
    async asyncData({ $axios, $auth, route}) {
        const OrdersData = await $axios.$get("/api/main/order/?user=" + $auth.user[0].id + '&order_number=' + route.params.id);
        return { OrdersData };
        },
    methods:{
        image(images){
            for(var im = 0; im<images.length; im++){
                if (images[im].type == 'main'){
                    return images[im].image_url
                }
            }
        }
    },
    computed: {
               name(){

                    return this.$auth.user[0].first_name + ' ' + this.$auth.user[0].last_name
               }
          }
    
}
</script>
<style lang="css" scoped>
@import "~/assets/css/user.css";

</style>