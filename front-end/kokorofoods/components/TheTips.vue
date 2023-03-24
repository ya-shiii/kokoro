<template>
    <section class="tips container col-md-12">
    <div class="row featurette">
      <div class="col-md-5 order-md-1">
        <h2 class="featurette-heading">Tips & Recetas<span class="text-muted"><br> Para incorporar el Ajo Negro en tu estilo de vida.</span></h2>
        <img class="img-fluid separador" src="img/separador.svg" alt="separador">
        <p><a class="btn btn-lg btn-secondary" href="#">ver todos los tips & recetas</a></p>
      </div>
      <div class="col-md-7 order-md-2">

      </div>
    </div>

    <div class="card-deck section">
        <div class="card">
            <div class="categoria">
                <ul class="list-group list-group-horizontal">
                    <li class="list-group-item receta">Receta</li>
                    <li class="list-group-item ensalada">Ensalada</li>
                    <li class="list-group-item vegan">Vegan</li>
                    <!-- <li class="list-group-item">A third item</li> -->
                  </ul>
            </div>
          <img src="img/img-tips.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text"><small class="text-muted-in"><img src="img/icons-16px-time.svg" class="time-icon" alt=""> Last updated 3 mins ago</small></p>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <div class="share-box row"><a href="#" class="btn btn-secondary">Leer +</a>
              <div class="share-icons">
                <img class="img-fluid share" src="img/Icons-icon-share-filled.svg" alt="Compartir">
                <img class="img-fluid bookmark" src="img/Icons-icon-bookmark-filled.svg" alt="Favoritos">
                </div>
            </div>
        </div>
        </div>
        <div class="card">
            <div class="categoria">
                <ul class="list-group list-group-horizontal">
                    <li class="list-group-item receta">Receta</li>
                    <li class="list-group-item ensalada">Ensalada</li>
                    <li class="list-group-item vegan">Vegan</li>
                    <!-- <li class="list-group-item">A third item</li> -->
                  </ul>
            </div>
            <img src="img/img-tips.jpg" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text"><small class="text-muted-in"><img src="img/icons-16px-time.svg" class="time-icon" alt="">Last updated 3 mins ago</small></p>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="share-box row"><a href="#" class="btn btn-secondary">Leer +</a>
                <div class="share-icons">
                <img class="share" src="img/Icons-icon-share-filled.svg" alt="Compartir">
                <img class="bookmark" src="img/Icons-icon-bookmark-filled.svg" alt="Favoritos">
                </div>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="categoria">
                <ul class="list-group list-group-horizontal">
                    <li class="list-group-item receta">Receta</li>
                    <li class="list-group-item ensalada">Ensalada</li>
                    <li class="list-group-item vegan">Vegan</li>
                    <!-- <li class="list-group-item">A third item</li> -->
                  </ul>
            </div>
            <img src="img/img-tips.jpg" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text"><small class="text-muted-in"><img src="img/icons-16px-time.svg" class="time-icon" alt="">Last updated 3 mins ago</small></p>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="share-box row"><a href="#" class="btn btn-secondary">Leer +</a>
                <div class="share-icons">
                  <img class="share" src="img/Icons-icon-share-filled.svg" alt="Compartir">
                  <img class="bookmark" src="img/Icons-icon-bookmark-filled.svg" alt="Favoritos">
                  </div>
                </div>
            </div>
          </div>
      </div>
    
</section>
</template>

<script>
export default {
    
}
</script>


<style>


.card{
    background-color: none !important;
    border: none !important;

}
.card-body{
    padding: 10px 0 !important;
}
.card-title{
    color: #000;
    font-weight: 400;
}
.time-icon{
    width: 5%;
    padding: 0 5px 0 0 ;
}
.text-muted-in{
    color: #000 !important;
}
.card-text{
    font-weight: 300;
}
.share {
    margin-right: 10px;
}
.tips{
    background-color: #FFF;
    padding-left: 80px !important;
    padding-right: 80px !important;
}
.share-box {
    display: flex;
    justify-content: space-between;
}
.categorias input {
    margin: 10px 10px 10px 0;
}
.categorias {
    flex-wrap: wrap;
}
.categorizacion {
    padding: 0 !important;
}
.ui-corner-all{
    /* border-radius: 100%  !important; */
}
.ui-slider-handle {
    border-radius: 100% !important;
    background-color: #000 !important;
}
.ui-slider-horizontal .ui-slider-handle {
    top: -0.6em !important;
    margin-left: -.6em;
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
.list-group{
    border-radius: 0 !important;
    border: none !important;
}
.list-group-item{
    border: 0px solid !important;
}
.list-group-horizontal>.list-group-item:first-child, .list-group-horizontal>.list-group-item+.list-group-item{
    border-bottom-left-radius: 0 !important;
    border-top-right-radius: 0 !important;
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
.list-group-horizontal {
    flex-direction: row;
 }
</style>