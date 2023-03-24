<template>
    <div>
        <footer class="container-fluid py-5 bg-dark-footer footer">
            <div class="row col-12 col-sm">
                <div class="col-12 col-sm">
                <ul class="list-unstyled text-small">
                    <li><p>{{$t('Footer.language')}} <span><img src="/img/path.svg" alt=""></span><span class="idioma">
                        <button class="btn my-2 my-sm-0" :class="css_langES" @click="$i18n.setLocale('es')" :type="LanClass">esp</button></span><span class="idioma">
                        <button class="btn my-2 my-sm-0" :class="css_langEN" @click="$i18n.setLocale('en')" :type="LanClass">eng</button></span></p></li>
                </ul>
                <p class="p-logo"><img src="/img/logo-kokoro-wt.svg" alt="" class="img-fluid logo-foot"></p>
                <p class="p-logo"><img src="/img/logo-kumkare-wt.svg" alt="" class="img-fluid align-middle logo-foot"></p>
                <ul class="list-unstyled text-small">
                    
                    <li><p class="text-center"> © 2021, Kokorofoods</p></li>
                    <li class="border-bottom"><p class="text-center">{{$t('Footer.about')}}</p></li>
                    <li><h2 class="text-center">{{$t('Footer.Redes')}}</h2></li>
                    <li class="icons_rrss"><a class="text-muted text-center" href="https://www.facebook.com/kokorofoodsChile/?ref=br_rs"><img src="/img/logotipo-circular-de-facebook.svg" alt="" ><span>@kokorofoodsChile</span></a></li>
                    <li class="icons_rrss"><a class="text-muted" href="https://twitter.com/ajonegro_chile"><img src="/img/logo-twitter.svg" alt="" ><span>@AjoNegro_Chile</span></a></li>
                    <li class="icons_rrss"><a class="text-muted" href="https://www.instagram.com/ajo_negro_chile/"><img src="/img/logo-instagram.svg" alt="" ><span>@ajo_negro_chile</span></a></li>
                    <li></li>
                </ul>
                </div>
                <div class="col-12 col-sm">
                <ul class="list-unstyled text-small">
                    <li><h3 class="text-center">{{$t('Footer.Newsletter_title')}}</h3></li>
                    <li><p class="text-center">{{$t('Footer.Newsletter_body')}}</p></li>
                    <li><input class="form-control mr-sm-2" type="text" placeholder="Tu correo electrónico" aria-label="Search"></li>
                    <li class="border-bottom"><button class="btn btn-outline-secondary center-button-2 center-btn" type="submit">{{$t('Buttons.Sent')}}</button></li>
                    <li><h3 class="text-center">{{$t('Footer.PuntosVentas_title')}}</h3></li>
                    <li><button class="btn btn-outline-secondary my-2 my-sm-0 center-button-2" type="submit" @click="Store">{{$t('Buttons.SalesPoint')}}</button></li>
                </ul >
                </div>
                <div class="col-12 col-sm">
                <ul class="list-unstyled text-small">

                    <li><h3 class="text-center">{{$t('Footer.contact_info')}}</h3></li>
                    <li><p class="text-center">{{$t('Footer.contact_body')}}</p></li>
                    <li class="border-bottom"><button class="btn btn-outline-secondary my-2 my-sm-0 center-button-2" type="submit" @click="Contacto">{{$t('Buttons.ContactUS')}}</button></li>
                    <li><h3 class="text-center">{{$t('Footer.qainfo')}}</h3></li>
                    <li><button class="btn btn-outline-secondary my-2 my-sm-0 center-button-2" type="submit">{{$t('Buttons.qaButton')}}</button></li>
                </ul>
                </div>
                
            </div>
        </footer>
        <div class="formas-pago row">
        <div class="col-12 row">
            <ul class="list-group lista-pago">
                <li class="list-group-item"><h3 class="text-center">{{$t('Footer.Payment_title')}}</h3></li>
                <li class="list-group-item"><p class="text-center"> {{$t('Footer.Payment_body')}}</p></li>
                <li class="list-group-item"><img class="img-fluid" src="/img/pago-icons.svg" alt=""></li>
            </ul>
        </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      css_langES: "btn-outline-primary",
      css_langEN: "btn-outline-secondary",
      lang: this.$i18n.locale,
    };
  },
  methods: {
    Contacto() {
      this.$router.push(this.localePath("/contacto"));
    },
    Store() {
      this.$router.push(this.localePath("/tiendas"));
    },
  },
  computed: {
    LanClass() {
      const lang = this.$i18n.locale;
      if (lang == "en") {
        this.css_langES = "btn-outline-secondary";
        this.css_langEN = "btn-outline-primary";
        return "submit";
      } else {
        this.css_langES = "btn-outline-primary";
        this.css_langEN = "btn-outline-secondary";
        return "submit";
      }
    },
  },
};
</script>

<style scoped>
@import "~/assets/css/mobile.css";
</style>