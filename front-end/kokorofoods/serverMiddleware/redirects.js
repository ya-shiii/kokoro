const redirects = [
    { from: '/ajo-negro-beneficios-y-propiedades/', to: '/es/ajonegro' },
    { from: '/donde-comprar/', to: '/tiendas' },
  ]

module.exports = function (req, res, next) {
  const host = req.headers.host;
  const fullUrl = req.url;
  var url = req.url.split('?')[0];
  var urlParams = null;
  if (req.url.includes("?")) {
    urlParams = '?' + req.url.split('?')[1]
  }

  const redirect = redirects.find(r => r.from === url)
  if (redirect) {
    var newLocation;
    if (urlParams) {
      newLocation = redirect.to + urlParams;
    } else {
      newLocation = redirect.to;
    }
    res.writeHead(301, {
      Location: newLocation
    });
    res.end()
  } else {
    next()
  }
}