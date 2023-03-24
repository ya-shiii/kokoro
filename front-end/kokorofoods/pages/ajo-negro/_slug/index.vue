<template>
    <main>
     <section class="info-ajo container col-md-12 section">
      <LazyTheHeaderOP
        :title="Title"
        :image="Image_url"
        :background="Background_color"
        v-if="!mobile"
      />
      <LazyMobileTheHeaderOPMob :title="Title" v-if="mobile" />
    </section>
    <section class="productos container col-md-12" v-if="!mobile">
        <div class="row featurette">
        <div class="col-3 order-md-2">
            <h2 class="featurette-heading">Vivir preocupado del colesterol no es agradable</h2>
            <img
            class="img-fluid separador"
            src="/img/separador.svg"
            alt="separador"
            />
            <p class="lead">La videa es muy corta para pasarla preocupada del colesterol</p>
        </div>
        <div class="col-9 order-md-1">
            <img class="img-fluid" src="/img/colesterol_worried.png" alt="colesterol" />
        </div>
        </div>
    </section>
    <section class="info-contenido container col-md-12">
    <div class="row featurette">
        <div class="col-md-3 order-md-1 left-col">
        </div>
      <div class="col-md-3 order-md-3 float-text">
        <h2 class="featurette-heading">100% natural ayuda a disminuir el colesterol </h2>
        <img class="img-fluid separador" src="/img/separador.svg" alt="separador">
      </div>
      <div class="col-md-9 order-md-2 right-col">
        <img class="img-fluid" src="/img/img-cont-1.jpg" alt="información 1">

      </div>
    </div>
    <div class="row info-text">
        <div class="col-md-4 order-md-1">
            <h4 class="featurette-title">Y ademas es muy rico y con increibles beneficios para la salud</h4>
        </div>
        <div class="col-md-4 order-md-2">
            <p>1. Ajo negro ayuda a disminuir el colesterol malo y aumenta el bueno</p>
            <p>2. Disminuyendo el riesgo a enfermedades cardio vasculares</p>
        </div>
        <div class="col-md-4 order-md-3">
            <p>3. Sin olor a ajo y de rico sabor (ideal para tus recetas favoritas)</p>
            <p></p>
        </div>
    </div>
    </section>
    <LazyTheDestacado
      :MasDestacado="DestacadoData.results"
      :ButtonON="false"
      :CTA_text="text_destacados"
      :ModuleName="name"
      v-if="!mobile"
    />
    <section class="container my-5 productos col-md-12 pb-5">
          <div class="row justify-content-md-center my-4">
            <h3>Compra con tres simples pasos</h3>
          </div>
           <div class="row mb-3">
            <div class="col"><img src="/img/checklist.svg" class="mx-auto d-block" alt="" width="20%"></div>
            <div class="col"><img src="/img/coin.svg" class="mx-auto d-block" alt="" width="20%"></div>
            <div class="col"><img src="/img/fast-delivery.svg" class="mx-auto d-block" alt="" width="20%"></div>
          </div>
          <div class="row">
            <div class="col text-center"><h4>Selecciona tu producto</h4></div>
            <div class="col text-center"><h4>Realiza el pago</h4></div>
            <div class="col text-center"><h4>Despacho a todo Chile</h4></div>
          </div>
          <div class="row">
            <div class="col pb-5"><p>Agrega el producto al carro de compra haciendo click en comprar</p></div>
            <div class="col pb-5"><p>LLena toda la información y realiza el pago con tarjetas de debito o credito. Toda la información es encriptada para otorgar mas seguridad</p></div>
            <div class="col pb-5"><p>Recibe el ajo negro en tu casa, <strong>con compras superiores a 18 mil pesos el despacho es gratis.</strong></p></div>
          </div>
    </section>
    </main>
    
</template>

<script>
export default {
    auth: 'guest',
     async asyncData({ $axios }) {
    const DestacadoData = await $axios.$get(
      "/api/main/product/?is_destacado=true&store=1"
    );
    return { DestacadoData };
  },
  head(){
        return {
            script: [{ type: 'text/javascript',
                        body: true,
                        defer: true,
                        innerHTML: `(function () {
                                    soicos.registerConversion({
                                    pid: '13211',
                                    data: "",
                                    trans: {
                                    orderID:"",
                                    store_name: 'Kokorofoods',
                                    total:"" ,
                                    currency: "CLP",
                                    }
                                    });
                                    })();
                                    `}]
        }
    },
    data () {
        return {
        Title: "<span class='text-muted'>Ajo negro</span> <br> el arma secreta contra el colesterol",
        Image_url: '/img/tips.jpg',
        Background_color: "#000000",
        text_destacados:"Todo nuestros productos son <strong>100% naturales</strong> y usamos capsulas vegetales, nada de quimicos.",
        name: "La salud para nosotros es muy importante",
        page: 1,
        mobile: false,
        lang: this.$i18n.locale
        }
    },
    mounted: function() {
      if (screen.width < 769 ){
        this.mobile = true
      }
    }
    
}
</script>

<style scoped="css">
.info-text div{
    display: flex;
}
.info-text{
padding-top:50px;
}
.right-col{
    padding: 0 !important;
}
.info-contenido{
    background-color: #F4F5E6;
    padding-left: 80px !important;
    padding-right: 80px !important;
}
.featurette-heading {
    margin-top: 0 !important;
    color: #000 !important;
    font-weight: bold !important;
    font-size: 2.5em !important;
}
.featurette-heading span{
 font-weight: normal !important;
 color: #000 !important;
}
h4.featurette-title {
    color: #000;
    font-weight: 400;
}
.left-col {
    background-color: #000;
}
.float-text {
    position: absolute !important;
    z-index: 10;
    background-color: #F4F5E6;
    padding: 30px 5px 20px 5px;
    left: 150px;
}
img.img-fluid.separador {
  padding-bottom: 35px;
}
.featurette-heading {
  margin-top: 0 !important;
  color: #000 !important;
  font-weight: bold !important;
  font-size: 2.5em !important;
}
.featurette-heading span {
  font-weight: normal !important;
  color: #000 !important;
}
h4.featurette-title {
  color: #000;
  font-weight: 400;
}
.info-text p {
  color: #000;
  font-weight: 400;
}
.productos {
  background-color: #f4f5e6;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
</style>