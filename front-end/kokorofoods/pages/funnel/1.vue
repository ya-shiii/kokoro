<template>
    <main role="main">
        <section class="container col-md-12 section" v-if="!mobile">
            <div class="mx-auto" style="width: 80%;">
                <center>
                    <p class="text-uppercase mb-0 py-0" style="color: black; font-size: 3.5rem; font-weight: bold;">Disfruta del sabor del ajo negro con un recetario <span style="color:#D5441C">gratis.</span></p><br>
                    <p class="text-uppercase mt-0 py-0" style="font-size: 3rem; font-weight: smaller;">enviado directamente a tu correo</p>
                </center> 
            </div>
        </section>
        <section class="container col-md-12 section" v-if="!mobile">
            <div class="d-flex flex-wrap">
                <div class="col-7 pl-5">
                    <div class="bg-light-subtle">
                        ...
                    </div>
                    
                </div>
                <div class="col-5">
                    Second div content here
                </div>
            </div>
        </section>
    </main>
    
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
</style>