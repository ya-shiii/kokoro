<template>
    <div>
<!-- Seccion de recetas  -->
<section class="recetas container col-md-12" v-if="!mobile">
  <div class="row featurette">
    <div class="col-md-7 order-md-2">
      <h2 class="featurette-heading">{{RecipeData.receta.recipe_title}}</h2>
      <img class="img-fluid separador" src="/img/separador.svg" alt="separador">

      <div class="row info-block"> <!--row1-->
        <div class="col-md-4 row">
        <p><img src="/img/icons-16px-time.svg" alt="" class="ico-time"></p>
        <p>{{$d(new Date(RecipeData.receta.created_at), 'short')}}</p>
        </div>
        <div class="col-md-4">
          <div class="share-box row share-recipe">
            <img class="img-fluid share" src="/img/Icons-icon-share-filled.svg" alt="Compartir">
            <img class="img-fluid bookmark" src="/img/Icons-icon-bookmark-filled.svg" alt="Favoritos">
            </div>
        
        </div>
        <div class="col-md-4">
        
        </div> 
      </div>
      <div class="row info-block"><!--row2-->
        <div class="col-md-4 row table-border-left">
        <p>Tiempo</p><span>{{RecipeData.receta.recipe_time}} minutos</span>
        </div>
        <div class="col-md-4 row table-border">
          
        <p>Porciones</p><span>{{RecipeData.receta.recipe_portions}} personas</span>
        
        </div>
        <div class="col-md-4">
        
        </div> 
      </div>
      <div class="row info-block"><!--row3-->
        <div class="col-md-4 row">
          <h4 class="n-articulo borde-abajo">Ingredientes</h4>
          <hr>
        </div>
        <div class="col-md-4 row">
          <div v-html="RecipeData.receta.recipe_ingredients">
        </div>
        </div>
        <div class="col-md-4">
        
        </div> 
      </div>
      <div class="row info-block"><!--row4-->
        <div class="col-md-12 row">
          <h4 class="n-articulo borde borde-abajo">Preparación</h4>
        </div>
        <div class="note" v-html="RecipeData.receta.recipe_preparation"></div>
        </div>
      
      <p><NuxtLink class="btn btn-lg btn-primary" :to="localePath('/recetas')">volver</NuxtLink></p>
    </div>
    <div class="col-md-5 order-md-1">
      <img class="img-fluid" :src="RecipeData.receta.recipe_images[0].image_url" :alt="RecipeData.receta.recipe_title">

    </div>
  </div>
  
</section>
<section class="info-contenido container col-12 section-slider seccion" v-if="mobile">
  <div class="row featurette">
    <div class="col-12  right-col">
        <img class="img-fluid" :src="RecipeData.receta.recipe_images[0].image_url" :alt="RecipeData.receta.recipe_title">
    </div>
    <NuxtLink class="btn btn-lg btn-secondary float-btn-2 btn-light" :to="localePath('/recetas')"> volver</NuxtLink>
  </div>
  <div class="info-text info-cont-mob">
    <img src="/img/mobile/top-seccion-img.jpg" alt="" class="top-img-secc">
    <div class="col-12 p-0">
      <h2 class="featurette-heading">{{RecipeData.receta.recipe_title}}</h2>
    </div>
    <div class="col-12 p-0 mt-2 row">
      <p><img src="/img/icons-16px-time.svg" alt="" class="ico-time"></p>
      <p>{{$d(new Date(RecipeData.receta.created_at), 'short')}}</p>
    </div>
    <div class="row info-block p-0"><!--row2-->
      <div class="col-6 row table-border-left">
        <p>Tiempo</p><span>{{RecipeData.receta.recipe_time}} minutos</span>
      </div>
      <div class="col-6 row table-border">
        <p>Porciones</p><span>{{RecipeData.receta.recipe_portions}} personas</span>
      </div>
    </div>
    <div class="row info-block"><!--row3-->
      <div class="col-12 row p-0">
        <h4 class="n-articulo borde-abajo">Ingredientes</h4>
        <hr>
      </div>
      <div class="col-12 row p-0" v-html="RecipeData.receta.recipe_ingredients">
      </div>
      <div class="col-12 row p-0">
        <h4 class="n-articulo borde borde-abajo">Preparación</h4>
      </div>
      <div class="col-12 row p-0" v-html="RecipeData.receta.recipe_preparation">

      </div>
    </div>
      
      <div class="col-12 p-0 mt-3 border-top pt-5">
        <div class="col-9 p-0"><p><a class="btn btn-lg btn-primary" href="#">volver</a></p></div>
        <div class="share-icons-box col-3 row">
          <div class="col-6 mr-2"><img class="share" src="/img/Icons-icon-share-filled.svg" alt="Compartir"></div>
          <div class="col-6"><img class="bookmark" src="/img/Icons-icon-bookmark-filled.svg" alt="Favoritos"></div>
        </div>
      </div>
  </div>
</section>

