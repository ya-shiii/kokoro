<template>
    <header>
  <div id="mySidebar" class="sidebar">
    
    <ul class="navbar-nav mr-auto">
      <li><a href="javascript:void(0)" class="closebtn" @click="closeNav">×</a></li>
      <li>
           <p>
               <!-- <button class="btn log-btn my-2 my-sm-0" 
                    type="submit" 
                    @click="GoAccount">
                    <img src="/img/Icons-icon-settings.svg" alt="">
                         Mi Cuenta
               </button> -->
               <nuxt-link class="btn log-btn my-2 my-sm-0 my-account" 
                    :to="Linkauth()">
                    <img src="/img/Icons-icon-settings.svg" alt="">
                         Mi Cuenta
               </nuxt-link>
          </p>
     </li>
     <li class="nav-item border-bottom active">
        <NuxtLink :to="localePath('/')" class="nav-link">{{ $t('menu.home') }}<span><img src="/img/path.svg" alt=""></span><span class="sr-only">(current)</span></NuxtLink>
      </li>
      <li class="nav-item border-bottom">
        <nuxt-link class="nav-link" :to="localePath('/nosotros')">{{ $t('menu.nosotros') }}<span><img src="/img/path.svg" alt=""></span></nuxt-link>
      </li>
      <li class="nav-item border-bottom">
        <NuxtLink :to="localePath('/ajonegro')" class="nav-link" tabindex="-1">{{ $t('menu.ajoNegro') }}<span><img src="/img/path.svg" alt=""></span></NuxtLink>
        <!-- <a class="nav-link" href="ajo.html" tabindex="-1">El Ajo Negro <span><img src="/img/path.svg" alt=""></span></a> -->
      </li>
      <li class="nav-item border-bottom">
        <NuxtLink class="nav-link" :to="localePath('/recetas')" tabindex="-1">{{ $t('menu.tipRecetas') }}<span><img src="/img/path.svg" alt=""></span></NuxtLink>
      </li>
      
      <li class="nav-item border-bottom">
          <NuxtLink class="nav-link" :to="localePath('/contacto')" tabindex="-1">{{ $t('menu.contacto') }}<span><img src="/img/path.svg" alt=""></span></NuxtLink>
    </li>
      <li class="nav-item border-bottom">
        <NuxtLink class="nav-link" :to="localePath('/productos')" tabindex="-1">{{ $t('menu.catalogo') }}<span><img src="/img/path.svg" alt=""></span></NuxtLink>
      </li>
      <li class="idioma-ic">{{$t('Footer.language')}} <div class="idiomas"><span><img src="/img/path.svg" alt=""></span>
        <button class="btn my-2 my-sm-0" :class="ESClass" @click="$i18n.setLocale('es')" :type="LanClass">esp</button>
        <button class="btn my-2 my-sm-0" :class="ENClass" :type="LanClass" @click="$i18n.setLocale('en')"> eng</button></div>
      </li>
    </ul>
  </div>
  
  <div id="main">
        <nav class="navbar navbar-light fixed-top bg-light openbtn">
          <button  @click="openNav" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <NuxtLink class="navbar-brand" :to="localePath('/')"><img src="/img/logo-nav.svg" alt=""></NuxtLink>
          <form class="form-inline mt-2 mt-md-0 search-fr">
            <img src="/img/search_nav.svg" alt="">
            <input class="form-control mr-sm-2" type="text" placeholder="" aria-label="Search">
            <button class="btn my-2 my-sm-0 log-btn" type="submit">Log In</button>
          </form>
          <button type="button" class="btn" @click="viewCart"><img src="/img/Icons-icon-shopping-bag.svg" alt=""> <span class="badge badge-success">{{ProductsinCart}}</span>
            <span class="sr-only">Artículos Carrito</span>
          </button>
        </nav>
  </div>
      
      </header>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      ESClass: "btn-outline-primary",
      ENClass: "log-btn",
    };
  },
  watch: {
    $route() {
      document.getElementById("mySidebar").style.width = "0";
      document.getElementById("main").style.marginLeft = "0";
    },
  },
  computed: {
    ...mapGetters("cart", ["ProductsinCart"]),
    LanClass() {
      const lang = this.$i18n.locale;
      if (lang == "en") {
        this.ESClass = "log-btn";
        this.ENClass = "btn-outline-primary";
        return "submit";
      } else {
        this.ESClass = "btn-outline-primary";
        this.ENClass = "log-btn";
        return "submit";
      }
    },
  },
  methods: {
    openNav: function () {
      document.getElementById("mySidebar").style.width = "400px";
      document.getElementById("main").style.marginLeft = "400px";
    },
    closeNav: function () {
      document.getElementById("mySidebar").style.width = "0";
      document.getElementById("main").style.marginLeft = "0";
    },
    viewCart: function () {
      this.$router.push(this.localePath("/carro"));
    },
    GoAccount: function () {
      this.$router.push(this.localePath("/register"));
    },
    Linkauth: function() {
      if (this.$auth.user){
        return this.localePath('/pedidos')
      } else {
        return this.localePath('/register')
      }
    }
  },
};
</script>

<style scoped>
.padd-sld-itm {
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin: 0;
}
.search-btn {
  margin: 0 0 0 15px;
}
.logos-nos {
  margin: 30px 0;
}
.sidebar {
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  z-index: 1000; /* Stay on top */
  top: 0;
  left: 0;
  background-color: #111; /* Black*/
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 60px; /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidebar */
}

.sidebar .closebtn {
  position: absolute;
  top: 60px;
  right: 25px;
  font-size: 70px !important;
  margin-left: 50px;
  text-decoration: none;
}

.openbtn {
  font-size: 20px;
  cursor: pointer;
  background-color: #111;
  color: white;
  padding: 10px 15px;
  border: none;
}

.openbtn:hover {
  background-color: #444;
}

#main {
  transition: margin-left 0.5s;
  transition: ease-in 0.5s;
  padding: 16px;
}

.sidebar {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 10000;
  top: 0;
  left: 0;
  background-color: #fff;
  overflow-x: hidden;
  overflow-y: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidebar a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.sidebar a:hover {
  color: #f1f1f1;
}

.navbar-light .navbar-toggler-icon {
  background-image: url(/img/menu.svg) !important;
  border: 0px solid !important;
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
  font-size: 1%;
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
.idiomas span img {
  transform: rotateZ(270deg);
}
.idioma-ic {
  display: -webkit-box;
  /* align-items: flex-end; */
  /* justify-content: space-around; */
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
.idiomas button {
  padding: 3px 20px !important;
  margin: 0 10px;
  text-transform: uppercase;
  font-size: 0.7em;
}
.idiomas {
  margin-top: 10px;
}
.idioma-ic p {
  margin: 10px 10px 0 0px;
}
.search-fr img {
  margin: 0 25px 0 0;
}
.search-fr button {
  padding: 5px 20px !important;
  text-transform: uppercase;
}
.my-account{
     width: 150px;
}
</style>