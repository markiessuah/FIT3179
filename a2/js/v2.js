var spec = "https://raw.githubusercontent.com/markiessuah/FIT3179/main/a2/js/choropleth_map.json";
vegaEmbed('#vis2', spec).then(function(result) {
  // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);
