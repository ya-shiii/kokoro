<template>
  <main role="main" style="background-color:#F3F5E6; padding-bottom: 60px; min-height: calc(100vh - 60px)">
    <section class="pl-2 pr-2" v-if="!mobile">
      <div class="mx-auto" style="width: 100% ">
          <p class="text-uppercase mb-0 py-0 text-center" style="color: black; font-size: 3.5rem; font-weight: bold">
            <span style="color: #d5441c">24% de descuento</span> En Sal Con Ajo
          </p>
          <p class="text-uppercase mb-0 py-0 text-center" style="color: black; font-size: 3.5rem; font-weight: bold" >Negro </p>
          <p class="text-uppercase mt-0 py-0 text-center" style="font-size: 3rem; font-weight: smaller">
            Agregando una pasta de ajo negro
          </p>
      </div>
    </section>
    <section style="padding:0!important;" v-if="!mobile">
      <div class="d-flex justify-content-center">
        <div>
          <div style="background-color: grey; height: 429px; width: 949px;">
          </div>
        </div>
      </div>
    </section>
    <section style="padding:0!important;" v-if="!mobile">
      <div class="d-flex justify-content-left" style="margin-left: 15%; margin-top: 30px">
        <div>
          <p class="text-start" style="font-size: 16px; margin-top: 2rem;">
            Disfruta este ajo negro con un recetario que te ayudará a sorprender amigos y familiares.
          </p>
          <h4 style="font-weight: 700; color: #000000">Qué llevarías:</h4>
          <span><ul style="padding-left: 40px;">
            <li><span style="font-weight: 700; color: #000000">140gr de Ajo Negro</span> puro $6.500.</li>
            <li><span style="font-weight: 700; color: #000000">100% Ajo Negro</span> sin conservantes.</li>
            <li>Producido con Ajo cultivado en <span style="font-weight: 700; color: #000000">Chile.</span></li>
            <li>Listo para usar, no necesita cocción.</li>
            <li>Recetario <span style="font-weight: 700; color: #000000">Exclusivo</span>  Kokorofoods Valor $3.000</li>
          </ul></span>
        </div>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center">
            <p style="font-size: 16px; margin-bottom: 0">
              <del> Antes: $9.500 </del>
            </p>
            <p style="font-size: 35px; font-weight: 700; margin-bottom: 0">
              $23.500
            </p>
            <p style="font-size: 16px; font-weight: 700">+ despacho ($4.000)</p>
            <div>
              <button type="button" class="mt-5 mb-0 text-uppercase btn btn-outline-dark">compar</button>
            </div>
            <div class="pb-2 pt-4 mb-5">
              <a href="" style="color: grey; text-decoration: underline!important; ">No gracias, quiero pagar el despacho de $4.000</a>
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
main {
  min-height: calc(100vh - 100px); /* Set the minimum height of the main section to be the height of the viewport minus the height of the footer */
}
</style>
