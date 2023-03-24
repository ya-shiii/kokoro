<template>
    <main role="main">
        <section class="info-nos container col-md-12 section" v-if="!mobile">
            <TheHeaderOP :title="Title"
                    :image="Image_url"
                    :background="Background_color"/> 
            <div class="row info-text">
                <div class="col-md-4 order-md-3 flex-column">
                    <h4 class="featurette-title"><strong>El 99%</strong> de nuestros desechos son <strong>reciclados y compostados,</strong> </h4>
                    <p>además nuestro proceso de producción permite obtener un <strong>negro de gran calidad con bajo consumo de energía.</strong> </p>
                </div>
                <div class="col-md-4 order-md-2">
                    <img class="img-fluid logo-foot" src="/img/logo-ku.svg" alt="logo Kumkare">
                </div>
                <div class="col-md-4 order-md-1">
                    <img class="img-fluid logo-foot" src="/img/logo-kokoro.svg" alt="logo kokorofoods">
                </div>
            </div>
        </section>
        <section class="info-contenido container col-12 section-slider seccion" v-if="mobile">
            <div class="row featurette">
                <div class="col-12  left-col">
                </div>
                <div class="col-12 float-text info-mobile-secc">
                <h2 class="featurette-heading" v-html="title_mobile"></h2>
                <img class="separador" src="/img/separador.svg" alt="separador">
                </div>
                <div class="col-12  right-col">
                <img class="img-fluid" src="/img/mobile/abouts_us-img.jpg" alt="información 1">

                </div>
            </div>
            <div class="info-text info-cont-mob">
                <img src="/img/mobile/top-seccion-img.jpg" alt="" class="top-img-secc">
                <div class="col-12 float-text articulo">
                <h2 class="featurette-heading"><span class="text-muted">Producimos un ajo negro de calidad,</span> <br>con total compromiso con el medio ambiente.</h2>
                
                </div>
                <img class="" src="/img/separador.svg" alt="separador">
            </div>
            <div class="row col-12 logos-cont">
            <div class="col-6">
                <img class="img-fluid" src="/img/logo-kokoro.svg" alt="logo kokoro foods">
            </div>
            <div class="col-6">
                <img class="img-fluid" src="/img/logo-ku.svg" alt="logo kokoro foods">
            </div>
            </div>
        </section>
        <section class="proposito container col-md-12 section" v-if="!mobile">
            <div class="row featurette">
            <div class="col-md-4 order-md-1"></div>
            <div class="col-md-4 order-md-2">
                <h2 class="featurette-heading">Nuestro<br>Propósito</h2>
                <img class="img-fluid separador" src="/img/separador.svg" alt="separador">
                <p>{{ $t('Nosotros.proposito_1')}} </p>
                <p>{{ $t('Nosotros.proposito_2')}}
                    <img class="img-fluid logos-nos" src="/img/logos-kokoros.svg" alt="">
                <p>Kokorofoods.com <strong> contacto@kokorofoods.com</strong></p>
                <p><a class="btn btn-lg btn-primary" href="">{{ $t('Nosotros.escribenos')}} </a></p>
            </div>
            <div class="col-md-4 order-md-2">

            </div>
            </div>
        </section>
        <section class="info-nos container col-12 section-slider section" v-if="mobile">
            <div class="row featurette">
            <img src="/img/mobile/top-seccion-img-2.jpg" alt="" class="top-img">
            <div class="col-12  right-col">
                <img class="img-fluid" src="/img/img-nosotros.jpg" alt="información 1">

            </div>
            </div>
            <div class="row info-text-dark">
                <div class="col-12 flex-column">
                    <h4 class="featurette-title"><strong>El 99%</strong> de nuestros desechos son <strong>reciclados y compostados,</strong> </h4>
                    <p>además nuestro proceso de producción permite obtener un <strong>negro de gran calidad con bajo consumo de energía.</strong> </p>
                </div>
                
            </div>
        </section>
        <section class="info-contenido container col-12 section-slider seccion" v-if="mobile">
            <div class="row featurette">
                <div class="col-12   left-col">
                </div>
                <div class="col-12 float-text info-mobile-secc mob-pos">
                <h2 class="featurette-heading">Nuestro<span class="text-muted"><br>
                    Propósito</span></h2>
                <img class="separador" src="/img/separador.svg" alt="separador">
                </div>
                <div class="col-12  right-col">
                <img class="img-fluid" src="/img/mobile/proposito-img-1.jpg" alt="información 1">

                </div>
                <div class="col-12 proposito-mob">
                <p>{{ $t('Nosotros.proposito_1')}} </p>
                <p>{{ $t('Nosotros.proposito_2')}}
                    <img class="img-fluid logos-nos" src="/img/mobile/producto-chileno-1.svg" alt=""></p>
                    <!-- <p>Lorem Ipsum is simply dummy text of the printing and <strong> contacto@industry.com</strong>
                    <p><a class="btn btn-lg btn-primary" href="#">Escribenos Aquí</a></p> -->
                </div>
            </div>
        </section>
        <LazyTheStoreBuy :title="title"
                  :Button_text="bu_text"
                  :Image_URL="image_url"
                  :Button_link="bu_link"
                  :class_section="class_section"
                  v-if="!mobile"/>
        <LazyMobileTheStoreBuyMob :title="title"
                  :Button_text="bu_text"
                  :Image_URL_mob="image_url_mob"
                  :Button_link="bu_link"
                  :class_section="class_section"
                  v-if="mobile"/>
    </main>
