<template>
  <div class="bg-light-green pt-5">
    <div class="pl-2 pr-2 pt-3" v-if="!mobile">
      <div class="head mx-auto">
        <div class="mb-4">
          <p class="ng text-uppercase mb-0 py-0 text-center">
            <span style="color: #d5441c">24% de descuento</span> En Sal Con Ajo
          </p>
          <p class="ng text-uppercase mb-0 py-0 text-center">Negro</p>
        </div>
        <p class="agr text-uppercase mt-0 mb-5 py-0 text-center">
          Agregando una pasta de ajo negro
        </p>
      </div>
    </div>
    <div class="py-0" v-if="!mobile">
      <div class="d-flex justify-content-center">
        <div>
          <div class="gray-box"></div>
        </div>
      </div>
    </div>
    <div class="py-0 mt-5" v-if="!mobile">
      <div class="cont d-flex justify-content-left">
        <div>
          <p class="text-start">
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
        <div class="text-left">
          <div>
            <p class="p1 mt-5 mb-0"><del> Antes: $9.500 </del></p>
          </div>
          <div>
            <p class="p2 mb-0">$23.500</p>
          </div>
          <p class="p3">+ despacho ($4.000)</p>
        </div>
        <div>
          <button
            type="button"
            class="mt-5 mb-0 px-5 py-3 rounded text-uppercase comprar-btn"
          >
            compar
          </button>
        </div>
        <div class="pb-2 pt-4 mb-5">
          <a href="" class="note"
            >No gracias, quiero pagar el despacho de $4.000</a
          >
        </div>
      </div>
    </div>
  </div>
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

.bg-light-green {
  background-color: #f3f5e6;
}

.head {
  width: 100%;
}
.gray-box {
  background: #d9d9d9;
  height: 429px;
  width: 949px;
}

.ng {
  font-weight: 700;
  font-size: 55px;
  line-height: 63px;
}
.agr {
  font-weight: 300;
  font-size: 46px;
  line-height: 53px;
  color: #000000;
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

.note {
  text-decoration: underline !important;
  font-weight: 500;
  font-size: 12px;
  line-height: 15px;
  color: #7e7c7c;
  width: fit-content;
}

.comprar-btn {
  font-weight: 700;
  font-size: 16px;
  line-height: 18px;
  color: #000000;
  background: none;
}

@media only screen and (max-width: 1023px) {
  .gray-box {
    height: 300px;
    width: 100%;
  }
}
</style>