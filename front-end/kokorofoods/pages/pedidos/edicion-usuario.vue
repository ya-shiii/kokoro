<template>
    <section class="p-0 m-0 col-lg-12 row">
     <!-- MENU USUARIO IZQUIERDO -->
          <div class="info-left col-lg-4 p-0 side-lists">
               <!-- user id - menu -->
               <div class="row featurette user-id">
                    <nuxt-link :to="localePath('/pedidos/edicion-usuario')" class="id-menu center-itms">
                         <strong class="text">
                              Diego Berrios
                         </strong>
                         <img class="user-icon"
                              src="~/static/img/edit-icon.svg"
                              alt=""/>
                    </nuxt-link>
               </div>
               <!-- user id - menu -->
               <ul class="navbar-nav mr-auto usr-mn">
                    <li class="nav-item border-bottom active">
                         <a class="nav-link" href="#">
                               {{ $t("orders.my_orders") }}
                              <span>
                                   <img class="icon" src="~/static/img/path.svg" alt="" />
                              </span>
                              <span class="sr-only">(current)</span>
                         </a>
                    </li>
                    <li class="nav-item border-bottom">
                         <a class="nav-link" href="#">
                             {{ $t("orders.favorite_recipes") }}
                              <span>
                                   <img class="icon" src="~/static/img/path.svg" alt="" />
                              </span>
                         </a>
                    </li>
                    <li class="nav-item border-bottom">
                         <a class="nav-link" href="#" tabindex="-1">
                               {{ $t("orders.favorite_tips") }}
                              <span>
                                   <img class="icon" src="~/static/img/path.svg" alt="" />
                              </span>
                         </a>
                    </li>
                    <li class="nav-item border-bottom">
                         <a class="nav-link"
                              href="#"
                              tabindex="-1">
                                   {{ $t("orders.subscriptions") }}
                              <span>
                                   <img class="icon" src="~/static/img/path.svg" alt="" />
                              </span>
                         </a>
                    </li>
               </ul>
          </div>
          <!-- MENU USUARIO DERECHO -->
          <div class="info-right col-lg-8 p-0 user-order">
               <div class="row featurette title-id">
                    <strong class="text">
                         {{ $t("orders.edit_profile") }}
                    </strong>
               </div>
               <div class="display-icon">
                    <img class="ubic-ds"
                         src="~/static/img/ubicacion-display.svg"
                         alt="">
               </div>
               <ul class="form-inputs">
                    <li class="item">
                         <label class="title">
                              {{ $t("orders.address") }}
                         </label>
                         <input class="input-text"
                              type="text"
                              placeholder="San Enrique 550"
                              aria-label="Address">
                    </li>
                    <li class="item">
                         <label class="title">
                              {{ $t("orders.apartment_block_or_house") }}
                         </label>
                         <input class="input-text"
                              type="text"
                              placeholder="San Enrique 550"
                              aria-label="Address">
                    </li>
                    <li class="item">
                         <label class="title">
                              {{ $t("orders.region_state") }}
                         </label>
                         <input class="input-text"
                              type="text"
                              placeholder="San Enrique 550"
                              aria-label="Address">
                    </li>
                    <li class="item">
                         <label class="title">
                              {{ $t("orders.commune_city") }}
                         </label>
                         <input class="input-text"
                              type="text"
                              placeholder="San Enrique 550"
                              aria-label="Address">
                    </li>
                    <li class="item">
                         <label class="title">
                              {{ $t("orders.postal_code") }}
                         </label>
                         <input class="input-text"
                              type="text"
                              placeholder="San Enrique 550"
                              aria-label="Address">
                    </li>
               </ul>
               <div class="display-icon">
                    <img class="ubic-ds" src="~/static/img/pagos-display.svg" alt="">
               </div>
               <div class="associated-cards">
                    <div class="flex">
                         <div class="sub-title">
                              {{ $t("orders.associated_cards") }}
                         </div>
                         <div class="form-group">
                              <input class="input-form"
                                   type="text"
                                   placeholder="xxxx-xxxx-xxxx-4556">
                              <img 
                                   class="ico-mas"
                                   src="~/static/img/icon-menos.svg"
                                   alt="">
                         </div>
                         <div class="form-group">
                              <input class="input-form"
                                   type="text"
                                   placeholder="xxxx-xxxx-xxxx-4556"
                                   aria-label="Address">
                              <img
                                   class="ico-mas"
                                   src="~/static/img/icon-mas.svg"
                                   alt=""> 
                         </div>
                    </div>
                    <div class="buttons">
                         <button 
                              class="return btn"
                              type="submit">
                                   {{ $t("orders.return") }}
                         </button>
                         <button 
                              class="save btn"
                              type="submit">
                                   {{ $t("orders.save") }}
                         </button>
                    </div>  
               </div>
          </div>
     </section>
