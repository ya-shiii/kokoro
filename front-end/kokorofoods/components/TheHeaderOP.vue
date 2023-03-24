<template>
            <div class="row featurette">
                <div class="col-md-3 order-md-1" :style="{backgroundColor: background }">
                </div>
            <div class="col-md-3 order-md-3 float-text">
                <h2 class="featurette-heading" v-html="title"></h2>
                <img class="img-fluid separador" src="/img/separador.svg" alt="separador">
            </div>
            <div class="col-md-9 order-md-2 right-col">
                <img class="img-fluid" :src="image" alt="Ajo Negro">

            </div>
            </div>
</template>


<script>
export default {
    props: {
        title: String,
        image: String,
        background: String
    }
}
</script>

<style scoped>
.info-ajo{
    background-color: #FFF;
    padding-left: 80px !important;
    padding-right: 80px !important;
}
.right-col{
    padding: 0 !important;
}
.left-col {
    background-color: #000;
}
img.img-fluid.separador {
    padding-bottom: 35px;
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
.float-text {
    position: absolute !important;
    z-index: 10;
    background-color: #F4F5E6;
    padding: 30px 5px 20px 5px;
    left: 150px;
}
</style>