<template>
    <section class="section-slider">  <!-- slider principal-->
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class=""></li>
        <li data-target="#myCarousel" data-slide-to="1" class=""></li>
        <li data-target="#myCarousel" data-slide-to="2" class="active"></li>
      </ol>
      <div class="carousel-inner" >

          <!-- Slide1 -->
        <div class="carousel-item" v-for="slide in sliders" :key="slide.id" :class="{active: slide.data.IsActive, 'slide1': slide.data.slide1, 'slide2': slide.data.slide2,
              'slide3': slide.data.slide3}">
            <div class="row">
                <div class="col-md-5 sld-left img-fluid padd-sld-itm">
                    <div class="container">
                        <div class="carousel-caption text-left row">
                          <div class="col-md-12">
                            <h1>{{slide.data.title}}</h1>
                          </div>
                          <div class="col-md-4" v-if="slide.data.img_oferta">
                            <img :src="slide.data.img_oferta" alt="" class="img-oferta">
                          </div>
                          <div class="col-md-8">
                            <p>{{slide.data.product_name}}</p>
                            <img class="img-fluid separador" src="img/separador.svg" alt="separador">
                          </div>
                          <div class="precio row container-fluid">
                            <h3 class="precio-oferta">{{slide.data.precio_oferta}}</h3>
                            <div class="precio-normal">
                              <h4 v-if="slide.data.precio_antes">antes<br><span>{{slide.data.precio_antes}}</span></h4>
                            </div>
                          </div>
                          <div class="container-fluid"><NuxtLink class="btn btn-lg btn-primary" :to="slide.data.link">{{$t('Buttons.buy')}}</NuxtLink></div>
                        </div>
                      </div>
                </div>
                <div class="col-md-5 padd-sld-itm"><img :src="slide.data.img_prin" class="img-fluid " :alt="slide.data.title"></div>
                <div class="col-md-2 sld-right img-fluid padd-sld-itm"></div>
            </div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
</section>
</template>

<script>
export default {
  props: {
    sliders: Array,
    isProduct: Boolean
  }
}
</script>

<style>
@import '~/assets/css/carousel.css';
.section-slider{
      padding: 0 !important;
  }

 .slide1 .sld-left{
      background-color: #90DDE2;
      padding: 0;
      margin: 0;
  }

 .slide1 .sld-right{
      background-color: #FB925B;
      padding: 0;
      margin: 0;
  }
  .slide2 .sld-left{
    background-color: #FB925B;
    padding: 0;
    margin: 0;
}

.slide2 .sld-right{
    background-color: #90DDE2;
    padding: 0;
    margin: 0;
}
.slide3 .sld-left{
    background-color: #90DDE2;
    padding: 0;
    margin: 0;
}

.slide3 .sld-right{
    background-color: #FB925B;
    padding: 0;
    margin: 0;
}
  .padd-sld-itm{
      padding-left: 0 !important;
      padding-right: 0 !important;
      margin: 0;
  }
  .carousel-item {
    height: auto !important;
}
  
  .carousel{
      margin-bottom: 0 !important;
  }

  .carousel-control-next, .carousel-control-prev {
    position: absolute;
    top: 0;
    bottom: 0;
    z-index: 1;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    -ms-flex-pack: center;
    justify-content: center;
    width: 5% !important;
    color: #fff;
    text-align: center;
    opacity: .5;
    transition: opacity .15s ease;
}
.img-oferta{
    width: 100%;
}
.carousel-control-next-icon {
    background-image: url(/img/arrow-carousel.svg) !important;
}
.carousel-control-prev-icon {
    background-image: url(/img/arrow-l.svg) !important;
}
.carousel h1{
    color: #000 !important;
    font-weight: 600;
    font-size: 2.5rem !important;
}
.carousel p{
    color: #000 !important;
    font-weight: 400;
    font-size: 1.4rem !important;
}
h3.precio-oferta {
    color: #000;
    font-size: 2.5em;
    font-weight: 600;
}
.precio-oferta h3 {
    color: #000;
    font-size: 1.5rem;
    font-weight: 600;
}
.precio-oferta{
    padding-left: 0 !important;
    padding-right: 0 !important;
}

.precio-normal{
    padding-left: 20px !important;
}
.precio-normal h4, .precio-normal p {
    color: #000;
    font-size: 1em;
    font-weight: 400;
    text-transform: capitalize;
}
.precio-normal h4>span, .precio-normal p>span {
    color: #000;
    font-size: 1em;
    font-weight: 400;
    text-decoration: line-through;
}
.precio-dest .precio-normal{
    padding: 0  !important;

}
.ico-cont img {
    background: #000;
    padding: 5px;
    border-radius: 10px;
}
.form-cont li {
    background-color: #fff0 !important;
    list-style: none;
    margin: 35px auto;
    text-align: center;
    border-bottom: 1px solid #000;
}
.form-cont input {
    background-color: #fff0;
    border: 0px solid;
    text-align: center;
    color: #000 !important;
}
</style>