<template>
  <main role="main" style="background-color:#F3F5E6;">
    <section class="container col-md-12 section" v-if="!mobile">
      
      <!--Head content-->
      <div class="mx-auto" style="width: 100%;">
        <p class="text-center text-uppercase mb-0 py-0" style="color: black; font-size: 3.5rem; font-weight: bold;">Aprovecha el despacho
        <span style="color:#D5441C">gratis.</span></p>
        <p class="text-center text-uppercase mt-0 py-0 mb-0" style="font-size: 3rem; font-weight: smaller;">Agregando una pasta de ajo negro</p>
      </div>
    </section>
    <section class="container col-md-12 section" v-if="!mobile">
      <div class="row p-0">

      <!--Right content-->
      <div class="col-md-7 pl-md-5 order-md-1 order-1">
        <div class="mb-5" style="background-color: #D9D9D9; width:100%; height: 600px;">
          ...
        </div>
      <div class="mb-4">
        <p style="font-size: 16px">Disfruta este ajo negro con un recetario que te ayudara a sorprender amigos y familiares.</p>
        <h4 style="font-weight: 700; color: #000000">Que llevarías:</h4>
        <span><ul>
          <li><span style="font-weight: 700; color: #000000">140gr de Ajo Negro</span>puro $6.500.</li>
          <li><span style="font-weight: 700; color: #000000">100% Ajo Negro</span>sin conservantes.</li>
          <li>Producido con Ajo cultivado en <span style="font-weight: 700; color: #000000">Chile.</span> </li>
          <li>Listo para usar, no necesita cocción.</li>
          <li>Recetario <span style="font-weight: 700; color: #000000">Exclusivo</span> Kokorofoods Valor $3.000</li>
        </ul></span>
        </div>
          <div style="margin-left: 30px">
            <p style="font-size: 16px; margin-bottom: 0">
              <del> Antes: $9.500 </del>
            </p>
            <p style="font-size: 35px; font-weight: 700; margin-bottom: 0">
              $23.500
            </p>
            <p style="font-size: 16px; font-weight: 700">+ despacho ($4.000)</p>
          </div>
        </div>

        <!--Left content-->
        <div class="col-md-5 mb-1 order-md-2 order-2">
          <div class="mb-0 pb-0" style="background-color: #F6F0EE;">
          <div class="mt-0 mb-5" style="background-color: #D5441C;">
          <p class="text-center text-white text-uppercase py-3 px-2" style="font-size: 1.8rem; font-weight: bold;">Agrega una pasta y aprovecha despacho gratis</p>
        </div>
          <form class="mt-5 px-4 pb-5 pt-2">
          <div class="d-flex flex-wrap">
            <p class="mb-4" style="font-size: 16px; font-weight: 700">Ecoge tu ajo negro</p>
            <div class="col-8 mt-2" style="border-top: 2px solid black;"></div>
          </div>           
          <p style="font-size: 16px"><input class="mb-4 form-check-input" type="checkbox">Pasta de ajo negro 140gr</p>
          <p style="font-size: 16px"><input class="mb-4 form-check-input" type="checkbox">Pasta de ajo negro 140gr</p>
          <p style="font-size: 16px"><input class="mb-4 form-check-input" type="checkbox">Pasta de ajo negro con merken 140gr </p>
          <p style="font-size: 16px"><input class="mb-4 form-check-input" type="checkbox">Pasta de ajo negro con maqui 140gr </p>
          <p style="font-size: 16px"><input class="mb-4 form-check-input" type="checkbox">Pasta de ajo negro con miel de ulmo 140gr </p>
          
          <div class="d-flex flex-wrap">
            <div style="flex-basis: 49%; margin-right: 2%;" >
              <p class="mt-5 mb-0" style="font-weight: 700;">Total</p>
              <p style="font-size: 1.5rem; font-weight: 700;">$16.500</p>
            </div>
              <div  style="flex-basis: 49%;" >
                <button type="button" class="mt-5 mb-0 text-uppercase btn btn-outline-dark">compar</button>
              </div>
          </div>
          <div class="pb-2 pt-4 mb-5 px-5" style="">
              <a href="" style="color: grey; text-decoration: underline!important; ">No gracias, quiero pagar el despacho de $4.000</a>
            </div>
            </form>
        </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  auth: "guest",
  data() {
    return {
      //   Title:
      //     '<span class="text-muted">Ajo negro de calidad,</span> <br>comprometidos con el medio ambiente.',
      //   Image_url: "/img/img-nosotros.jpg",
      //   Background_color: "#000000",
      //   title: '<span class="text-muted">Ajo negro</span><br>Ir al Catálogo ',
      //   bu_text: "Ir al Catálogo",
      //   bu_link: "/productos",
      //   image_url: "/img/img-catalogo.jpg",
      //   image_url_mob: "/img/mobile/img-catalogo-1.jpg",
      //   class_section: "ir-catalogo",
      //   title_mobile: 'Headline<span class="text-muted"><br>About Us</span>',
      //   mobile: false,
    };
  },
  mounted: function () {
    if (screen.width < 769) {
      this.mobile = true;
    }
  },
};
</script>

<style>
#omnisend-forms-container {
  display: none;
}
</style>