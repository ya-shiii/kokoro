<template>
    <section class="p-0 m-0 col-lg-12 row">
     <!-- MENU USUARIO IZQUIERDO -->
     <div class="info-left col-lg-4 p-0 side-lists">
          <!-- user id - menu -->
          <div class="row featurette user-id">
               <nuxt-link :to="localePath('/pedidos/edicion-usuario')" class="id-menu center-itms">
                    <strong class="text">
                         {{ name }}
                    </strong>
                    <img class="user-icon"
                         src="~/static/img/edit-icon.svg"
                         alt=""/>
               </nuxt-link>
          </div>
          <!-- user id - menu -->
          <ul class="navbar-nav mr-auto usr-mn">
               <li class="nav-item border-bottom active">
                    <a class="nav-link" href="">
                         {{ $t("orders.my_orders") }}
                         <span>
                              <img class="icon" src="~/static/img/path.svg" alt="" />
                         </span>
                         <span class="sr-only">(current)</span>
                    </a>
               </li>
               <!-- <li class="nav-item border-bottom">
                    <a class="nav-link" href="">
                         {{ $t("orders.favorite_recipes") }}
                         <span>
                              <img class="icon" src="~/static/img/path.svg" alt="" />
                         </span>
                    </a>
               </li>
               <li class="nav-item border-bottom">
                    <a class="nav-link" href="" tabindex="-1">
                          {{ $t("orders.favorite_tips") }}
                         <span>
                              <img class="icon" src="~/static/img/path.svg" alt="" />
                         </span>
                    </a>
               </li> -->
               <!-- <li class="nav-item border-bottom">
                    <a class="nav-link"
                         href=""
                         tabindex="-1">
                              {{ $t("orders.subscriptions") }}
                         <span>
                              <img class="icon" src="~/static/img/path.svg" alt="" />
                         </span>
                    </a>
               </li> -->
          </ul>
      </div>
      <!-- MENU USUARIO DERECHO -->
     <div class="info-right col-lg-8 p-0 user-order">
          <div class="row featurette title-id">
               <strong class="text">
                    {{ $t("orders.my_orders") }}
               </strong>
          </div>
        <!-- user id - menu -->
        <div class="pedidos col-12 mt-3 mb-3 p-0">
          <ul class="navbar-nav p-3">
            <li class="nav-item border-bottom active p-0 m-0 col-12">
               <div class="tabla-tit col-12 row p-0 m-0">
                    <div class="col p-0 mt-0 mb-0 center-itms">
                    <strong><p>
                         {{ $t("orders.number") }}   
                         </p></strong>
                    </div>
                    <div class="col p-0 mt-0 mb-0 center-itms">
                    <strong><p>
                         {{ $t("orders.date") }}   
                         </p></strong>
                    </div>
                    <div class="col p-0 mt-0 mb-0 center-itms">
                         <strong><p>TOTAL</p></strong>
                    </div>
               </div>
            </li>
            <li class="nav-item border-bottom active p-0 m-0 col-12" 
               v-for="order in OrdersData.results" :key="order.order_number">
              <NuxtLink
                class="nav-link itm p-0 m-"
                :to="localePath('/pedidos/' + order.order_number)"
              >
                <div class="tabla-tit col-12 row p-0 m-0">
                    <div class="col p-0 mt-0 mb-0 center-itms">
                         <span class="text">
                         {{order.order_number}}
                         </span>
                    </div>
                  <div class="col p-0 mt-0 mb-0 center-itms">
                    <span class="text">
                        {{$d(new Date(order.created_at), 'short')}}
                      </span>
                  </div>
                  <div class="col p-0 mt-0 mb-0 center-itms row">
                       <div class="total">
                             <span class="text">{{ order.total_net}}</span>
                              <span class="icon" style="padding-left:10%;">
                                   <img src="~/static/img/path.svg" alt="" />
                              </span>
                       </div>
                  </div>
                </div>
              </NuxtLink>
            </li>
          </ul>
        </div>
        <div class="return">
             <NuxtLink class="btn return-btn center center-itms" :to="localePath('/productos')">
                     {{ $t("orders.return") }}   
             </NuxtLink>
          </div>
      </div>
    </section>
</template>

<script lang="js">
     export default {
          data() {
              return {
              }
          },
          async asyncData({ $axios, $auth}) {
               const OrdersData = await $axios.$get("/api/main/order/?user=" + $auth.user[0].id);
               return { OrdersData };
               },
          computed: {
               name(){

                    return this.$auth.user[0].first_name + ' ' + this.$auth.user[0].last_name
               }
          }
     }
</script>

<style lang="scss" scoped>
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
          .pedidos{
               width: 590px;
               margin: 0 auto;
               .center-itms {
                    display: block;
                    margin: 0 auto;
                    text-align: center !important;
                    .text {
                         display: block;
                         padding: 20px 0;
                         color: #000;
                         .sus-ico{
                              width: 12px;
                              margin: -5px 0 0 -5px;
                         }
                    }
               }
               .total{
                    display: flex;
                    margin: 0 auto;
                    .text {
                         text-align: center;
                         width: 100%;
                    }
                    .icon{
                         margin: 3px 0 0 0;
                         float: right;
                         transform: rotateZ(270deg);
                    }
               }
          }
     }
     .id-menu{
          display: flex;
     }
     .return {
          margin: 0 auto 30px;
          width: fit-content;
          .return-btn{
               color: #000;
               border-color: #000;
               width: 250px;
          }
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

     @media only screen and (max-width: 1023px) {
          .user-id {
               .center-itms{
                     width: 100%;
                    .text {       
                         width: 100%;
                    }
               }
          }
          .side-lists{
               .usr-mn{
                    width: 90%;
                    margin: 0 auto;
                    .icon{
                         margin: 5px 0 0 0;
                         float: right;
                         transform:unset;
                    }
               }
          }
          .user-order{
               .pedidos{
                    .center-itms {
                         .text {
                              transform: none;
                              text-align: center;
                              width: 100%;
                         }
                    }
                    .total{
                         .text {
                              transform: none;
                         }
                    }
               }
          }
     }

     @media only screen and (max-width: 400px) {
          .user-id {
               padding: 20px 10px;
          }
     }
</style>