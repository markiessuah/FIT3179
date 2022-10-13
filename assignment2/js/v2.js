var spec = "https://raw.githubusercontent.com/markiessuah/FIT3179/main/homework2/js/visualization.vl.json";
vegaEmbed('#vis', spec).then(function(result) {
  // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);
