<template>
    
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