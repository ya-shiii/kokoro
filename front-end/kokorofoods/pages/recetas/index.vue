<template>
  <main role="main">
    <section class="info-contenido container col-12 section-slider seccion" v-if="mobile">
        <div class="row featurette">
            <div class="col-12  left-col">
            </div>
          
          <div class="col-12  right-col">
            <img class="img-fluid" src="/img/mobile/img-tips-1.jpg" alt="información 1">

          </div>
        </div>
        <div class="info-text info-cont-mob">
          <img src="img/mobil/top-seccion-img.jpg" alt="" class="top-img-secc">
          <div class="col-12">
            <h2 class="featurette-heading">Recetas de<span class="text-muted"><br>
              Ajo Negro</span></h2>
          </div>
            <img class="" src="/img/separador.svg" alt="separador">
        </div>

   </section>
    <section class="info-ajo container col-md-12 section" v-if="!mobile">
        <TheHeaderOP :title="title" :image="image" :background="background" v-if="!mobile"/>
      <div class="row info-text">
        <div class="col-md-3 order-md-1"></div>
        <div class="col-md-6 order-md-2 row">
          <!-- <div class="buscar row input-group mb-3">
            <input
              class="form-control"
              type="text"
              placeholder="Buscar"
              aria-label="Buscar"
            />
            <button class="btn btn-primary search-btn" type="submit">
              Buscar
            </button>
          </div> -->
          <p class="n-articulo">Filtros</p>
          <div class="col-md-12 categorizacion">
            <div class="categorias">
              <input
                v-for="categoria in categoryData.results"
                :key="categoria.id"
                class="btn btn-secondary text-nowrap"
                type="button"
                :value="categoria.category"
                :id="'filtro' + categoria.id"
                @click="seleccionada(categoria.id)"
              />
            </div>
          </div>
          <div class="pagination">
            <nav aria-label="Page navigation">
              <ul class="pagination">
                <li class="page-item">
                  <a
                    class="page-link"
                    href="#"
                    @click="bpp(blogsData.previous)"
                    aria-label="Previous"
                    v-show="blogsData.previous"
                  >
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                <li class="page-item">
                  <p class="page-link"><strong>Página {{page}}</strong>/{{countPages}}</p>
                </li>
                <li class="page-item">
                  <a
                    class="page-link"
                    href="#"
                    @click="bpn(blogsData.next)"
                    aria-label="Next"
                    v-show="blogsData.next"
                  >
                    <span aria-hidden="true">&raquo;</span>
                  </a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
        <div class="col-md-3 order-md-3"></div>
      </div>
    </section>
    <section class="info-ajo col-12" v-if="mobile">
    <div class="row">
        <div class="col-12 row">
        <p class="n-articulo">Seleccionar Categorías</p>
        <div class="col-12 categorizacion">
          
          <div class="categorias">
            
            <input class="btn btn-secondary btn-sm .text-nowrap" type="button" v-for="categoria in categoryData.results"
                :key="categoria.id" :value="categoria.category"
                :id="'filtro' + categoria.id"
                @click="seleccionada(categoria.id)">
          </div>
          
        </div>
        <div class="pagination">
          <nav aria-label="Page navigation">
            <ul class="pagination">
              <li class="page-item">
                <a class="page-link" href="#" aria-label="Previous"  @click="cpp(categoryData.previous)" v-show="categoryData.previous">
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              <li class="page-item "><p class="page-link"><strong>Página {{page}}</strong>/{{countPages}}</p></li>
              <li class="page-item">
                <a class="page-link" href="#" aria-label="Next"  @click="cpn(categoryData.next)" v-show="categoryData.next">
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
        
    </div>

