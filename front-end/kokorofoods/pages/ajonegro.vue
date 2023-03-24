<template>
  <main role="main">
    <section class="info-ajo container col-md-12 section" v-if="!mobile">
      <LazyTheHeaderOP
        :title="Title"
        :image="Image_url"
        :background="Background_color"
        v-if="!mobile"
      />
      <div class="row info-text">
        <div class="col-md-8 order-md-1">
          <p v-html="$t('ajoNegro.textBelowHero')"></p>
        </div>
        <div class="col-md-4 order-md-2"></div>
      </div>
      <div class="row">
        <div class="col-md-4">
          <!-- accordion 1 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapseOne"
                  aria-expanded="true"
                  aria-controls="collapseOne"
                >
                  {{ $t("ajoNegro.Historia-Title") }}
                </button>
                <img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapseOne"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body parrafo"
                  v-html="$t('ajoNegro.Historia-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <!-- accordion 2 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse2"
                  aria-expanded="true"
                  aria-controls="collapse2"
                >
                  {{ $t("ajoNegro.Inmune-Title") }}
                </button>
                <img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse2"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body parrafo"
                  v-html="$t('ajoNegro.Inmune-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <!-- accordion 3 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse3"
                  aria-expanded="true"
                  aria-controls="collapse3"
                >
                  {{ $t("ajoNegro.Cardio-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse3"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Cardio-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <!-- fila 2 accordiones -->
        <div class="col-md-4">
          <!-- accordion 4 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse4"
                  aria-expanded="true"
                  aria-controls="collapse4"
                >
                  {{ $t("ajoNegro.Diabetes-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse4"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Diabetes-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <!-- accordion 5 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse5"
                  aria-expanded="true"
                  aria-controls="collapse5"
                >
                  {{ $t("ajoNegro.Energizante-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse5"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Energizante-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <!-- accordion 6 -->
          <div class="accordion" id="accordionExample">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse6"
                  aria-expanded="true"
                  aria-controls="collapse6"
                >
                  {{ $t("ajoNegro.Sexual-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse6"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Sexual-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section
      class="info-contenido container col-12 section-slider seccion"
      v-if="mobile"
    >
      <div class="row featurette">
        <div class="col-12 left-col"></div>
        <div class="col-12 float-text info-mobile-secc">
          <h2
            class="featurette-heading"
            v-html="$t('ajoNegro.Mobile_title')"
          ></h2>
          <img class="separador" src="/img/separador.svg" alt="separador" />
        </div>
        <div class="col-12 right-col">
          <img
            class="img-fluid"
            src="/img/mobile/img-ajo-negro.jpg"
            alt="información 1"
          />
        </div>
      </div>
      <div class="info-text info-cont-mob">
        <img
          src="/img/mobile/top-seccion-img.jpg"
          alt=""
          class="top-img-secc"
        />
        <div class="col-12 float-text articulo">
          <h2
            class="featurette-heading"
            v-html="$t('ajoNegro.Mobile_subtitle')"
          ></h2>
        </div>

        <div class="col-12 articulo">
          <p v-html="$t('ajoNegro.Mobile_descrip')"></p>
        </div>
      </div>

      <!-- accordiones -->
      <div class="">
        <div class="col-12">
          <!-- accordion 1 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapseOne"
                  aria-expanded="true"
                  aria-controls="collapseOne"
                >
                  {{ $t("ajoNegro.Historia-Title") }}
                </button>
                <img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapseOne"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Historia-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-12">
          <!-- accordion 2 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse2"
                  aria-expanded="true"
                  aria-controls="collapse2"
                >
                  {{ $t("ajoNegro.Inmune-Title") }}
                </button>
                <img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse2"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Inmune-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-12">
          <!-- accordion 3 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse3"
                  aria-expanded="true"
                  aria-controls="collapse3"
                >
                  {{ $t("ajoNegro.Cardio-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse3"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Cardio-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12">
          <!-- accordion 4 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse4"
                  aria-expanded="true"
                  aria-controls="collapse4"
                >
                  {{ $t("ajoNegro.Diabetes-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse4"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Diabetes-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12">
          <!-- accordion 5 -->
          <div class="accordion" id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse5"
                  aria-expanded="true"
                  aria-controls="collapse5"
                >
                  {{ $t("ajoNegro.Energizante-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse5"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Energizante-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-12">
          <!-- accordion 6 -->
          <div class="accordion" id="accordionExample">
            <div class="card">
              <div class="card-header" id="headingOne">
                <button
                  class="btn btn-block text-left"
                  type="button"
                  data-toggle="collapse"
                  data-target="#collapse6"
                  aria-expanded="true"
                  aria-controls="collapse6"
                >
                  {{ $t("ajoNegro.Sexual-Title") }}</button
                ><img class="icn-acc" src="/img/acc_arr.svg" alt="" />
              </div>

              <div
                id="collapse6"
                class="collapse"
                aria-labelledby="headingOne"
                data-parent="#accordionExample"
              >
                <div
                  class="card-body"
                  v-html="$t('ajoNegro.Sexual-body')"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- fin - accordiones -->
    </section>
    <LazyTheDestacado
      :MasDestacado="DestacadoData.results"
      :ButtonON="false"
      :CTA_text="text_destacados"
      :ModuleName="name"
      v-if="!mobile"
    />
    <LazyMobileTheDestacadoMob
      :MasDestacado="DestacadoData.results"
      :ButtonON="false"
      :CTA_text="text_destacados"
      :ModuleName="name"
      v-if="mobile"
    />
    <LazyTheMostSale :MasVendidos="MasVendido.results" v-if="!mobile" />
    <LazyMobileTheMostSaleMob
      :MasVendidosMob="MasVendido.results"
      v-if="mobile"
    />
    <!-- <TheRecetas /> -->
    <LazyTheStoreBuy
      :title="title"
      :Button_text="bu_text"
      :Image_URL="image_url"
      :Button_link="bu_link"
      :class_section="class_section"
      v-if="!mobile"
    />
    <LazyMobileTheStoreBuyMob
      :title="title"
      :Button_text="bu_text"
      :Image_URL_mob="image_url_mob"
      :Button_link="bu_link"
      :class_section="class_section"
      v-if="mobile"
    />
  </main>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  auth: "guest",
  head() { return {
    title: 'Beneficios y propiedades del ajo negro',
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
                                    `}],
    meta: [
      {
          hid: "description",
          name: "description",
          content:
            "Conoce todo los beneficios y propiedades del ajo negro"
        },
        {
          hid: "og:title",
          name: "og:title",
          content:
            'Beneficios y propiedades del ajo negro',
        },
        {
          hid: "og:description",
          name: "og:description",
          content:
            "Conoce todo los beneficios y propiedades del ajo negro" 
        },
        {
          hid: "og:image",
          name: "og:image",
          content: "https://kokorofoods.cl/img/img-cont-1.jpg",
        },
        {
          hid: "og:url",
          name: "og:url",
          content: "https://kokorofoods.cl/es/ajonegro",
        },
    ]
  }
  },
  async asyncData({ $axios }) {
    const DestacadoData = await $axios.$get(
      "/api/main/product/?is_destacado=true&store=1"
    );
    return { DestacadoData };
  },
  data() {
    return {
      Title: this.$t("ajoNegro.header_title"),
      Image_url: "/img/img-ajo-negro.jpg",
      Background_color: "#000000",
      text_destacados: this.$t("ajoNegro.text_destacado"),
      name: this.$t("ajoNegro.dosis"),
      title: this.$t("ajoNegro.product_catalogo"),
      bu_text: this.$t("Buttons.GoProducts"),
      bu_link: "/productos",
      image_url: "/img/img-catalogo.jpg",
      image_url_mob: "/img/mobile/img-catalogo-2.jpg",
      class_section: "ir-catalogo",
      mobile: false,
    };
  },
  mounted: function () {
    if (screen.width < 769) {
      this.mobile = true;
    }
  },
  computed: {
        ...mapGetters(['MasVendido'])
  },
};
</script>

<style>
@import "~/assets/css/mobile.css";
.parrafo {
  white-space: pre-wrap;
}
@media screen and (min-width: 769px) {
  .accordion > .card {
    border: 1px solid #3d3d3d !important;
    background-color: #fff !important;
    border-radius: 0 !important;
    color: #000 !important;
    text-decoration: none;
    margin: 10px 0;
  }
  .accordion > .card > .card-header {
    padding: 10px !important;
    display: flex;
  }
  .accordion > .card > .card-header button {
    padding: 10px 10px !important;
    font-size: 0.9em;
  }
  .accordion > .card > .card-header {
    background-color: #fff0 !important;
  }
  .icn-acc {
    float: right;
  }
  .collapse > .card-body {
    padding: 15px !important;
  }
  .ir-catalogo {
    background-color: #f4f5e6;
    padding-left: 80px !important;
    padding-right: 80px !important;
  }
}
</style>