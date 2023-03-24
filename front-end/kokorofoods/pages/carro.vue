<template>
  <section class="p-0 m-0 col-lg-12 row">
    <!-- MENU USUARIO IZQUIERDO -->
    <div class="info-left-carro col-lg-4 p-0">
      <!-- info-tienda -->
      <ul class="navbar-nav mr-auto usr-mn">
        <li class="nav-item border-bottom">
          <p>
            <strong>{{ $t("cart.personal") }}</strong>
          </p>
          <ul class="form-cont-usr p-0 center-itms">
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Nombre"
                aria-label="Search"
                v-model="user.first_name"
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Apellido"
                aria-label="Search"
                v-model="user.last_name"
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="email"
                placeholder="*Correo Electrónico"
                aria-label="Search"
                v-model="user.email"
              />
            </li>
          </ul>
          <p v-if="step == 'user'">
            <button class="btn btn-primary" type="submit" @click="SubmitForm">
              {{ $t("Buttons.continue") }}
            </button>
          </p>
          <p v-if="step == 'user'">
            <NuxtLink class="btn btn-secondary" role="button" :to="localePath('/productos')">{{ $t("Buttons.cont_buy") }}</NuxtLink>
          </p>
        </li>
        <li
          class="nav-item border-bottom"
          v-if="step == 'despacho' || step == 'payment'"
        >
          <p>
            <strong>{{ $t("cart.shipping") }}</strong>
          </p>
          <ul class="form-cont-usr p-0 center-itms">
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*RUT"
                aria-label="Search"
                v-model="address.rut"
                required
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Direccion"
                aria-label="Search"
                v-model="address.street"
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="Depto o numero de casa"
                aria-label="Search"
                v-model="address.number"
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Ciudad"
                aria-label="Search"
                v-model="address.city"
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Comuna"
                aria-label="Search"
                v-model="address.comuna"
                required/>
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Region"
                aria-label="Search"
                v-model="address.state"
                required/>
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="Codigo Postal"
                aria-label="Search"
                v-model="address.zipcode"
                required="false"
              />
            </li>
            <li>
              <input
                class="form-control mr-sm-2"
                type="text"
                placeholder="*Celular"
                aria-label="Search"
                v-model="address.mobile"
                required="true"/>
            </li>
          </ul>
          <div class="alert alert-danger" role="alert" v-if="message_form">
            {{message_form}}
          </div>
          <p>
            <button
              class="btn btn-primary"
              type="submit"
              @click="SubmitToPayment"
              v-if="step == 'despacho'"
            >
              {{ $t("Buttons.continue") }}
            </button>
          </p>
        </li>
        <li class="nav-item border-bottom" v-if="step == 'payment'">
          <p>
            <strong>{{ $t("cart.shipping_method") }}</strong>
          </p>
          <div v-for="ship in ShippinArray" :key="ship.id">
          <div class="envio-lista" v-if="ship.price == 0 && TotalPrice.subtotal > 18000 ">
              <input
                id="free"
                class="mt-0"
                type="radio"
                name="envio"
                :value="ship.price"
                aria-label="Tarjeta crédito"
                v-model="shipping"
                required
              />
              <p class="tipo-envio">{{ ship.description }}</p>
              <p class="precio" v-if="ship.price > 0">{{ ship.price }}</p>
              <p class="precio" v-if="ship.price == 0">Gratis</p>
          </div>
          <div class="envio-lista" v-if="ship.price > 0 ">
              <input
                id="cost s"
                class="mt-0"
                type="radio"
                name="envio"
                :value="ship.price"
                aria-label="Tarjeta crédito"
                v-model="shipping"
                required
              />
              <p class="tipo-envio">{{ ship.description }}</p>
              <p class="precio" v-if="ship.price > 0">{{ ship.price }}</p>
              <p class="precio" v-if="ship.price == 0">Gratis</p>
          </div>
          </div>
          <div v-if="TotalPrice.subtotal < 18000">
             <p>Agrega más productos y obten <strong>despacho gratis</strong> por compras superiores a 18 mil pesos </p>
             <p><NuxtLink class="btn btn-secondary" role="button" :to="localePath('/productos')">{{ $t("Buttons.cont_buy") }}</NuxtLink></p>
          </div>
        </li>
        <li class="nav-item border-bottom" v-if="step == 'payment' && GetCheckStore == 1">
          <p>
            <strong>{{ $t("cart.payment") }}</strong>
          </p>
          <p>
            <input
              class="mt-0"
              type="radio"
              value="1"
              name="pago"
              aria-label="Tarjeta crédito"
              v-model="payment_method"
            />
            <img src="/img/webpay_desktop.png" alt="" />
            Paga con tarjetas de credito o debito
          </p>
          <p>
            <input
              class="mt-0"
              type="radio"
              value="2"
              name="pago"
              aria-label="Tarjeta crédito"
              v-model="payment_method"
            />
            <img src="/img/Logo-khipu-oficial.png" alt="" />
            Paga con Kiphu
          </p>
          <p>
            <button
              class="btn btn-primary"
              type="submit"
              :disabled="check_shipping"
              @click="
                PayOrder({
                  address: address,
                  payment_method: payment_method,
                  user_id: getUser,
                })
              "
            >
              {{ $t("Buttons.pay") }}
            </button>
          </p>
        </li>
        <li class="nav-item border-bottom" v-if="step == 'payment' && GetCheckStore == 2">Sorry we are not ready yet</li>
      </ul>
    </div>
    <!-- MENU USUARIO DERECHO -->
    <div class="info-right col-lg-8 p-0 usuario-der">
      <div class="row featurette pr-5 pl-5">
        <div
          class="pedido pt-5 pr-2 pl-2 pb-0 border-bottom col-12 row center"
        ></div>
      </div>
      <!-- user id - menu -->
      <div class="pedidos col-12 mt-3 mb-3 p-0">
        <ul class="navbar-nav p-3">
          <li
            class="nav-item border-bottom active p-3 m-0 col-12"
            v-for="item in CartProducts"
            :key="item.product.id"
          >
            <div class="col-12 p-0 m-0 row">
              <div class="col-6 p-0 mt-0 mb-0 center-itms">
                <img
                  :src="Img_product(item.product.product_images)"
                  :alt="item.product.name"
                  class="img-art-pedidos cart_img"
                />
              </div>
              <div class="col-6 p-0 mt-0 mb-0">
                <div class="col-8 articulo row">
                  <div class="col-12">
                    <p class="n-articulo">{{ item.product.name }}</p>
                    <div class="precio-oferta col-12 cantidad-info">
                      <p class="cantidad">x{{ item.quantity }}</p>
                      <a
                        href="#"
                        @click="PlusOne({ plus: false, itemTo: item })"
                      >
                        <div class="ico-mas">
                          <img src="/img/icon-menos.svg" alt="" />
                        </div>
                      </a>
                      <a href="#" @click="PlusOne({ plus: true, itemTo: item })"
                        ><div class="ico-mas">
                          <img src="/img/icon-mas.svg" alt="" /></div
                      ></a>
                      <h4>
                        <span
                          ><strong>${{ item.product.price }}</strong></span
                        >
                      </h4>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item border-bottom active p-3 m-0 col-12">
            <div class="col-12 p-0 m-0 row">
              <div class="col-6 p-0 mt-0 mb-0 center-itms"></div>
              <div class="col-6 p-0 mt-0 mb-0">
                <div class="col-8 articulo row">
                  <div class="col-12 p-0">
                    <div class="precio-oferta col-12 cantidad-info">
                      <div class="table-price col-12">
                        <p class="subtotal pr-3">{{ $t("cart.Subtotal") }}</p>
                        <h4>
                          <span>${{ TotalPrice.subtotal }}</span>
                        </h4>
                        <br />
                      </div>
                      <div class="table-price col-12 border-bottom">
                        <p class="envio pr-3">{{ $t("cart.cost_shipping") }}</p>
                        <h4>
                           <span>${{ TotalPrice.shipping }}</span>
                        </h4>
                      </div>
                      <div class="table-price col-12">
                        <p class="total pr-3 pt-2">
                          {{ $t("cart.total_cost") }}
                        </p>
                        <h4>
                          <span>
                               <strong>${{ TotalPrice.total }}</strong></span>
                        </h4>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  auth: "guest",
  data() {
    return {
      user: {
        first_name: null,
        last_name: null,
        email: null,
        password: "Koko09User",
      },
      ShippinArray: [],
      address: {
        street: null,
        number: null,
        comuna: null,
        city: null,
        state: null,
        zipcode: null,
        rut: null,
        mobile: null
      },
      step: "user",
      payment_method: null,
      shipping: null,
      userid: null,
      message_form: null
    };
  },
  computed: {
    ...mapGetters("cart", ["CartProducts", "TotalPrice", "GetCheckStore"]),
    ...mapGetters(["Showshipping"]),
    getUser() {
      return this.$auth.user[0].id;
    },
    check_shipping() {
      if (this.shipping == null || this.payment_method == null) {
        return true
      } else {
        return false
      }
    }
  },
  
  methods: {
    ...mapActions("cart", ["PlusOne", "PayOrder"]),
    async SubmitForm() {
      if (!this.$auth.loggedIn) {
        let response = await this.$axios
          .$post("/api/user/create/", this.user)
          .catch(({ response }) => {
            if (response.status == 400) {
              let login_res = this.$auth
                .loginWith("local", { data: this.user })
                .then(() => {

                  this.userid = this.$auth.user[0].id;
                });
            }
          });
          let login_res = await this.$auth
                .loginWith("local", { data: this.user })
                  this.userid = this.$auth.user[0].id;
      }
       this.userid = this.$auth.user[0].id;
       this.$gtm.push({ event: 'identify', user_id: this.userid,
                            name: this.$auth.user[0].first_name + " " + this.$auth.user[0].last_name,
                            email: this.$auth.user[0].email
                          });
      let add_res = await this.$axios.$get("/api/main/address/", {
        params: { user: this.userid },
      });
      try {
        this.address.street = add_res.results[0].street;
        this.address.number = add_res.results[0].number;
        this.address.comuna = add_res.results[0].comuna;
        this.address.city = add_res.results[0].city;
        this.address.state = add_res.results[0].state;
        this.address.zipcode = add_res.results[0].zipcode;
        this.address.rut = add_res.result[0].rut;
      } catch (error) {
        console.log(error);
      }
      this.step = "despacho";
    },
    async SubmitToPayment() {
      if (!this.address.street || !this.address.number || !this.address.comuna
      || !this.address.city || !this.address.state || !this.address.mobile || !this.address.rut){
        this.message_form = 'Ingrese todo los campos'
      } else {
      var payload = this.address;
      payload.user = this.$auth.user[0].id;
      // let response = await this.$axios.$post("/api/main/address/", payload);
      let Shipping = await this.$axios.$get("/api/main/shipping/");
      this.ShippinArray = Shipping.results;
      this.step = "payment";
      this.message_form = null;
      this.$gtm.push( { event:'ContToShipping',
            comuna: this.address.comuna,
            city: this.address.city
          });
    }},
    Img_product(images) {
      for (var i = 0; i < images.length; i++) {
        if (images[i].type == "main") {
          var url = images[i].image_url;
        }
      }
      return url;
    },
  },
  watch: {
    shipping: function() {
      this.$store.dispatch("cart/AddShipping", this.shipping)
    }
  },
};
</script>

