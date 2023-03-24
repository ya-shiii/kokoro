<template>
    <main role="main">
         <section class="informacion container col-md-12">
        <div class="row featurette">
          <div :class="{'col-3 order-md-1': !mobile, 'col-12':mobile}">
            <h2 class="featurette-heading">Escríbenos<span class="text-muted"><br>
                Contacto</span></h2>
            <img class="img-fluid separador" src="/img/separador.svg" alt="separador">
            <div v-if="!mobile">
                <p>{{ $t('Contacto.main-blurb')}}</p>
                <ul class="list-unstyled text-small ico-cont">
                    <li class="icons_rrss"><a class="text-muted" href="#"><img src="/img/logotipo-circular-de-facebook.svg" alt="" ><span>@kokorofoodsChile</span></a></li>
                    <li class="icons_rrss"><a class="text-muted" href="#"><img src="/img/logo-twitter.svg" alt="" ><span>@AjoNegro_Chile</span></a></li>
                    <li class="icons_rrss"><a class="text-muted" href="#"><img src="/img/logo-instagram.svg" alt="" ><span>@ajo_negro_chile</span></a></li>
                </ul>
            </div>
          </div>
          <div :class="{'col-9 order-md-2': !mobile, 'col-12': mobile}" >
            <form @submit.prevent="Contactform" method="POST">
            <ul class="form-cont" :class="{'p-0': mobile }">
                <li><input class="form-control mr-sm-2" type="text" v-model="motivo" placeholder="Motivo" aria-label="Search"></li>
                <li><input class="form-control mr-sm-2" type="text" v-model="nombre" placeholder="Nombre" aria-label="Search"></li>
                <li><input class="form-control mr-sm-2" type="text" v-model="email" placeholder="Correo Electrónico" aria-label="Search"></li>
                <li><input class="form-control mr-sm-2" type="text" v-model="mensaje" placeholder="Mensaje" aria-label="Search"></li>
                <button class="btn btn-primary my-2 my-sm-0 float-right" type="submit"> Enviar</button>
            </ul>
            </form>
          </div>
        </div>
        
    </section>
    </main>
</template>
<script>
import axios from 'axios'
export default {
    auth: 'guest',
    data () {
        return {
            motivo: '',
            nombre: '',
            mensaje: '',
            email: '',
            mobile:false
        }
        
    },
    methods: {
        Contactform(){
            let params ={motivo:this.motivo, 
                        nombre:this.nombre, 
                        email:this.email,
                        mensaje:this.mensaje}
            axios.post(
                '/api/main/contacto/', params
            )
            .then(response=>{
                 if (response.status == '201') {
                    alert("Mensaje enviado correctamente");
                    this.motivo= '';
                    this.nombre= '';
                    this.mensaje= '';
                    this.email= '';
                }
            })
            .catch(error => {
                console.log(error.response.data)
               alert("Porfavor revise los campos");
            })
        }
    },
    mounted: function() {
      if (screen.width < 769 ){
        this.mobile = true
      }
    }
   
}
</script>
<style scoped>
@import '~/assets/css/mobile.css';
.icons_rrss img{
    margin: 0 15px 0 0;
}
.icons_rrss{
    margin: 15px 0 0 0;
}
.form-cont li {
    background-color: #fff0 !important;
    list-style: none;
    margin: 35px auto;
    text-align: center;
    border-bottom: 1px solid #000;
}
.form-cont input {
    background-color: #fff0;
    border: 0px solid;
    text-align: center;
    color: #000 !important;
}
</style>