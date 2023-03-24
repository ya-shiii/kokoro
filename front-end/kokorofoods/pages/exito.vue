<template>
    <main role="main">
        <section class="p-0 m-0 col-lg-12 row mt-5">
            <div class="col-12 my-5 mx-auto">
            <h1 class="titulo-exito">Pedido Exitoso</h1>
            <div class="img-cont row col-12">
                <img src="/img/img-exito.jpg" class="img-fluid img-exito" alt="exito compra">
                <img src="/img/icon-ok-ex.svg" class="icon-ex" alt="">
            </div>
            <p class="texto-pedido center-itms">Tu Pedido <span class="num-ped">#{{order}}</span> fue tomado con éxito.
                <strong> Muchas Gracias por preferirnos, que tengas un buen día.</strong></p>
                <p class="texto-pedido center-itms">Te hemos enviado un email con toda la información de tu pedido</p>
                <NuxtLink :to="localePath('/productos')"><button class="btn btn-outline-primary my-2 my-sm-0 center-itms" type="submit">SALIR</button></NuxtLink>
                
            </div> 
        </section>
    </main>
</template>

<script>
export default {
    data () {
        return {
            order: this.$route.query.order,
            test: []
        }
    },
    head(){
        return {
            script: [{ type: 'text/javascript',
                        body: true,
                        defer: true,
                        innerHTML: `(function () {
                                    soicos.registerConversion({
                                    pid: '13211',
                                    data: "",
                                    trans: {
                                    orderID:` + this.order + `,
                                    store_name: 'Kokorofoods',
                                    total: ` + this.test.total_net + `,
                                    currency: "CLP",
                                    }
                                    });
                                    })();
                                    `}]
        }
    },

    mounted: function () {
            this.$axios.$get("/api/main/order/?order_number=" + this.$route.query.order).
            then(response => this.test = response.results[0])
            this.$gtm.push({ event: 'PurchasedSuccesful',
            UserID: this.$auth.user[0].id,
            order: this.order,
            total: this.test.total_net
          });
        },
}
</script>

<style>
h1.titulo-exito {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: center;
    justify-content: center;
    align-items: center;
}
img.img-fluid.img-exito {
    width: 75%;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: center;
    justify-content: center;
    align-items: center;
    margin: 15px auto;
}
img.icon-ex {
    width: 5%;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
}
.center-itms {
    width: 250px;
    display: block !important;
    margin: 20px auto;
    text-align: center;
}
</style>