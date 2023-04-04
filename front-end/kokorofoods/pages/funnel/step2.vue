<template>
  <main role="main" class="bg-light-green">
    <section class="container col-md-12 section" v-if="!mobile">
      <!--Head content-->
      <div class="headcontent mx-auto">
        <p class="head1 text-center text-uppercase mb-0 py-0">
          Aprovecha el despacho <span class="head1span">gratis.</span>
        </p>
        <p class="head2 text-center text-uppercase mt-0 py-0 mb-0">
          Agregando una pasta de ajo negro
        </p>
      </div>
    </section>
    <section class="container col-md-12 section" v-if="!mobile">
      <div class="row p-0">
        <!--Right content-->
        <div class="col-md-7 pl-md-5 order-md-1 order-1">
          <div class="rightcontent mb-5">...</div>
          <div class="mb-4">
            <p class="right1">
              Disfruta este ajo negro con un recetario que te ayudara a
              sorprender amigos y familiares.
            </p>
            <h4 class="right2">Que llevarías:</h4>
            <span
              ><ul>
                <li>
                  <span class="right3">140gr de Ajo Negro </span>puro $6.500.
                </li>
                <li>
                  <span class="right4">100% Ajo Negro </span>sin conservantes.
                </li>
                <li>
                  Producido con Ajo cultivado en
                  <span class="right5">Chile.</span>
                </li>
                <li>Listo para usar, no necesita cocción.</li>
                <li>
                  Recetario <span class="right6">Exclusivo</span> Kokorofoods
                  Valor $3.000
                </li>
              </ul></span
            >
          </div>
          <div class="right7">
            <p class="right8"><del> Antes: $9.500 </del></p>
            <p class="right9">$23.500</p>
            <p class="right10" style="font-size: 16px; font-weight: 700">
              + despacho ($4.000)
            </p>
          </div>
        </div>

        <!--Left content-->
        <div class="col-md-5 mb-1 order-md-2 order-2">
          <div class="leftcontent mb-0 pb-0">
            <div class="left1 mt-0 mb-5">
              <p class="left2 text-center text-white text-uppercase py-3 px-2">
                Agrega una pasta y aprovecha despacho gratis
              </p>
            </div>
            <form class="mt-5 px-4 pb-5 pt-2">
              <div class="d-flex flex-wrap">
                <p class="left3 mb-4 pr-3">Ecoge tu ajo negro</p>
                <div class="left4 col-8"></div>
              </div>
              <div class="left5 pl-4 checkbox-container">
                <input class="mb-4 form-check-input" type="checkbox" />
                <p class="pl-3">Pasta de ajo negro 140gr</p>
                <input class="mb-4 form-check-input" type="checkbox" />
                <p class="pl-3">Pasta de ajo negro 140gr</p>
                <input class="mb-4 form-check-input" type="checkbox" />
                <p class="pl-3">Pasta de ajo negro con merken 140gr</p>
                <input class="mb-4 form-check-input" type="checkbox" />
                <p class="pl-3">Pasta de ajo negro con maqui 140gr</p>
                <input class="mb-4 form-check-input" type="checkbox" />
                <p class="pl-3">Pasta de ajo negro con miel de ulmo 140gr</p>
              </div>
              <div class="d-flex flex-wrap">
                <div class="left6">
                  <p class="left7 mt-5 mb-0">Total</p>
                  <p class="left8">$16.500</p>
                </div>
                <div class="mt-2">
                  <button
                    type="button"
                    class="mt-5 text-uppercase btn btn-outline-dark"
                  >
                    comprar
                  </button>
                </div>
              </div>
              <div class="pb-2 mt-0 mb-5 px-5 mr-0">
                <a href="" class="left9"
                  >No gracias, quiero pagar el despacho de $4.000</a
                >
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
  auth: "guest",
  data() {
    return {
      mobile: false,
    };
  },
  mounted: function () {
    if (screen.width < 769) {
      this.mobile = true;
    }
  },
};
</script>

<style scoped>
/* #omnisend-dynamic-container{
  display: none;
}

#omnisend-forms-container{
  display: none;
} */

.bg-light-green {
  background-color: #f3f5e6;
}

.main {
  background-color: #f3f5e6;
}

.headcontent {
  width: 100%;
}

.head1 {
  color: black;
  font-size: 3.5rem;
  font-weight: bold;
}

.head1span {
  color: #d5441c;
}

.head2 {
  font-size: 3rem;
  font-weight: smaller;
}

.rightcontent {
  background-color: #d9d9d9;
  width: 100%;
  height: 600px;
}

.right1,
.left5 {
  font-size: 1rem;
}

.right2,
.right3,
.right4,
.right5,
.right6 {
  font-weight: 700;
  color: #000000;
}

.right7 {
  margin-left: 30px;
}

.right8 {
  font-size: 16px;
  margin-bottom: 0;
}

.right9 {
  font-size: 35px;
  font-weight: 700;
  margin-bottom: 0;
}

.leftcontent {
  background-color: #f6f0ee;
  height: 105%;
}

.left1 {
  background-color: #d5441c;
}

.left2 {
  font-size: 1.8rem;
  font-weight: bold;
}

.left3 {
  font-size: 16px;
  font-weight: 700;
}

.left4 {
  border-top: 2px solid black;
  margin-top: 12px;
}

.left6 {
  flex-basis: 46%;
}

.left7 {
  font-weight: 700;
}

.left8 {
  font-size: 1.5rem;
  font-weight: 700;
}

.left9 {
  color: grey;
  text-decoration: underline !important;
  padding-left: 110px;
}
</style>