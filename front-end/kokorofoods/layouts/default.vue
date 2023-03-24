<template>
  <div>
    <LazyTheHeader v-if="!mobile" />
    <LazyMobileTheHeaderMob  v-if="mobile" />
    <main role="main">
        <Nuxt />
        <LazyTheFooter v-if="!mobile" />
        <LazyMobileTheFooterMob v-if="mobile" />
    </main>
  </div>
</template>
<script>
export default {
    data () {
        return {
            mobile: false,
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
@media screen and (min-width: 769px) {
    body{
        padding: auto;
        margin: auto;
        font-family: 'Mukta', sans-serif !important;
        color: #000;
    }
    a{
        text-decoration: none !important;
        font-size: 0.9em !important;
        color: #D5441C;
    }
    p a{
        color: #D5441C;
    }
    .text-left {
        letter-spacing: 0 !important;
    }
    p{
        font-size: 0.9rem;
        color: #000;
    }
    .border-bottom-00 {
        border-bottom: 1px solid #000 !important;
        margin: 20px 0;
        padding: 10px 0 10px 0 !important;
    }
    .lead{
        font-size: 16px !important;
        font-weight: 300;
    }
    .row{
        margin-right: 0 !important;
        margin-left: 0 !important;
    }
    .btn{
        padding: 10px 20px !important;
        letter-spacing: 0.2em;
    }
    .btn-primary{
        background-color: #000 !important;
        border-color: #000 !important;
        text-transform: uppercase;
        font-size: 0.8em !important;
    }
    .btn-secondary {
        color: #000 !important;
        background-color: #fff0 !important;
        border-color: #000 !important;
        font-size: 0.8em !important;
        text-transform: uppercase;
    }
    .footer .btn-outline-primary {
        color: #fff !important;
        border-color: #fff !important;
        background-color: #fff !important;
        color: #000 !important;
    }
    .btn-outline-primary {
        color: #000 !important;
        border-color: #000 !important;
        background-color: #000 !important;
        color: #fff !important;
    }
    .pagination{
        margin: 0 auto !important;
    }
    .page-link {
        border: 0 solid !important;
        color: #000 !important;
        background-color: #fff0 !important;
    }
    .section{
        padding-top: 100px;
        padding-bottom: 50px;
    }
}
</style>
