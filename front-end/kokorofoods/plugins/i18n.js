export default function ({ app, store }) {
    // onLanguageSwitched called right after a new locale has been set
    app.i18n.onLanguageSwitched = (oldLocale, newLocale) => {
        store.dispatch('StoreChange', newLocale)
        store.dispatch('StoreCatalogChange',newLocale)
        console.log(oldLocale, newLocale)
    }
  }