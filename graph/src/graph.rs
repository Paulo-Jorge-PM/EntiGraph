use oxigraph::MemoryStore;
use oxigraph::model::*;
use oxigraph::sparql::QueryResults;


fn graph() {
    let store = MemoryStore::new();

    // insertion
    let ex = NamedNode::new("http://example.com")?;
    let quad = Quad::new(ex.clone(), ex.clone(), ex.clone(), None);
    store.insert(quad.clone());

    // quad filter
    let results: Vec<Quad> = store.quads_for_pattern(Some(ex.as_ref().into()), None, None, None).collect();
    assert_eq!(vec![quad], results);

    // SPARQL query
    if let QueryResults::Solutions(mut solutions) =  store.query("SELECT ?s WHERE { ?s ?p ?o }")? {
        assert_eq!(solutions.next().unwrap()?.get("s"), Some(&ex.into()));
    }
}
