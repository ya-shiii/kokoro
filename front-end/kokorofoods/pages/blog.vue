<template>
    <main role="main">
        <section class="recetas container col-md-12">
        <div class="row featurette">
            <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading">{{blog.blog_title}}</span></h2>
            <img class="img-fluid separador" src="img/separador.svg" alt="separador">
            
            <div class="row info-block"> <!--row1-->
                <div class="col-md-6 descripcion row border-bottom-00">
                <img src="img/icons-16px-time.svg" class="" alt="">
                <p class="text-muted-in">Actualizado el {{blog.updated_at}}</p>
                
                <div class="share-box row">
                <div class="share-icons">
                    <img class="share" src="img/Icons-icon-share-filled.svg" alt="Compartir">
                    <img class="bookmark" src="img/Icons-icon-bookmark-filled.svg" alt="Favoritos">
                    </div>
                </div>
                </div>
                <div class="col-md-3">
                
                </div> 
                <div class="col-md-3">
                
                </div> 
            </div>
            <div class="row info-block"><!--row2-->
                <div class="col-md-12">
                <p>{{blog.blog_content}}</p>
                </div>
                
            </div>
            
            <p><NuxtLink :to="localePath('/tipsyrecetas')" class="btn btn-lg btn-primary">volver</NuxtLink></p>
            </div>
            <div class="col-md-5 order-md-1">
            <img v-for="image in blog.blog_images" :key="image" :src="image.image_url" class="img-fluid" alt="imagen blog">

            </div>
        </div>
        
        </section>
        <Thetipsyrecetas :blogsData="blogsData" />
        <TheStoreBuy :title="title"
                  :Button_text="bu_text"
                  :Image_URL="image_url"
                  :Button_link="bu_link"
                  :class_section="class_section"/>
    </main>
</template>
<script>
import axios from "axios";
export default {
  async asyncData({ $axios }) {
    const blogsData = await $axios.$get("/api/main/blog/");
    return { blogsData };
  },
  auth: "guest",
  data() {
    return {
      blog: [],
      title: '<span class="text-muted">Headline</span><br>Ir al Catálogo ',
      bu_text: "Ir al Catálogo",
      bu_link: "/catalogo",
      image_url: "img/img-catalogo.jpg",
      class_section: "ir-catalogo",
    };
  },
  async mounted() {
    try {
      console.log(this.$route);
      const response = await axios.get(
        `http://192.168.1.23:8000/api/main/blog/?id=${this.$route.params.id}`
      );
      this.blog = response.data.results[0];
    } catch (e) {
      console.log(e);
    }
  },
};
</script>
<style>
.info-block ul {
  list-style: none !important;
  padding: 0;
}
</style>