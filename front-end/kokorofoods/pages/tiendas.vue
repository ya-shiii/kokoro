<template>
     <div>
          <section class="info-ajo container col-md-12 section">
               <LazyTheHeaderOP
               :title="Title"
               :image="Image_url"
               :background="Background_color"
               v-if="!mobile"
               />
               <LazyMobileTheHeaderOPMob :title="Title" v-if="mobile" />
          </section>
          <section class="tienda-table container table-responsive-sm">
               <div class="form-group">
                  <input class="form-control" v-model="searchQuery" type="text" :placeholder="$t('store.search')">
                </div>
               <table class="table table-striped">
                    <thead>
                    <tr>
                         <th scope="col">Tienda</th>
                         <th scope="col">Direccion</th>
                         <th scope="col" v-if="!mobile">Telefono</th>
                         <th scope="col">Website</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="tienda in filteredResources" :key=tienda.id>
                         <th scope="row">{{tienda.nombre}}</th>
                         <td>{{tienda.direccion}}</td>
                         <td v-if="!mobile">{{tienda.telefono}}</td>
                         <td><a :href="tienda.website"> {{tienda.website}}</a></td>
                    </tr>
                    
                    </tbody>
               </table>
          
          </section>         
     </div>
</template>

<script>
export default {
     auth: "guest",
     data () {
        return {
        Title: this.$t('store.title'),
        Image_url: '/img/tips.jpg',
        Background_color: "#000000",
        page: 1,
        mobile: false,
        lang: this.$i18n.locale,
        searchQuery: null
        }
    },
     async asyncData({ $axios }) {
          const tiendaData = await $axios.$get("/api/main/tiendas/");
          return { tiendaData };
  },
     computed: {
          filteredResources (){
               if(this.searchQuery){
               return this.tiendaData.filter((item)=>{
               return item.direccion.includes(this.searchQuery);
               })
               }else{
               return this.tiendaData;
               }
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
@import '~/assets/css/mobile.css';
.tienda-table {
    padding-left: 80px !important;
    padding-right: 80px !important;
  }
</style>