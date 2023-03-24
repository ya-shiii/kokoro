
export const state = () => ({
    cart: [],
    total_product: 0,
    SubTotal: 0,
    Shipping: null,
    Discount: 0,
    Total: 0,
    cart_message: false,
    cart_store: 0,
    store_error: false
  })

export const mutations = {
    addProductToCartM(state, product_cart){
        const result = state.cart.findIndex( (obj) => obj.product.id === product_cart.product.id)
        if (result > -1){
            state.cart[result].quantity++
            state.total_product++
            state.SubTotal += product_cart.product.price
        } else {
            if (state.cart.length == 0){
                state.cart_store = product_cart.store
            }
        state.cart.push(product_cart)
        state.total_product++
        state.SubTotal += product_cart.product.price
        }
        state.Total = state.SubTotal + state.Shipping - state.Discount
        state.cart_message = true
    },
    modifyQuantity(state, item){
        if (item.plus){
            const result = state.cart.findIndex( (obj) => obj.product.id === item.itemTo.product.id)
            state.total_product++
            state.cart[result].quantity++
            state.SubTotal += item.itemTo.product.price
        } else {
            const result = state.cart.findIndex( (obj) => obj.product.id === item.itemTo.product.id)
            if (item.itemTo.quantity == 1) {
                state.cart.splice(result, 1)
                state.SubTotal -= item.itemTo.product.price
            } else {
                state.total_product--
                state.cart[result].quantity--
                state.SubTotal -= item.itemTo.product.price
            }
        }
        state.Total = state.SubTotal + state.Shipping - state.Discount
    },
    ModifyShipping(state, Shipping){
        state.Shipping = Shipping
        state.Total = state.SubTotal + state.Shipping
    },
    StoreError(state){
        state.store_error = true
    },
    Modal(state){
        state.store_error = false
    }
}

export const actions = {
    CloseModal(context) {
        context.commit("Modal")
    },
    addProductToCart(context, product){
        const store = context.getters.GetCheckStore
        this.$gtm.push({ event: 'addToCart',
            product_name: product.product.name,
            Quantity: product.quantity,
            Store: store,
            Price: product.product.price
          });
        if (product.product.store == store){
                context.commit('addProductToCartM', product)
                this.$router.push(this.localePath('/carro'))
        } else if (store == 0) {
            context.commit('addProductToCartM', product)
            this.$router.push(this.localePath('/carro'))
        }else {
            context.commit('StoreError')
        }
        
    },
    PlusOne(context, item){
        context.commit('modifyQuantity', item)
    },
    AddShipping(context, shipping){
        context.commit('ModifyShipping', shipping)
    },
    async PayOrder( context, cart){
        const payload = {'cart': context.state.cart,
                        'SubTotal': context.state.SubTotal,
                        'Shipping': context.state.Shipping,
                        'Discount': context.state.Discount,
                        'Total': context.state.Total
                        }
        const payload1 = payload
        const payload2 = cart
        const merge = Object.assign(payload1, payload2)
        const final = JSON.stringify(merge)
        this.$axios.setHeader('Content-Type', 'application/json')
        this.$gtm.push({ event: 'ContToPayku',
            SubTotal: context.state.SubTotal,
            Shipping: context.state.Shipping,
            Total: context.state.Total
          });
        const response = await this.$axios.$post('/api/main/order/', final)
        window.location.replace(response.url)
    }
}

export const getters = {
    ProductsinCart(state){
        return state.total_product
    },
    CartProducts(state){
        return state.cart
    },
    TotalPrice(state){
        var total_price = {'subtotal': state.SubTotal,
                            'shipping': state.Shipping,
                            'discount': state.Discount,
                            'total': state.Total}
        return total_price
    },
    CartMessage(state){
        return state.cart_message
    },
    GetCheckStore(state){
        return state.cart_store
    },
    StoreErrorModal(state){
        return state.store_error
    }
}