</template>

<script lang="js">
     export default {
          data() {
              return {
                    orders: [
                    {
                         subscribe: false,
                         data: "20 / 05 / 2022",
                         total: "$25.490"
                    },
                    {
                         subscribe: true,
                         data: "05/20/2022",
                         total: "$25.490"
                    },
                    {
                         subscribe: false,
                         data: "20 / 05 / 2022",
                         total: "$25.490"
                    },
                    {
                         subscribe: false,
                         data: "20 / 05 / 2022",
                         total: "$25.490"
                    },
                    {
                         subscribe: false,
                         data: "20 / 05 / 2022",
                         total: "$25.490"
                    },
                    {
                         subscribe: false,
                         data: "20 / 05 / 2022",
                         total: "$25.490"
                    },
               ]
              }
          }
     }
</script>

<style lang="scss" scoped>
     ul {
          list-style-type: none!important;
     }
     .side-lists, .user-order{
          margin: 35px 0 0 0;
     }
     .user-id {
          background-color: #D5441C;
          padding: 20px 50px;
          height: 90px;
          .center-itms{
               border-radius: 5px;
               background: #fff;
               padding: 10px;
               width: 100%;
               .text {
                    display: flex;
                    width: 100%;
                    font-size: 14px;
                    font-family: Mukta, sans-serif;
                    color: #000;
                    padding: 4px 5px 0;
               }
          }
     }
     .user-order{
          .title-id{
               background-color: #CBD402;
               height: 90px;
               .text{
                    display: block;
                    margin: 0 auto;
                    color: #fff;
                    font-size: 18px;
                    font-family: Mukta, sans-serif;
                    font-weight: 700;
                    line-height: 90px;
               }
          }
          .display-icon{
               text-align: center;
               margin: 30px 0;
               padding: 0 0 0 40px;
          }
          .form-inputs{
               .item {
                    width: fit-content;
                    margin: 0 auto;
                    font-family: "Mukta, sans-serif";
                    .title {
                         display: block;
                         font-size: 14px;
                         margin: 0 0 16px 0;
                         color: #000;
                    }
                    .input-text {
                         display: block;
                         border: 1px solid #ced4da;
                         font-size: 14px;
                         padding: 6px 12px;
                         width: 400px;
                         height: 38px;
                         margin: 0 0 20px 0;
                         border-radius: .25rem;
                    }
               }
          }
          .associated-cards{
               width: fit-content;
               margin: 0 auto;
               padding: 0 0 0 50px;
               .sub-title{
                    font-family: "Mukta, sans-serif";
                    font-size: 15px;
                    background: none;
                    color: #000;
                    margin: 0 0 20px 0;
               }
               .input-form{
                    border: 1px solid #ced4da;
                    width: 340px;
                    height: 38px;
                    border-radius: .25rem;
                    padding: 5px 10px;
                    margin: 0 0 3px 0;
               }
               .ico-mas{
                    margin: 0 0 0 10px;
               }
               .form-group {
                    display: flex;
               }
               .buttons{
                    margin: 30px 0 70px 0;
                    .btn{
                         border-color: #000;
                         border-radius: .25rem;
                         padding: 8px 13px!important;
                         text-transform: uppercase;
                         font-size: 14px;
                    }
                    .return{
                         color: #000;
                         background: none;
                    }
                    .save {
                         float: right;
                         background: #000;
                         color: #fff;
                    }
               }
          }
     }
     .id-menu{
          display: flex;
     }
     .side-lists{
          .usr-mn{
               width: 295px;
               margin: 50px auto;
               .nav-link{
                    color: #000;
               }
               .border-bottom{
                    padding: 15px 0;
               }
               .icon{
                    margin: 5px 0 0 0;
                    float: right;
                    transform: rotateZ(270deg);
               }
               .active {
                    border-bottom: 2px solid #D5441C !important;
               }
          }
     }
     @media only screen and (max-width: 500px) {
          .user-order{
               .display-icon{
                    padding: 0;
               }
               .form-inputs{
                    padding: 10px 50px;
                    .item {
                         width: 100%;
                         .input-text {
                              width: 100%;
                         }
                    }
               }
               .associated-cards{
                    padding: 0;
                    .input-form {
                         width: 100%;
                    }
               }
          }
     }
</style>