</section>
    <section class="productos-dest container col-md-12" v-if="!mobile">
      <div class="row featurette">
        <div class="col-md-12 order-md-2 row">
          <div class="card-deck">
            <div
              class="card"
              v-for="blog in blogsData.results.slice(0, 3)"
              :key="blog.id"
            >
              <div class="categoria">
                <ul class="list-group list-group-horizontal">
                  <li
                    v-for="tag in blog.recipe_tags"
                    :key="tag.id"
                    :class="tag.class_css"
                  >
                    {{ tag.tag }}
                  </li>
                </ul>
              </div>
              <img
                v-for="image in blog.recipe_images.slice(0, 1)"
                :key="image.id"
                :src="image.image_url"
                class="card-img-top"
                :alt="blog.recipe_title"
              />
              <div class="card-body">
                <h5 class="card-title">{{ blog.recipe_title }}</h5>
                <p class="card-text">
                  <small class="text-muted-in"
                    ><img
                      src="/img/icons-16px-time.svg"
                      class="time-icon"
                      alt=""
                    />
                     {{$d(new Date(blog.created_at), 'short')}}</small
                  >
                </p>
                <p class="card-text">
                  {{ blog.summary }}...
                </p>
                <div class="share-box row">
                  <NuxtLink
                    :to="localePath({
                      name: 'recetas-slug',
                      params: { slug: blog.slug },
                    })"
                    class="btn btn-secondary">
                         Leer +
                  </NuxtLink>
                    <div class="share-icons">
                    <img
                      class="img-fluid share"
                      src="/img/Icons-icon-share-filled.svg"
                      alt="Compartir"
                    />
                    <img
                      class="img-fluid bookmark"
                      src="/img/Icons-icon-bookmark-filled.svg"
                      alt="Favoritos"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-12 order-md-2 row">
          <div class="card-deck section">
            <div
              class="card"
              v-for="blog in blogsData.results.slice(3, 6)"
              :key="blog.id"
            >
              <div class="categoria">
                <ul class="list-group list-group-horizontal">
                  <li
                    v-for="tag in blog.recipe_tags"
                    :key="tag.id"
                    :class="tag.class_css"
                  >
                    {{ tag.tag }}
                  </li>
                </ul>
              </div>
              <img
                v-for="image in blog.recipe_images.slice(0, 1)"
                :key="image.id"
                :src="image.image_url"
                class="card-img-top"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ blog.recipe_title }}</h5>
                <p class="card-text">
                  <small class="text-muted-in"
                    ><img
                      src="/img/icons-16px-time.svg"
                      class="time-icon"
                      alt=""
                    />
                    {{$d(new Date(blog.created_at), 'short')}}</small
                  >
                </p>
                <p class="card-text">
                  {{ blog.summary}}...
                </p>
                <div class="share-box row">
                  <NuxtLink
                    :to="localePath({
                      name: 'recetas-slug',
                      params: { slug: blog.slug },
                    })"
                    class="btn btn-secondary">
                         Leer +
                  </NuxtLink>
                  <div class="share-icons">
                    <img
                         class="img-fluid share"
                         src="/img/Icons-icon-share-filled.svg"
                         alt="Compartir"
                    />
                    <img
                         class="img-fluid bookmark"
                         src="/img/Icons-icon-bookmark-filled.svg"
                         alt="Favoritos"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
           <div class="pagination">
            <nav aria-label="Page navigation">
              <ul class="pagination">
                <li class="page-item">
                  <a
                    class="page-link"
                    @click="bpp(blogsData.previous)"
                    aria-label="Previous"
                    v-show="blogsData.previous"
                  >
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                <li class="page-item">
                  <p class="page-link"><strong>Página {{page}}</strong>/{{ countPages}}</p>
                </li>
                <li class="page-item">
                  <a
                    class="page-link"
                    @click="bpn(blogsData.next)"
                    aria-label="Next"
                    v-show="blogsData.next"
                  >
                    <span aria-hidden="true">&raquo;</span>
                  </a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
        
      </div>
    </section>
    <section class="productos-dest container col-12 mb-5 mt-5" v-if="mobile">
  <NuxtLink class="btn btn-lg outlined p-0 link-rec" :to="localePath({
                      name: 'recetas-slug',
                      params: { slug: blog.slug },
                    })" v-for="blog in blogsData.results"
              :key="blog.id">
    <div class="col-12 row p-0">
      <div class="col-10 p-0 col-i">
        <p>{{blog.recipe_title}}</p>
    </div>
    <div class="col-2 p-0 col-d">
      <p>Leer</p>
    </div>
  </div>
  </NuxtLink>
</section>

  </main>
