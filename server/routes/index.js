var express = require('express');
var router = express.Router();
const oxigraph = require('oxigraph');
const fs = require('fs');
const path = require('path');

const child_process = require('child_process');


function python_cli(json_data) {
    let command = 'python3 -u ../run.py -w project1 -j \''+json_data+'\';'

    child_process.exec(command, (err, stdout, stderr) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(stdout);
      // check if generated file exists
      //let fileExists = require("fs").existsSync("/path/to/generated/file");
      //if (fileExists) {
        // do something with the file
      //}
    });
}




function amqp_consumer() {
    app.use(express.static(path.join(__dirname, '../my-app/dist')));

    // Consumer
    var q = 'hiperfolio';
    var open = require('amqplib').connect('amqp://localhost');
    open.then(function(conn) {
      return conn.createChannel();
    }).then(function(ch) {
      return ch.assertQueue(q).then(function(ok) {
        return ch.consume(q, function(msg) {
          if (msg !== null) {
            console.log("AMQP consumed!");
            console.log(msg.content.toString());

            python_cli(msg.content.toString());

            ch.ack(msg);
          }
        });
      });
    }).catch(console.warn);
}




const BindingMapToObject = (map) => {
  const obj = {};
  for (const item of [...map]) {
    const [
      key,
      value
    ] = item;
    obj[key] = value.value;
  }
  return obj;
}

function readOntology(fPath) {
    try {
        const data = fs.readFileSync(fPath, 'utf8');
        return data;
    } catch (err) {
      console.error(err)
      return "error";
    }
}

function doQuery(query, uri, project) {
    const ontologyPath = '../saves/'+project+'/ontology.ttl';
    let ontology = readOntology(ontologyPath);
    const store = new oxigraph.Store();
    //console.log(ontology);
    store.load(ontology, "text/turtle", uri);
    //store.load("<http://example.com> <http://example.com> <> .", "text/turtle", "http://example.com", oxigraph.namedNode("http://example.com/graph"));
    
    /*const ex = oxigraph.namedNode("http://example/");
    const schemaName = oxigraph.namedNode("http://schema.org/name");
    store.add(oxigraph.triple(ex, schemaName, oxigraph.literal("example")));
    var results = [];
    for (binding of store.query("SELECT ?name WHERE { <http://example/> <http://schema.org/name> ?name }")) {
        //console.log(binding.get("name").value);
        let item = binding.get("name").value;
        results.push(item);
    }*/
    
    //const r = store.query('PREFIX : <http://sparql.entigraph.di.pt/corpus#>select ?article where {?article a :Article.}');
    //console.log(r[0].get("article"));
    
    //let query = "PREFIX : <http://sparql.entigraph.di.pt/corpus#>select ?article ?text where {?article a :Article. ?article :text ?text.}";
    //let query = "SELECT DISTINCT ?s WHERE { ?s ?p ?o }";
    var results = [];
    for (binding of store.query(query)) {
        //console.log(JSON.stringify(binding));
        
        //console.log(Object.fromEntries(binding));
        //let item = binding.get("text").value;
        let item = BindingMapToObject(binding);
        results.push(item);
    }
    console.log(JSON.stringify(results));
    
    return results;
}

/* GET home page. */
router.get('/view', function(req, res, next) {
    res.send("API: <a href='http://localhost:3888/sparql?q=SELECT%20DISTINCT%20?s%20WHERE%20%7B%20?s%20?p%20?o%20%7D&uri=http://sparql.entigraph.di.pt/corpus&project=project1' target='_blank'>http://localhost:3888/sparql</a><br/>/sparql?query=xx will execute a sparql query and give JSON as response. Note: query should be url encoded.");
  //res.render('index', { title: 'Express' });
  
});

router.get('/', function(req, res, next) {
  //res.render('vue/index.html');
  res.sendFile(path.join(__dirname, '../views/index.html'));
  //res.sendFile("../views/vue/index.html", { root: __dirname })
  
});

router.post('/amqp', function(req, res, next) {
  //RABITMQ


  const data = req.body;

  console.log("Post received:")
  console.log(JSON.stringify(data))

var q = 'hiperfolio';
var open = require('amqplib').connect('amqp://localhost');

// Publisher
open.then(function(conn) {
  return conn.createChannel();
}).then(function(ch) {
  return ch.assertQueue(q).then(function(ok) {
    return ch.sendToQueue(q, Buffer.from(JSON.stringify(data)));
  });
}).catch(console.warn);

// Consumer
/*
var q = 'hiperfolio';
var open = require('amqplib').connect('amqp://localhost');
open.then(function(conn) {
  return conn.createChannel();
}).then(function(ch) {
  return ch.assertQueue(q).then(function(ok) {
    return ch.consume(q, function(msg) {
      if (msg !== null) {
        console.log("Consumed!!");
        console.log(msg.content.toString());
        ch.ack(msg);
      }
    });
  });
}).catch(console.warn);*/

  /*res.send({
    'data': data,
  });*/


});

/* GET home page. */
router.get('/sparql', function(req, res, next) {
    //e.g.:
    //uri: http://sparql.entigraph.di.pt/corpus
    //query: SELECT%20DISTINCT%20?s%20WHERE%20%7B%20?s%20?p%20?o%20%7D
    //query: PREFIX%20:%20%3Chttp://sparql.entigraph.di.pt/corpus#%3Eselect%20?article%20?text%20where%20%7B?article%20a%20:Article.%20?article%20:text%20?text.%7D
    
    let query = req.query.q;//encoded query
    
    
    if(req.query.uri) {
        var uri = req.query.uri;//ontology uri
    } else {
        var uri = "http://sparql.entigraph.di.pt/corpus";
    }
    
    if(req.query.project) {
        var project = req.query.project;//folder name at /saves
    } else {
        var project = "project1";
    }
    
    
    let data = doQuery(query, uri, project);
    res.send(data);
    
    //console.log(JSON.stringify(data));
    //res.send('Hello World!' + data[0]);
    //res.send("Data: "+JSON.stringify(data));
  //res.render('index', { title: 'Express' });
  
});

module.exports = router;
