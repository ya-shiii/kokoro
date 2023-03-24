<template>
  <main role="main">
    <section class="info-ajo container col-md-12 section">
      <TheHeaderOP :title="title" :image="image" :background="background" />

      <div class="row info-text">
        <div class="col-md-3 order-md-1"></div>
        <div class="col-md-6 order-md-2 row">
          <div class="buscar row input-group mb-3">
            <input
              class="form-control"
              type="text"
              placeholder="Buscar"
              aria-label="Buscar"
            />
            <button class="btn btn-primary search-btn" type="submit">
              Buscar
            </button>
          </div>
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
                    @click="cpp(categoryData.previous)"
                    aria-label="Previous"
                  >
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                <li class="page-item">
                  <p class="page-link"><strong>Página 01</strong>/08</p>
                </li>
                <li class="page-item">
                  <a
                    class="page-link"
                    href="#"
                    @click="cpn(categoryData.next)"
                    aria-label="Next"
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
    <section class="productos-dest container col-md-12">
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
                    v-for="tag in blog.tags"
                    :key="tag.id"
                    :class="tag.class_css"
                  >
                    {{ tag.tag }}
                  </li>
                </ul>
              </div>
              <img
                v-for="image in blog.blog_images.slice(0, 1)"
                :key="image.id"
                :src="image.image_url"
                class="card-img-top"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ blog.blog_title }}</h5>
                <p class="card-text">
                  <small class="text-muted-in"
                    ><img
                      src="img/icons-16px-time.svg"
                      class="time-icon"
                      alt=""
                    />
                    Actualizado el {{ blog.updated_at }}</small
                  >
                </p>
                <p class="card-text">
                  "{{ blog.blog_content.slice(0, 127) }}..."
                </p>
                <div class="share-box row">
                  <router-link
                    :to="localePath({
                      name: 'blog___es',
                      params: { id: blog.id, slug: blog.slug },
                    })"
                    class="btn btn-secondary">
                         Leer +
                    </router-link>
                    <div class="share-icons">
                    <img
                      class="img-fluid share"
                      src="img/Icons-icon-share-filled.svg"
                      alt="Compartir"
                    />
                    <img
                      class="img-fluid bookmark"
                      src="img/Icons-icon-bookmark-filled.svg"
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
                    v-for="tag in blog.tags"
                    :key="tag.id"
                    :class="tag.class_css"
                  >
                    {{ tag.tag }}
                  </li>
                </ul>
              </div>
              <img
                v-for="image in blog.blog_images.slice(0, 1)"
                :key="image.id"
                :src="image.image_url"
                class="card-img-top"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ blog.blog_title }}</h5>
                <p class="card-text">
                  <small class="text-muted-in"
                    ><img
                      src="img/icons-16px-time.svg"
                      class="time-icon"
                      alt=""
                    />
                    Actualizado el {{ blog.updated_at }}</small
                  >
                </p>
                <p class="card-text">
                  "{{ blog.blog_content.slice(0, 127) }}..."
                </p>
                <div class="share-box row">
                  <router-link
                    :to="localePath({
                         name: 'blog___es',
                         params: { id: blog.id, slug: blog.slug },
                    })"
                    class="btn btn-secondary">
                    Leer +
                    </router-link>
                  <div class="share-icons">
                    <img
                         class="img-fluid share"
                         src="img/Icons-icon-share-filled.svg"
                         alt="Compartir"
                    />
                    <img
                         class="img-fluid bookmark"
                         src="img/Icons-icon-bookmark-filled.svg"
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
                  >
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                <li class="page-item">
                  <p class="page-link"><strong>Página 01</strong>/08</p>
                </li>
                <li class="page-item">
                  <a
                    class="page-link"
                    @click="bpn(blogsData.next)"
                    aria-label="Next"
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
  </main>
</template>
<script>
import axios from "axios";
export default {
  async asyncData({ $axios }) {
    const categoryData = await $axios.$get("/api/main/category/");
    const blogsData = await $axios.$get("/api/main/blog/");
    return { categoryData, blogsData };
  },
  auth: "guest",
  data() {
    return {
      title: '<span class="text-muted">Headline</span> <br>Tips & Recetas',
      image: "img/tips.jpg",
      background: "#000000",
    };
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
      });
    },
    bpp: function (previousurl) {
      axios.get(previousurl).then((response) => {
        this.blogsData = response.data;
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
      var filtrado = "https://api.kokorofoods.cl/api/main/blog/?";
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