<template>
  <section class="tips container col-md-12">
    <div class="row featurette">
      <div class="col-md-5 order-md-1">
        <h2 class="featurette-heading">
          Headline
          <span class="text-muted"><br />Tips &amp; Recetas Relacionadas</span>
        </h2>
        <img class="img-fluid" src="img/separador.svg" alt="separador" />
      </div>
      <div class="col-md-7 order-md-2"></div>
    </div>
    claro claro claro

    <div class="card-deck section">
      <div
        class="card"
        v-for="blog in blogsData.results.slice(0, 3)"
        :key="blog.id"
      >
        <div class="categoria">
          <ul class="list-group list-group-horizontal">
            <li v-for="tag in blog.tags" :key="tag.id" :class="tag.class_css">
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
               <small class="text-muted-in">
               <img src="img/icons-16px-time.svg" class="time-icon" alt="" />
                    Actualizado el {{ blog.updated_at }}
               </small>
          </p>
          <p class="card-text">"{{ blog.blog_content.slice(0, 127) }}..."</p>
          <div class="share-box row">
               <router-link
                    :to="localePath({
                    name: 'blog___es',
                    params: { id: blog.id, slug: blog.slug },
               })"
              class="btn btn-secondary">
              Leer +</router-link>
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
     <p>
          <NuxtLink :to="localePath('/tipsyrecetas')" 
               class="btn btn-lg btn-primary">
               volver
          </NuxtLink>
     </p>
     </section>
</template>
<script>
     export default {
          props: {
               blogsData: Object,
          },
     };
</script>
<style scoped>
     img.img-fluid.separador {
          padding-bottom: 35px;
     }
     .featurette-heading {
          margin-top: 0 !important;
          color: #000 !important;
          font-weight: bold !important;
          font-size: 2.5em !important;
     }
     .featurette-heading span {
          font-weight: normal !important;
          color: #000 !important;
     }
     h4.featurette-title {
          color: #000;
          font-weight: 400;
     }
     .info-text p {
          color: #000;
          font-weight: 400;
     }
</style>