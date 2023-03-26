<template>
    <main role="main">
        <section class="container col-md-12 section" v-if="!mobile">
            <!--Head content-->
            <div class="mx-auto" style="width: 100%;">
                    <p class="text-center text-uppercase mb-0 py-0" style="color: black; font-size: 3.5rem; font-weight: bold;">Disfruta del sabor del ajo negro con un recetario
                        <span style="color:#D5441C">gratis.</span></p>
                    <p class="text-center text-uppercase mt-0 py-0" style="font-size: 3rem; font-weight: smaller;">enviado directamente a tu correo</p>
            </div>
        </section>
        <section class="container col-md-12 section p-0" v-if="!mobile">
            <div class="row p-0">
                <!--Right content-->
                <div class="col-md-7 pl-md-5 order-md-1 order-1">
                    <div class="mb-5" style="background-color: #D9D9D9; width:100%; height: 600px;">
                        ...
                    </div>
                    <div>
                        <p class="pl-2 mb-5 text-start">Disfruta este ajo negro con un recetario que te ayudara a sorprender amigos y familiares.</p>
                        <p class="pl-2 mt-5" style="font-size: 1.2rem; font-weight: 900;">Que llevarías:</p>
                        <div class="pl-4 mb-5">
                            <ul class="mb-3" style="color:black">
                                <li><b>140gr de Ajo Negro</b> puro $6.500.</li>
                                <li><b>100% Ajo Negro</b> sin conservantes.</li>
                                <li>Producido con Ajo cultivado en <b>Chile.</b></li>
                                <li>Listo para usar, no necesita cocción.</li>
                                <li>Recetario <b>Exclusivo</b> Kokorofoods Valor $3.000.</li>
                            </ul>
                            <div class="d-flex flex-column">
                                <p class="my-0" ><span style="text-decoration: line-through;">Antes: $9.500</span></p>
                                <p class="my-0" style="font-size: 1.5rem; font-weight: 700;">$6.500:</p>
                                <p class="mt-0" style="font-weight: 700;">+ despacho ($4.000)</p>
                            </div>
                        </div>
                    </div>
                </div>
                <!--Left content-->
                <div class="col-md-5 mb-1 order-md-2 order-2">
                    <div class="mb-0 pb-5" style="background-color: #F6F0EE;">
                        <div class="mt-0 mb-5" style="background-color: #D5441C;">
                        <p class="text-center text-white text-uppercase py-3 px-2" style="font-size: 1.8rem; font-weight: bold;">Aprovecha de llevarte este increible resetario gratis ($3.000)</p>
                        </div>
                        <form class="mt-5 px-4 pb-5 pt-3">
                        <input class="pl-5 mb-4 form-control form-control-lg" type="text" placeholder="Nombre" aria-label="Nombre">
                        <input class="pl-5 mb-4 form-control form-control-lg" type="text" placeholder="Apellido" aria-label="Apellido">
                        <input class="pl-5 mb-4 form-control form-control-lg" type="text" placeholder="Email" aria-label="Email">
                        <input class="pl-5 mb-4 form-control form-control-lg" type="text" placeholder="Telefono mobile" aria-label="Telefono mobile">
                        <input class="pl-5 mb-4 form-control form-control-lg" type="text" placeholder="Rut" aria-label="Rut">
                        <div class="d-flex flex-wrap">
                            <p class="col-2">Despacho</p>
                            <div class="col-10 mt-2" style="border-top: 2px solid black;"></div>
                        </div>
                        <div class="d-flex flex-wrap">
                            <input class="pl-5 mb-4 form-control form-control-lg" style="flex-basis: 100%;" type="text" placeholder="Calle" aria-label="Nombre">
                            <input class="pl-5 mb-4 form-control form-control-lg" style="flex-basis: 100%;" type="text" placeholder="Numero" aria-label="Nombre">
                            <input class="pl-5 mb-4 form-control form-control-lg" style="flex-basis: 100%;" type="text" placeholder="Comuna" aria-label="Nombre">
                        </div>
                        <div class="d-flex flex-wrap">
                            <div style="flex-basis: 49%; margin-right: 2%;" >
                                <input class="pl-5 form-control form-control-lg" type="text" placeholder="Region" aria-label="Nombre">
                                <p class="mt-5 mb-0" style="font-weight: 700;">Total con despacho</p>
                                <p style="font-size: 1.5rem; font-weight: 700;">$10.500</p>
                            </div>
                            <div  style="flex-basis: 49%;" >
                                <input class="pl-5 form-control form-control-lg" type="text" placeholder="Codigo postal" aria-label="Codigo postal">
                                <button type="button" class="mt-5 mb-0 text-uppercase btn btn-outline-dark">compar</button>
                            </div>

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
    auth: 'guest',
    data () {
        return {
            /*Title: '<span class="text-muted">Ajo negro de calidad,</span> <br>comprometidos con el medio ambiente.',
            Image_url: '/img/img-nosotros.jpg',
            Background_color: '#000000',
            title: '<span class="text-muted">Ajo negro</span><br>Ir al Catálogo ',
            bu_text: 'Ir al Catálogo',
            bu_link: '/productos',
            image_url: '/img/img-catalogo.jpg',
            image_url_mob: '/img/mobile/img-catalogo-1.jpg',
            class_section: 'ir-catalogo',
            title_mobile: 'Headline<span class="text-muted"><br>About Us</span>',*/
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
#omnisend-dynamic-container{
    display: none;
}
</style>
