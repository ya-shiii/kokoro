<template>
  <main role="main" style="background-color:#F3F5E6;">
    <section class="container col-md-12 section" v-if="!mobile">
      <div class="mx-auto" style="width: 80%">
        <center>
          <p
            class="text-uppercase mb-0 py-0"
            style="color: black; font-size: 3.5rem; font-weight: bold"
          >
            Aprovecha el despacho <span style="color: #d5441c">gratis.</span>
          </p>
          <br />
          <p
            class="text-uppercase mt-0 py-0"
            style="font-size: 3rem; font-weight: smaller"
          >
            Agregando una pasta de ajo negro
          </p>
        </center>
      </div>
    </section>
    <section class="container col-md-12 section" v-if="!mobile">
      <div class="d-flex flex-wrap">
        <div class="col-7 pl-5">
          <div
            class="col mb-5"
            style="background-color: grey; height: 400px"
          ></div>
          <div class="mb-4">
            <p style="font-size: 16px">
              Disfruta este ajo negro con un recetario que te ayudara a
              sorprender amigos y familiares.
            </p>
            <h4 style="font-weight: 700; color: #000000">Que llevarías:</h4>
            <span
              ><ul>
                <li>
                  <span style="font-weight: 700; color: #000000">
                    140gr de Ajo Negro
                  </span>
                  puro $6.500.
                </li>
                <li>
                  <span style="font-weight: 700; color: #000000">
                    100% Ajo Negro
                  </span>
                  sin conservantes.
                </li>

                <li>Producido con Ajo cultivado en <span style="font-weight: 700; color: #000000">
                    Chile.
                  </span> </li>
                <li>Listo para usar, no necesita cocción.</li>
                <li>Recetario <span style="font-weight: 700; color: #000000">
                   Exclusivo
                  </span>  Kokorofoods Valor $3.000</li>
              </ul></span
            >
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

         <div class="col-3" style="background-color: #F6F0EE; padding :0!important;">
            <div style="background-color: #D5441C; font-weight: 700;" class="text-white text-uppercase text-center p-3">Agrega una pasta y aprovecha despacho gratis</div>
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