</template>

<script>
export default {
    auth: 'guest',
    data () {
        return {
            Title: '<span class="text-muted">Ajo negro de calidad,</span> <br>comprometidos con el medio ambiente.',
            Image_url: '/img/img-nosotros.jpg',
            Background_color: '#000000',
            title: '<span class="text-muted">Ajo negro</span><br>Ir al Catálogo ',
            bu_text: 'Ir al Catálogo',
            bu_link: '/productos',
            image_url: '/img/img-catalogo.jpg',
            image_url_mob: '/img/mobile/img-catalogo-1.jpg',
            class_section: 'ir-catalogo',
            title_mobile: 'Headline<span class="text-muted"><br>About Us</span>',
            mobile: false
        }
    },
    mounted: function() {
      if (screen.width < 769 ){
        this.mobile = true
      }
    }
}
</script>

<style>
@import '~/assets/css/mobile.css';
.proposito-mob {
    padding-top: 78px;
}
.logo-foot {
    width: 50%;
    margin: 0 auto;
}
.proposito{
    background-color: #F4F5E6;
    padding-left: 80px !important;
    padding-right: 80px !important;
}

.ico-time {
    padding: 0 10px 0 0px;
    width: 30px;
}
.bd-placeholder-img {
    font-size: 1.125rem;
    text-anchor: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  .borde-abajo{
      border-bottom: 1px solid #000 !important;
      margin-bottom: 25px;
  }
  .table-border, .table-border-left {
    border: 1px 0px 1px 0px solid #000;
    /* display: flex; */
    border-bottom: 1px solid #000;
    border-top: 1px solid #000;
    margin: 5px 0 20px 0;
    align-items: center;
    align-content: space-between;
    padding-top: 10px;
    padding-bottom: 10px;
}
.table-border-left{
    border-right: 1px solid #000;
}
.share-recipe{
    justify-content: flex-end;
}
.table-border span, .table-border-left span {
    font-weight: 600;
    color: #000;
    margin: 0px 0 0 20px;
    /* text-align: center;
    vertical-align: baseline; */
}
.info-block ul{
    list-style: none !important;
    padding: 0;
}
.table-border p, .table-border-left p {
    font-weight: 400;
    color: #000;
    margin: 0px 0 0 20px;
    /* text-align: center;
    vertical-align: baseline; */
}

  @media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
  }
.info-nos{
    background-color: #FFF;
    padding-left: 80px !important;
    padding-right: 80px !important;
}
.info-text p{
    color: #000;
    font-weight: 400;
}
.info-text {
    padding-top:50px;
}
</style>