</template>
<script>
import axios from "axios";
export default {
  async asyncData({ $axios }) {
    const categoryData = await $axios.$get("/api/main/category/");
    const blogsData = await $axios.$get("/api/main/recipes/");
    return { categoryData, blogsData };
  },
  auth: "guest",
  data() {
    return {
      title: '<span class="text-muted">Ricas </span> <br>Recetas de ajo negro',
      image: "/img/tips.jpg",
      background: "#000000",
      mobile: false,
      page: 1
    };
  },
  mounted: function () {
    if (screen.width < 769) {
      this.mobile = true;
    }
  },
  computed: {
    countPages() {
            var pages = Math.ceil(this.blogsData.count/8)
            return ('0' + pages).slice(-2)
        },
  },
  methods: {
    cpn: function (nexturl) {
      axios.get(nexturl).then((response) => {
        this.categoryData = response.data;
      });
    },
    cpp: function (previousurl) {
      axios.get(previousurl).then((response) => {
        this.categoryData = response.data;
      });
    },
    bpn: function (nexturl) {
      axios.get(nexturl).then((response) => {
        this.blogsData = response.data;
        this.page += 1
      });
    },
    bpp: function (previousurl) {
      axios.get(previousurl).then((response) => {
        this.blogsData = response.data;
         this.page -= 1
      });
    },
    seleccionada: function (id) {
      var elemento = document.getElementById("filtro" + id);
      if (elemento.classList.contains("btn-secondary")) {
        elemento.classList.remove("btn-secondary");
        elemento.classList.add("btn-primary");
      } else {
        elemento.classList.remove("btn-primary");
        elemento.classList.add("btn-secondary");
      }
      var array = $(".btn-primary").map(function () {
        return $(this).attr("id");
      });
      var filtrado = "http://localhost:8000/api/main/recipes/?";
      for (var i = 0; i < array.length; i++) {
        filtrado = filtrado.concat("category=", array[i].substring(6), "&");
      }
      axios.get(filtrado).then((response) => {
        this.blogsData = response.data;
      });
    },
  },
};
</script>
<style scoped>
/* seccion Productos destactados */
.productos-dest {
  background-color: #fff;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
/* Seccion Tip&recetas */
.card {
  background-color: none !important;
  border: none !important;
}
.card-body {
  padding: 10px 0 !important;
}
.card-title {
  color: #000;
  font-weight: 400;
}
.time-icon {
  width: 5%;
  padding: 0 5px 0 0;
}
.text-muted-in {
  color: #000 !important;
}
.card-text {
  font-weight: 300;
}
.share {
  margin-right: 10px;
}
.tips {
  background-color: #fff;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
.share-box {
  display: flex;
  justify-content: space-between;
}

/* Categorias */
.categorias input {
  margin: 10px 10px 10px 0;
}
.categorias {
  flex-wrap: wrap;
}
.categorizacion {
  padding: 0 !important;
}
.ui-corner-all {
  /* border-radius: 100%  !important; */
}
.ui-slider-handle {
  border-radius: 100% !important;
  background-color: #000 !important;
}
.ui-slider-horizontal .ui-slider-handle {
  top: -0.6em !important;
  margin-left: -0.6em;
}
.ui-slider-horizontal {
  height: 0px !important;
  color: #000 !important;
  border: 1px solid #00000038 !important;
}
.ui-widget-header {
  border: 1px solid #000 !important;
  background: #e9e9e9;
  color: #333333;
  font-weight: bold;
}

.ui-slider {
  position: relative;
  text-align: left;
  margin-bottom: 50px;
}
.list-group {
  border-radius: 0 !important;
  border: none !important;
}
.list-group-item {
  border: 0px solid !important;
}
.list-group-horizontal > .list-group-item:first-child,
.list-group-horizontal > .list-group-item + .list-group-item {
  border-bottom-left-radius: 0 !important;
  border-top-right-radius: 0 !important;
}
.receta {
  padding: 10px !important;
  background-color: #000 !important;
  color: #fff;
  border: none !important;
  text-transform: uppercase;
  font-size: 0.7em;
}
.ensalada {
  padding: 10px !important;
  background-color: #cbd402 !important;
  color: #000;
  border: none !important;
  text-transform: uppercase;
  font-size: 0.7em;
}
.vegan {
  padding: 10px !important;
  background-color: #d5441c !important;
  color: #fff;
  border: none !important;
  text-transform: uppercase;
  font-size: 0.7em;
}
</style>