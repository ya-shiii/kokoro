<template>
<main class="main">
    <section class="p-0 m-0 col-lg-12 row">
        <div class="info-left col-lg-6 p-0">
        <img src="/img/img-creacion-usuario.jpg" alt="" class="img-fluid">
        </div>
        <div class="info-right col-lg-6 p-0">
        <div class="col-12 flex-column center-itms mt-3">
            <img src="/img/logos-juntos.svg" alt="" class="center-itms">
            <h4 class="featurette-heading titulo-login center-itms">¡Comencemos!</h4>
            <p class="center-itms">{{$t('Register.main_title')}}</p>
        </div>
        <div class="col-12 center-itms">
            <ul class="form-cont-usr p-0 center-itms">
                <li><input class="form-control mr-sm-2" type="email" placeholder="*Email" aria-label="Email" v-model="email"></li>
                <li v-if="message"> <p> {{message}} </p></li>
                <li v-if="email_sent"><input class="form-control mr-sm-2" type="text" placeholder="*Codigo" aria-label="Email" v-model="code"></li>
                <button class="btn btn-primary center-button-2" type="submit" @click="EnviarMail" v-if="!message">Ingresar</button>
                <div class="alert alert-danger" v-if="alert">¡Error! El codigo no es valido.</div>
                <button class="btn btn-primary center-button-2" type="submit" @click="Validar" v-if="message">validar codigo</button>
            </ul>
        </div>
        </div>
    </section>
</main>
    
</template>

<script>
export default {
    auth: 'guest',
    data (){
        return {
            email: null,
            code: null,
            email_sent: false,
            message: null,
            alert: false
        }
    },
    methods: {
        async EnviarMail(){
            let response = await this.$axios.$get('/api/main/botonIniciarSesion/' + this.email)
            this.message = response
            this.email_sent = true
        },
        async Validar(){
            let response = await this.$axios.$get('/api/main/logear/' + this.email + '/' + this.code +'/' )
            if (response == 'Exito') {
                let login_res = await this.$auth.loginWith("local", { data: {'email': this.email, 'password': 'Koko09User'} })
            } else {
                this.alert = true
            }
        }
    }

}
</script>

<style scoped>
@import '~/assets/css/user.css';
</style>