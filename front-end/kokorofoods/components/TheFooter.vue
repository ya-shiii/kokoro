<template>
    <div>
        <footer class="container-fluid py-5 bg-dark-footer footer">
        <div class="row col-12 col-md">
            <div class="col-4 col-md">
            <p class="p-logo"><img src="/img/logo-kokoro-wt.svg" alt="" class="img-fluid logo-foot"></p>
            <p class="p-logo"><img src="/img/logo-kumkare-wt.svg" alt="" class="img-fluid align-middle logo-foot"></p>
            <ul class="list-unstyled text-small">
                <li><p class="text-center"> © 2021, Kokorofoods</p></li>
                <li class="border-bottom"><p class="text-center">{{$t('Footer.about')}}</p></li>
                <li><h2>{{$t('Footer.Redes')}}</h2></li>
                <li class="icons_rrss"><a class="text-muted" href="https://www.facebook.com/kokorofoodsChile/?ref=br_rs"><img src="/img/logotipo-circular-de-facebook.svg" alt="" ><span>@kokorofoodsChile</span></a></li>
                <li class="icons_rrss"><a class="text-muted" href="https://twitter.com/ajonegro_chile"><img src="/img/logo-twitter.svg" alt="" ><span>@AjoNegro_Chile</span></a></li>
                <li class="icons_rrss"><a class="text-muted" href="https://www.instagram.com/ajo_negro_chile/"><img src="/img/logo-instagram.svg" alt="" ><span>@ajo_negro_chile</span></a></li>
                <li></li>
            </ul>
            </div>
            <div class="col-4 col-md">
            <ul class="list-unstyled text-small">
                <li><h3>{{$t('Footer.Newsletter_title')}}</h3></li>
                <li><p>{{$t('Footer.Newsletter_body')}}</p></li>
                <li><input class="form-control mr-sm-2" type="text" placeholder="Tu correo electrónico" aria-label="Search"></li>
                <li class="border-bottom"><button class="btn btn-outline-secondary my-2 my-sm-0" type="submit">{{ $t('Buttons.Sent')}}</button></li>
                <li><h3>{{$t('Footer.PuntosVentas_title')}}</h3></li>
                <li class="border-bottom"><button class="btn btn-outline-secondary my-2 my-sm-0" type="submit" @click="Stores">{{$t('Buttons.SalesPoint')}}</button></li>
                <li><h3>{{$t('Footer.Supported_by')}}</h3></li>
                <li><img src="/img/Apoyado-por.png" alt="apoyan"></li>
            </ul >
            </div>
            <div class="col-4 col-md">
            <ul class="list-unstyled text-small">
                <li><p>{{$t('Footer.language')}} <span><img src="/img/path.svg" alt=""></span><span class="idioma">
                    <button class="btn my-2 my-sm-0"  :class="css_langES" @click="$i18n.setLocale('es')" :type="LanClass">esp</button></span><span class="idioma">
                    <button class="btn my-2 my-sm-0" :class="css_langEN" @click="$i18n.setLocale('en')" :type="LanClass"> eng</button></span></p></li>
                <li><h3>{{$t('Footer.contact_info')}}</h3></li>
                <li><p>{{$t('Footer.contact_body')}}</p></li>
                <li class="border-bottom"><button class="btn btn-outline-secondary my-2 my-sm-0" type="submit" @click="Contacto">{{$t('Buttons.ContactUS')}}</button></li>
                <li><h3>{{$t('Footer.qainfo')}}</h3></li>
                <li><button class="btn btn-outline-secondary my-2 my-sm-0" type="submit">{{$t('Buttons.qaButton')}}</button></li>
                <li><NuxtLink :to="localePath('/politica-privacidad')">Politica de Privacidad</NuxtLink></li>
                 <li><NuxtLink :to="localePath('/politica-envios')">Politica de despachos</NuxtLink></li>
            </ul>
            </div>
            
        </div>
        
        </footer>
        <div class="formas-pago row">
            <div class="col-md-1">
                
            </div>
            <div class="col-md-10 row">
                
                <ul class="list-group list-group-horizontal lista-pago">
                <li class="list-group-item"><h3>{{$t('Footer.Payment_title')}}</h3></li>
                <li class="list-group-item"><p>{{$t('Footer.Payment_body')}}</p></li>
                <li class="list-group-item"><img class="" src="/img/pago-icons.svg" alt=""></li>
                </ul>
            </div>

            <div class="col-md-1">
                
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    data () {
        return {
            css_langES: 'btn-outline-primary',
            css_langEN: 'btn-outline-secondary',
            lang: this.$i18n.locale
        }
    },
    methods: {
        Contacto(){
            this.$router.push(this.localePath('/contacto'))
        },
        Stores(){
            this.$router.push(this.localePath('/tiendas'))
        }
    },
    computed: {
        LanClass() {
            const lang = this.$i18n.locale
            if (lang == 'en'){
                this.css_langES = 'btn-outline-secondary'
                this.css_langEN = 'btn-outline-primary'
                return "submit"
            } else {
                this.css_langES = 'btn-outline-primary'
                this.css_langEN = 'btn-outline-secondary'
                return "submit"
            }
        }
    }
}
</script>

<style>
.footer .btn-outline-primary {
    color: #fff !important;
    border-color: #fff !important;
    background-color: #fff !important;
    color: #000 !important;
}
.footer p, .footer a{
    color: #fff !important;
    font-size: 0.9em;
    font-weight: 100;
}
.icons_rrss img{
    margin: 0 15px 0 0;
}
.icons_rrss{
    margin: 15px 0 0 0;
}
.btn-outline-secondary {
    color: #fff !important;
    border-color: #fff !important;
}
.log-btn {
    color: #000 !important;
    border-color: #000 !important;
}
.info-text div{
    display: flex;
}
.footer button{
    margin: 10px 0 20px !important;
    padding: 10px 25px;
    font-size: 0.8em;
    text-transform: uppercase;
}
.footer h2 {
    color: #fff;
    font-size: 3.1vh;
    font-weight: 200;
    padding: 30px 0 15px 0;
}
.footer h3 {
    color: #fff;
    font-size: 1.3em;
    font-weight: 400;
    padding: 15px 0 0 0;
}
.footer input{
    margin: 30px 0 15px 0;
    
}
.logo-foot {
    width: 50%;
    margin: 0 auto;
}
.p-logo{
    display: flex;
}
.lista-pago{
    margin: 0 auto;
}
.lista-pago h3
{
    font-size: 1.3em;
    font-weight: 400;
    color: black;
    padding-top: 30px;

}
.lista-pago p
{
    font-size: 0.9em;
    font-weight: 100;
    color: black;
    padding-top: 30px;
}
span.idioma {
    padding: 6px;
}

.bg-dark-footer {
    background-color: #000 !important;
}
</style>