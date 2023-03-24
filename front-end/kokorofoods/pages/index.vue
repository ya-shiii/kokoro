<template>
  <div>
    <LazyTheSlider :sliders="sliderData.results" v-if="!mobile" />
    <LazyMobileTheSliderMob :sliders="sliderData.results" v-if="mobile" />
    <LazyTheProductM v-if="!mobile" />
    <LazyMobileTheProductMob v-if="mobile" />
    <LazyTheArticleM v-if="!mobile" />
    <LazyMobileTheArticleMMob v-if="mobile" />
    <LazyTheTextArticle v-if="!mobile" />
    <LazyMobileTheTextArticleMob v-if="mobile" />
    <LazyTheMostSale :MasVendidos="MasVendido.results" v-if="!mobile" />
    <LazyMobileTheMostSaleMob
      :MasVendidosMob="MasVendido.results"
      v-if="mobile"
    />
    <LazyTheDestacado
      :MasDestacado="MasDestacadoG.results"
      :ButtonON="true"
      :ModuleName="name"
      v-if="!mobile"
    />
    <LazyMobileTheDestacadoMob
      :MasDestacado="MasDestacadoG.results"
      :ButtonON="true"
      :ModuleName="name"
      v-if="mobile"
    />
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
    <!-- <TheTips /> -->
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "index",
  auth: "guest",
  async asyncData({ $axios }) {
    const sliderData = await $axios.$get("/api/main/slider/");
    return { sliderData };
  },
  head() { return {
    title: 'Tienda de ajo negro',
    meta: [
      {name: "google-site-verification", content: "YawYAJZ2jL7NvIUf13QCPadM5MyYk5Izcc99vJmdGec"},
      {name: "description", content: "Disfruta de todo los beneficios del ajo negro, compra online con despacho a todo Chile"},
      {
          hid: "description",
          name: "description",
          content:
            "Tienda de ajo negro en capsulas, dientes y pastas"
        },
        {
          hid: "og:title",
          name: "og:title",
          content:
            "Tienda de ajo negro",
        },
        {
          hid: "og:description",
          name: "og:description",
          content:
            "Tienda de ajo negro con despacho a todo Chile " 
        },
        {
          hid: "og:image",
          name: "og:image",
          content: "https://kokorofoods.cl/img/img-cont-1.jpg",
        },
        {
          hid: "og:url",
          name: "og:url",
          content: "https://kokorofoods.cl/es",
        },
    ]
  }
  },
  computed: {
    ...mapGetters(["MasVendido", "MasDestacadoG"]),
  },
  data() {
    return {
      name: this.$t("TheDestacadoModule.name"),
      title: this.$t("TheStoreBuyModule.Title"),
      bu_text: this.$t("Buttons.ViewStores"),
      bu_link: this.localePath('/tiendas'),
      image_url: "img/img-donde.jpg",
      image_url_mob: "img/mobile/donde-comprar-1.png",
      class_section: "donde-comprar",
      mobile: false,
    };
  },
  mounted: function () {
    if (screen.width < 769) {
      this.mobile = true;
    }
  }
}
</script>

<style>
#main {
  transition: margin-left 0.5s;
  transition: ease-in 0.5s;
  padding: 16px;
}
section {
  padding-top: 100px;
}
.section {
  padding-top: 100px;
  padding-bottom: 50px;
}
@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}
</style>