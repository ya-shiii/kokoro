<template>
    <section class="productos-mas container col-sm-12">
    <div class="row featurette">
      <div class="col-12 order-1">
        <h2 class="featurette-heading"><span class="text-muted"><br>Nuestros
            productos</span><br> más vendidos</h2>
        <img class="separador" src="/img/separador.svg" alt="separador">
      </div>


      <!-- SLIDER 1 === PRODUCTOS -->

      <div class="col-12 order-2">
        <div id="Carousel-mob-pr" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#Carousel-mob-pr" data-slide-to="0" class=""></li>
            <li data-target="#Carousel-mob-pr" data-slide-to="1" class=""></li>
            <li data-target="#Carousel-mob-pr" data-slide-to="2" class="active"></li>
          </ol>
          <div class="carousel-inner">
    
              <!-- Slide1 -->
            <div class="carousel-item  active slide1" >
                <div class="col-12">
                    <div class="">
                      <NuxtLink :to="localePath('/productos/3')">
                      <img src="/img/mobile/pasta-maqui-mobile.png" class="img-fluid " alt="..."></NuxtLink>
                    </div>
                    <div class="col-2 sld-right img-fluid padd-sld-itm"></div>
                </div>
            </div>
    
            <!-- Slide2 -->
            <div class="carousel-item slide2">
              <div class="col-12">
                <div class="">
                   <NuxtLink :to="localePath('/productos/8')">
                  <img src="/img/mobile/pasta_oliva_mobile.png" class="img-fluid " alt="...">
                   </NuxtLink>
                </div>
                
            </div>
            </div>
    
            <!-- Slide3 -->
            <div class="carousel-item slide3">
              <div class="col-12">
                <div class="col-12 padd-sld-itm">
                  <NuxtLink :to="localePath('/productos/2')">
                  <img src="/img/mobile/Pasta_ulmo.png" class="img-fluid " alt="...">
                  </NuxtLink>
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
        </div>
      </div>
<!-- SLIDER 2 === PRODUCTOS -->
        <div class="col-12 order-3">
          <div id="Carousel-mob-pr2" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li data-target="#Carousel-mob-pr2" data-slide-to="0" class=""></li>
              <li data-target="#Carousel-mob-pr2" data-slide-to="1" class=""></li>
              <li data-target="#Carousel-mob-pr2" data-slide-to="2" class="active"></li>
            </ol>
            <div class="carousel-inner">
      
                <!-- Slide1 -->
              <div class="carousel-item  active slide1">
                  <div class="col-12">
                    <div class="">
                      <NuxtLink :to="localePath('/productos/44')">
                      <img src="/img/mobile/Capsula_ajo_negro_mobile.png" class="img-fluid " alt="Extracto de ajo negro">
                      </NuxtLink>
                      </div>
                      <div class="col-2 sld-right img-fluid padd-sld-itm"></div>
                  </div>
              </div>
      
              <!-- Slide2 -->
              <div class="carousel-item slide2">
                <div class="col-12">
                  <div class="">
                      <NuxtLink :to="localePath('/productos/48')">
                    <img src="/img/mobile/capsula_maqui_mobile.png" class="img-fluid " alt="...">
                      </NuxtLink>
                    </div>
                  
              </div>
              </div>
      
              <!-- Slide3 -->
              <div class="carousel-item slide3">
                <div class="col-12">
                  <!--  -->
                  <div class="col-12 padd-sld-itm">
                    <NuxtLink :to="localePath('/productos/19')">
                    <img src="/img/mobile/extracto_mobile.png" class="img-fluid " alt="...">
                    </NuxtLink>
                    </div>
                  
              </div>
              </div>
        
                <!-- Fin Slides -->
              </div>
            </div>
            <a class="carousel-control-prev" href="#Carousel-mob-pr2" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#Carousel-mob-pr2" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>  
    </div>

    
</section>
</template>
<script>
export default {
    data() {
      return {
        sendrow: false,
      }
    },
    props: {
        MasVendidosMob: Array
    },
    methods: {
        checkrow: function(index) {
            if (index > 1) {
                this.sendrow = true;
            }
        },
        titleFormat(name) {
            var short = name.toString().split(" ")
            var title = ""
            var secondPart = ""
            for (var index = 0; index < 4; index++) {
                title += short[index] + ' ';    
            }
            title += "<br>"
            for (var index = 4; index < short.length; index++) {
                secondPart += short[index] + ' ';
            }
            title += '<span class="pero-art">' + secondPart + '</span>'
            return title
        }
    }
}
</script>

<style scoped>
@import '~/assets/css/mobile.css';
</style>