// import i18n from './config/i18n'

export default {
     // Global page headers: https://go.nuxtjs.dev/config-head
     mode: 'universal',
     publicRuntimeConfig: {},
     privateRuntimeConfig: {
          UserAPI: process.env.USER_API,
          UserPass: process.env.USER_PASS
     },
     // server: {
     // host: '0'
     // },
     head: {
          title: 'kokorofoods',
          htmlAttrs: {
               lang: 'en'
          },
          meta: [
               { charset: 'utf-8' },
               { name: 'viewport', content: 'width=device-width, initial-scale=1' },
               { hid: 'description', name: 'description', content: '' }
          ],
          link: [
               { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
               { rel: "stylesheet", type: "text/css", href: "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" }
          ],
          script: [
               { src: 'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js' },
               { src: 'https://code.jquery.com/jquery-3.5.1.slim.min.js' },
               { src: 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js' },
               { src: '/js/freshchat/freshchat.js', body: true },
               { src: '/js/omnisend/omnisend.js', body: true },
               { src: 'https://ad.soicos.com/soicosjs.php?s=.js', body: true}
          ],
     },

     // Global CSS: https://go.nuxtjs.dev/config-css
     css: [
     ],
     // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
     plugins: [{ src: '~/plugins/i18n.js' }
     ],

     // Auto import components: https://go.nuxtjs.dev/config-components
     components: true,

     // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
     buildModules: [
          /* other modules */
     ],

     // Modules: https://go.nuxtjs.dev/config-modules
     modules: [
          '@nuxtjs/axios',
          '@nuxtjs/auth',
          '@nuxtjs/toast',
          '@nuxtjs/sentry',
          '@nuxtjs/i18n',
          '@nuxtjs/style-resources',
          '@nuxtjs/gtm',
     ],
     
     sentry: {
          dsn: 'https://d730917b754542a0bcaf90976ce4856c@o319134.ingest.sentry.io/5907089', // Enter your project's DSN here
          // Additional Module Options go here
          // https://sentry.nuxtjs.org/sentry/options
          config: {
               // Add native Sentry config here
               // https://docs.sentry.io/platforms/javascript/guides/vue/configuration/options/
          },
     },
     gtm: {
          id: 'GTM-58WH27C',
          pageTracking: true,
          enabled: true
        },
     i18n: {
          locales: ['en', 'es'],
          defaultLocale: 'es',
          strategy: 'prefix',
          seo: true,
          langDir: 'locales/',
          locales: [
               {
                    code: 'en',
                    name: 'English',
                    iso: 'en-US',
                    file: 'en.json'
               },
               {
                    code: 'es',
                    name: 'Spanish',
                    iso: 'es-ES',
                    file: 'es.json'
               }
          ],
          vueI18n: {
               locale: 'es',
               fallbackLocale: 'es',
               numberFormats: {
                    en: {
                         currency: {
                              style: 'currency',
                              currency: 'USD'
                         }
                    },
                    es: {
                         currency: {
                              style: 'currency',
                              currency: 'CLP',
                              currencyDisplay: 'symbol',
                              signDisplay: 'never'
                         }
                    }
               },
               dateTimeFormats: {
                    en: {
                      short: {
                        year: 'numeric',
                        month: 'numeric',
                        day: 'numeric'
                      },
                      long: {
                        year: 'numeric',
                        month: '2-digit',
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit'
                      }
                    },
                    es: {
                      short: {
                        year: 'numeric',
                        month: 'numeric',
                        day: 'numeric'
                      },
                      long: {
                        year: 'numeric',
                        month: '2-digit',
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit'
                      }
                    }
                  }
          }
     },

  auth: {
    strategies: {
        local: {
            endpoints: {
                login: {
                    url: '/api/user/token/',
                    method: 'post',
                    propertyName: 'token'
                },
                logout: {},
                user:{
                   url: '/api/user/account/',
                   method: 'get',
                   propertyName: 'results'
                }
            },
            tokenType: 'Token'
        }
    },
    redirect: {
     login: '/es/register',
     logout: '/es',
     callback: false,
     home: false
   }
},
router: {
    middleware: ['auth']
},
axios: {
    baseURL: 'https://api.kokorofoods.cl/'
},
toast: {
    position: 'top-center',
    iconPack: 'fontawesome',
    duration: 3000,
    register: [
      {
        name: 'defaultSuccess',
        message: (payload) =>
          !payload.msg ? 'Parece que todo salio bien' : payload.msg,
        options: {
          type: 'success',
          icon: 'check'
        }
      },
      {
        name: 'defaultError',
        message: (payload) =>
          !payload.msg ? 'Oops.. como el ajo.. algo paso' : payload.msg,
        options: {
          type: 'error',
          icon: 'times'
        }
      }
    ]
  },

     // Build Configuration: https://go.nuxtjs.dev/config-build
     build: {
     },
     serverMiddleware: [
          // Server-side redirects
          '~/serverMiddleware/redirects',
        ],
}