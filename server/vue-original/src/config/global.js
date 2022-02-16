module.exports.lhost = "http://127.0.0.1:8080"
module.exports.graphdb = "http://127.0.0.1:7200"
//module.exports.flaskSparql = "http://127.0.0.1:8080/sparql"
//module.exports.flaskDownload = "http://127.0.0.1:8080/api/sparql"
module.exports.flaskSparql = "http://minors.ilch.uminho.pt/sparql"
module.exports.flaskDownload = "http://minors.ilch.uminho.pt/api/sparql"

//GET QUERY:
//module.exports.netlang_graphdb = "http://localhost:7200/repositories/netlang2?query="
//POST QUERY: send quuery body param, without encoding/normalizing as plain text.
module.exports.graph = "http://localhost:3888/sparql"
module.exports.uri = "http://sparql.entigraph.di.pt/corpus"

//For tests (to avoid CORS erros)
//module.exports.netlang_graphdb = "http://sparql.ilch.uminho.pt/repositories/netlang"