<!-- Seccion Tip&recetas  -->
<section class="tips container col-md-12">
  <div class="row featurette">
    <div class="col-md-5 order-md-1">
      <h2 class="featurette-heading">Otras
        <span class="text-muted"><br>Recetas
          Relacionadas</span></h2>
      <img :class="{'img-fluid': !mobile, 'separador': mobile}" src="/img/separador.svg" alt="separador">
      
    </div>
    <div class="col-md-7 order-md-2">

    </div>
  </div>

  <div class="card-deck section">
    <div class="card" v-for="recipe in RecipeData.relacionados" :key="recipe.id">
        <div class="categoria">
            <ul class="list-group list-group-horizontal">
                <li class="list-group-item" v-for="tag in recipe.recipe_tags" :key="tag.id" :class="tag.class_css">{{tag.tag}}</li>
                <!-- <li class="list-group-item">A third item</li> -->
              </ul>
        </div>
      <img :src="recipe.recipe_images[0].image_url" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{recipe.recipe_title}}</h5>
        <p class="card-text"><small class="text-muted-in"><img src="/img/icons-16px-time.svg" class="time-icon" alt="">{{$d(new Date(recipe.created_at), 'short')}}</small></p>
        <p class="card-text">{{recipe.summary}}</p>
        <div class="share-box row"><NuxtLink :to="localePath({'name': 'recetas-slug', 'params': {'slug': recipe.slug}}) " class="btn btn-secondary">Leer +</NuxtLink>
          <div class="share-icons">
            <img :class="{'img-fluid share': !mobile, 'share': mobile}" src="/img/Icons-icon-share-filled.svg" alt="Compartir">
            <img :class="{'img-fluid bookmark': !mobile, 'bookmark': mobile}" src="/img/Icons-icon-bookmark-filled.svg" alt="Favoritos">
            </div>
        </div>
    </div>
    </div>
  </div>
    <p><a class="btn btn-lg btn-primary" href="#"> volver</a></p>
</section>

 <LazyTheStoreBuy
      :title="title"
      :Button_text="bu_text"
      :Image_URL="image_url"
      :Button_link="bu_link"
      :class_section="class_section"
      v-if="!mobile"
    />
    <LazyMobileTheStoreBuyMob
      :title="title"
      :Button_text="bu_text"
      :Image_URL_mob="image_url_mob"
      :Button_link="bu_link"
      :class_section="class_section"
      v-if="mobile"
    />
  

    <!-- fin contenido -->
 </div>   
</template>

<script>
export default {
  async asyncData({ $axios, params }) {
    const RecipeData = await $axios.$get("/api/main/recipe/" + params.slug + '/');
    return { RecipeData };
  },
  data() {
    return {
       mobile: false,
       title: this.$t("TheStoreBuyModuleRecipe.Title"),
        bu_text: this.$t("Buttons.ViewCatalog"),
        bu_link: this.localePath('/productos'),
        image_url: "/img/img-catalogo.jpg",
        image_url_mob: "/img/mobile/img-catalogo-3.jpg",
        class_section: "donde-comprar",
    }
  },
  head() {
    return {
    title: this.RecipeData.receta.recipe_title,
    meta: [
      {name: "description", content: this.RecipeData.receta.recipe_title,}
    ]
    }
  },
  auth: "guest",
  mounted: function () {
    if (screen.width < 769) {
      this.mobile = true;
    }
  }
}
</script>

<style>
@import "~/assets/css/mobile.css";
.share {
    margin-right: 10px;
}
img.img-fluid.separador {
    padding-bottom: 35px;
}
 .borde-abajo{
      border-bottom: 1px solid #000 !important;
      margin-bottom: 25px;
  }
.info-block ul{
    list-style: none !important;
    padding: 0;
}
.seg-row>.datos-art>.n-articulo {
    font-size: 1.1rem !important;
    color: #fff;
}
.seg-row>.datos-art>.n-articulo span{
    font-size: 1.1rem !important;
    color: #fff;
    font-weight: 200;
}
.n-articulo {
    font-size: 1.1rem !important;
    color: #000;
}
.n-articulo span{
    font-size: 1.1rem !important;
    color: #000;
    font-weight: 200;
}
.recetas{
    background-color: #FFF;
    padding-left: 80px !important;
    padding-right: 80px !important;
}
.float-text {
    position: absolute !important;
    z-index: 10;
    background-color: #F4F5E6;
    padding: 30px 5px 20px 5px;
    left: 150px;
}
.left-col {
    background-color: #000;
}
.right-col{
    padding: 0 !important;
}
.info-text{
padding-top:50px;
}
.share-box {
    display: flex;
    justify-content: space-between;
}
.featurette-heading {
    margin-top: 0 !important;
    color: #000 !important;
    font-weight: bold !important;
    font-size: 2.5em !important;
}
.featurette-heading span{
 font-weight: normal !important;
 color: #000 !important;
}
h4.featurette-title {
    color: #000;
    font-weight: 400;
}
.receta{
    padding: 10px !important;
    background-color: #000 !important;
    color:#FFF;
    border: none !important;
    text-transform: uppercase;
    font-size: 0.7em;
}
.ensalada{
    padding: 10px !important;
    background-color: #CBD402 !important;
    color:#000;
    border: none !important;
    text-transform: uppercase;
    font-size: 0.7em;
}
.vegan{
    padding: 10px !important;
    background-color: #D5441C !important;
    color:#FFF;
    border: none !important;
    text-transform: uppercase;
    font-size: 0.7em;
}

</style>
