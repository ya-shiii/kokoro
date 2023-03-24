
export const state = () => ({
    ProductData: [],
    DestacadoData: [],
    store: null,
    AllProducts: []
  })

export const mutations = {
    addProduct(state, products){
        state.ProductData = products
    },
    addDestacados(state, destacados){
        state.DestacadoData = destacados
    },
    SelectStore(state, store_id){
        state.store = store_id
    },
    addAllProducts(state, allproducts){
        state.AllProducts = allproducts
    }
}

export const actions = {
    async nuxtServerInit( {commit, getters} ) {
        const lang = this.$i18n.locale
        if (lang == 'es') {
            commit('SelectStore', '1')
        } else if (lang == 'en'){
            commit('SelectStore', '2')
        }
        const store_id = getters.GetStore
        const MasVendido = await this.$axios.$get('/api/main/product/?is_masvendido=true&store=' + store_id)
        const DestacadoData1 = await this.$axios.$get('/api/main/product/?is_destacado=true&store=' + store_id)
        commit('addDestacados', DestacadoData1)
        return commit('addProduct', MasVendido)
    },
    async StoreChange( { commit, getters }, lang){
        if (lang == 'es') {
            commit('SelectStore', '1')
        } else if (lang == 'en'){
            commit('SelectStore', '2')
        }
        const store_id = getters.GetStore
        const MasVendido = await this.$axios.$get('/api/main/product/?is_masvendido=true&store=' + store_id)
        const DestacadoData1 = await this.$axios.$get('/api/main/product/?is_destacado=true&store=' + store_id)
        commit('addDestacados', DestacadoData1)
        return commit('addProduct', MasVendido)
    },
    async StoreCatalogChange( { commit, getters}, lang) {
        if (lang == 'es') {
            commit('SelectStore', '1')
        } else if (lang == 'en'){
            commit('SelectStore', '2')
        }
        const store_id = getters.GetStore
        const allProducts = await this.$axios.$get('/api/main/product/?store=' + store_id)
        return commit('addAllProducts', allProducts)
    }
}


export const getters = {
    MasVendido(state){
        return state.ProductData
    },
    MasDestacadoG(state){
        return state.DestacadoData
    },
    GetStore(state){
        return state.store
    }
}
