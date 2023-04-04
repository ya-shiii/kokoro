<template>
  <main role="main" class="bg-light-green">
    <section class="pl-2 pr-2" v-if="!mobile">
      <div class="head mx-auto">
        <p class="ng text-uppercase mb-0 py-0 text-center">
          <span style="color: #d5441c">24% de descuento</span> En Sal Con Ajo
        </p>
        <p class="ng text-uppercase mb-0 py-0 text-center">Negro</p>
        <p class="agr text-uppercase mt-0 py-0 text-center">
          Agregando una pasta de ajo negro
        </p>
      </div>
    </section>
    <section class="py-0" v-if="!mobile">
      <div class="d-flex justify-content-center">
        <div>
          <div class="gray-box"></div>
        </div>
      </div>
    </section>
    <section class="py-0" v-if="!mobile">
      <div class="cont d-flex justify-content-left">
        <div>
          <p class="text-start mt-5">
            Disfruta este ajo negro con un recetario que te ayudará a sorprender
            amigos y familiares.
          </p>
          <h4 class="lstd">Qué llevarías:</h4>
          <span
            ><ul class="pad">
              <li><span class="lstd">140gr de Ajo Negro</span> puro $6.500.</li>
              <li>
                <span class="lstd">100% Ajo Negro</span> sin conservantes.
              </li>
              <li>
                Producido con Ajo cultivado en <span class="lstd">Chile.</span>
              </li>
              <li>Listo para usar, no necesita cocción.</li>
              <li>
                Recetario <span class="lstd">Exclusivo</span> Kokorofoods Valor
                $3.000
              </li>
            </ul></span
          >
        </div>
      </div>
      <div class="d-flex flex-column justify-content-center align-items-center">
        <div>
          <p class="p1 mt-5 mb-0"><del> Antes: $9.500 </del></p>
        </div>
        <div>
          <p class="p2 mb-0">$23.500</p>
        </div>
        <p class="p3">+ despacho ($4.000)</p>
        <div>
          <button
            type="button"
            class="mt-5 mb-0 text-uppercase btn btn-outline-dark"
          >
            compar
          </button>
        </div>
        <div class="pb-2 pt-4 mb-5">
          <a href="" class="btn"
            >No gracias, quiero pagar el despacho de $4.000</a
          >
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
/* #omnisend-forms-container {
  display: none;
} */
main {
  min-height: calc(100vh - 100px);
  /* Set the minimum height of the main section to be the height of the viewport minus the height of the footer */
  background-color: #f3f5e6;
}

.bg-light-green {
  background-color: #f3f5e6;
}

.head {
  width: 100%;
}
.gray-box {
  background-color: grey;
  height: 429px;
  width: 949px;
}

.ng {
  color: black;
  font-size: 3.5rem;
  font-weight: bold;
}
.agr {
  font-size: 3rem;
  font-weight: smaller;
}

.cont {
  margin-left: 15%;
  margin-top: 30px;
}

.lstd {
  font-weight: 700;
  color: #000000;
}

.pad {
  padding-left: 40px;
}
.p1 {
  font-size: 16px;
}

.p2 {
  font-size: 35px;
  font-weight: 700;
}

.p3 {
  font-size: 16px;
  font-weight: 700;
}

.btn {
  color: grey;
  text-decoration: underline !important;
}

@media only screen and (max-width: 1023px) {
  .gray-box {
    height: 300px;
    width: 100%;
  }
}
</style>