<style>
.alert {
  font-size: 90%;
}
.cart_img {
  width: 55%;
}
.info-left-carro {
  background-color: #f6f0ee;
}
.navbar-nav {
  padding-top: 10%;
  padding-left: 20% !important;
  padding-right: 10%;
}
.navbar-nav .nav-link {
  padding-right: 0;
  padding-left: 0;
  padding-top: 20px !important;
}

.badge-success {
  color: #000 !important;
  background-color: #cbd402 !important;
  border-radius: 100% !important;
  letter-spacing: 0px;
}
.nav-item {
  /* width: 25%; */
  padding: 2% 0%;
  /* font-size: 1%; */
}
.nav-link {
  display: block;
  padding: 0.5rem 1rem;
  font-size: 0.9rem !important;
  font-weight: 300;
  color: #000 !important;
}
.nav-link span {
  float: right;
  transform: rotateZ(270deg);
}
.navbar-toggler {
  border: 0px solid #fff !important ;
}
.border-bottom-00 {
  border-bottom: 1px solid #000 !important;
  margin: 20px 0;
  padding: 10px 0 10px 0 !important;
}

.envio-lista {
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: space-around;
  flex-wrap: nowrap;
}
.left-it {
  border-right: 1px solid #000;
  padding: 0 15px 0 0 !important;
}
.datos-art-dest {
  padding: 0 !important;
  margin: 20px 0 !important;
}
.datos-art-dest p {
  font-weight: 800;
}
.promo-align {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.btn-suscripcion {
  display: flex;
  justify-content: space-evenly;
  flex-direction: row;
  align-content: center;
  align-items: center;
  margin: 0;
}
.btn-suscripcion img {
  margin: 0 10px;
}
.alerta-suscripcion {
  background-color: #d5441c;
}
.pedidos {
  width: 100%;
  margin: 0 auto;
}
h3.precio-oferta {
  color: #000;
  font-size: 2.5em;
  font-weight: 600;
}
.precio-oferta h3 {
  color: #000;
  font-size: 1.5rem;
  font-weight: 600;
}
.precio-oferta {
  padding-left: 0 !important;
  padding-right: 0 !important;
}
p.cantidad {
  background-color: #cbd402;
  padding: 5px 10px;
}
.cantidad-info {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
  justify-content: space-between;
  align-items: flex-start;
}
.ico-mas {
  float: left;
  margin: 5px 0px 5px 15px;
}
.articulo-des {
  font-weight: 300 !important;
}
.articulo {
  padding: 10px !important;
  margin: 0 !important;
  padding: 5px 0;
}
.precio strong {
  color: #000;
}
.seg-row > .datos-art > .precio strong {
  color: #fff;
}
.seg-row > .datos-art > .n-articulo {
  font-size: 1.1rem !important;
  color: #fff;
}
.seg-row > .datos-art > .n-articulo span {
  font-size: 1.1rem !important;
  color: #fff;
  font-weight: 200;
}
.n-articulo {
  font-size: 1.1rem !important;
  color: #000;
}
.n-articulo span {
  font-size: 1.1rem !important;
  color: #000;
  font-weight: 200;
}
.center-itms {
  width: 250px;
  display: block !important;
  margin: 20px auto;
  text-align: center;
}
.center-itms-list {
  width: 400px;
  display: block !important;
  margin-bottom: 25px;
  margin-top: 25px;
  margin: 25px auto;
  text-align: center;
  list-style: none;
}
.table-price {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
  justify-content: flex-end;
  align-items: center;
}
.form-cont-usr li {
  background-color: #fff0 !important;
  list-style: none;
  margin: 20px auto;
  text-align: center;
  border-bottom: 1px solid #000;
}
.form-cont-usr input {
  background-color: #fff0;
  border: 0px solid;
  text-align: center;
  color: #000 !important;
}
.center-itms {
  width: 250px;
  display: block !important;
  margin: 20px auto;
  text-align: center;
}
</style>