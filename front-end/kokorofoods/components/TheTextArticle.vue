<template>
<section class="info-contenido container col-md-12">
    <div class="row featurette">
        <div class="col-md-3 order-md-1 left-col">
        </div>
      <div class="col-md-3 order-md-3 float-text">
        <h2 class="featurette-heading" v-html="Title"></h2>
        <img class="img-fluid separador" src="/img/separador.svg" alt="separador">
      </div>
      <div class="col-md-9 order-md-2 right-col">
        <img class="img-fluid" src="/img/img-cont-1.jpg" alt="información 1">

      </div>
    </div>
    <div class="row info-text">
        <div class="col-md-4 order-md-1">
            <h4 class="featurette-title">{{ $t('TextArticleModule.Title_small')}}</h4>
        </div>
        <div class="col-md-4 order-md-2">
            <p>{{ $t('TextArticleModule.body_1')}}</p>
            <p>{{ $t('TextArticleModule.body_2')}}</p>
        </div>
        <div class="col-md-4 order-md-3">
            <p>{{ $t('TextArticleModule.body_3')}}</p>
            <p>{{ $t('TextArticleModule.body_4')}}</p>
        </div>
    </div>
</section>
    
</template>
<script>
export default {
    computed: {
      Title() {
       return this.$t('TextArticleModule.Title')
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
</style>