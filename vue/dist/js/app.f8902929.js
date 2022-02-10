(function(t){function e(e){for(var s,i,l=e[0],o=e[1],c=e[2],d=0,p=[];d<l.length;d++)i=l[d],Object.prototype.hasOwnProperty.call(n,i)&&n[i]&&p.push(n[i][0]),n[i]=0;for(s in o)Object.prototype.hasOwnProperty.call(o,s)&&(t[s]=o[s]);u&&u(e);while(p.length)p.shift()();return r.push.apply(r,c||[]),a()}function a(){for(var t,e=0;e<r.length;e++){for(var a=r[e],s=!0,l=1;l<a.length;l++){var o=a[l];0!==n[o]&&(s=!1)}s&&(r.splice(e--,1),t=i(i.s=a[0]))}return t}var s={},n={app:0},r=[];function i(e){if(s[e])return s[e].exports;var a=s[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.m=t,i.c=s,i.d=function(t,e,a){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var s in t)i.d(a,s,function(e){return t[e]}.bind(null,s));return a},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],o=l.push.bind(l);l.push=e,l=l.slice();for(var c=0;c<l.length;c++)e(l[c]);var u=o;r.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var s=a("2b0e"),n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-app",[a("v-content",[a("Search")],1)],1)},r=[],i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",[a("v-row",{staticClass:"text-center"},[a("v-col",{staticClass:"mb-4"},[a("div",{staticClass:"search",attrs:{id:"search"}},[t.loading?a("div",{attrs:{id:"loading-icon-search"}},[a("v-progress-circular",{staticClass:"ml-2",attrs:{indeterminate:t.loading,value:0,size:"24"}})],1):t._e(),a("br"),a("br"),a("select",{attrs:{name:"classes",id:"classes"},on:{input:function(e){return t.classeOption(e)}}},[a("option",{staticClass:"disabled-option",attrs:{disabled:"",selected:""}},[t._v("Procurar artigos que mencionem...")]),t._l(t.classes,(function(e,s){return a("option",{key:s,domProps:{value:e.id}},[t._v(t._s(e.text))])}))],2),t.subclasses?a("span",[a("br"),a("select",{attrs:{name:"subclasses",id:"subclasses"},on:{input:function(e){return t.subclassOption(e)}}},[a("option",{staticClass:"disabled-option",attrs:{disabled:"",selected:""}},[t._v("Filtrar "+t._s(t.activeClasse.text)+" que mencionem...")]),t._l(t.subclassesFilter,(function(e,s){return a("option",{key:s,domProps:{value:e.row}},[t._v(t._s(e.row.charAt(0).toUpperCase()+e.row.slice(1)))])}))],2)]):t._e(),t.activeSubclasses?a("span",[a("br"),a("select",{attrs:{name:"subclasses3",id:"subclasses3"},on:{input:function(e){return t.filtroOption(e)}}},[a("option",{staticClass:"disabled-option",attrs:{disabled:"",selected:""}},[t._v("Filtrar resultados por...")]),t._l(t.filters,(function(e,s){return a("option",{key:s,domProps:{value:e.value}},[t._v(t._s(e.text))])}))],2)]):t._e(),t.filter?a("span",[a("br"),a("input",{directives:[{name:"model",rawName:"v-model",value:t.inputFilter,expression:"inputFilter"}],attrs:{id:"searchInput",type:"text",placeholder:"Search..."},domProps:{value:t.inputFilter},on:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.inputOption(e)},input:function(e){e.target.composing||(t.inputFilter=e.target.value)}}}),a("button",{attrs:{type:"button"},on:{click:function(e){return t.inputOption()}}},[a("i",{staticClass:"fa fa-search"})])]):t._e(),t.loading?a("div",[a("br"),a("v-progress-circular",{staticClass:"ml-2",attrs:{indeterminate:t.loading,value:0,size:"24"}}),a("span",{staticStyle:{color:"gray"}},[t._v(" Wait please, loading data...")])],1):t._e()])])],1),t.tableCount>0?a("v-row",{staticClass:"text-center"},[a("v-col",{staticClass:"mb-4"},[a("h2",[t._v("Resultados: "+t._s(t.tableCount))]),a("br"),a("v-btn",{attrs:{color:"primary"},on:{click:function(e){return t.download()}}},[t._v("Download")]),a("p",{staticStyle:{color:"gray:font-size:10px","text-align":"center","margin-top":"25px"}},[t._v("*Versão web limitada a "+t._s(t.limit)+" resultados - efetue download para dataset completo")])],1)],1):t._e(),a("br"),t.tableHasData?a("v-card",[a("v-card-title",[t._v(" Dados "),a("v-spacer"),a("v-text-field",{attrs:{"append-icon":"mdi-magnify",label:"Search","single-line":"","hide-details":""},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.hdados,items:t.table,search:t.search,"footer-props":{"items-per-page-options":[25,50,100,200,500,-1],"items-per-page-text":"Resultados por página:"},"items-per-page":10,loading:t.loading},scopedSlots:t._u([{key:"item.sourceUrl",fn:function(e){return[a("b",[a("a",{attrs:{set:t.id=e.item.sourceUrl,href:e.item.sourceUrl,target:"_blank"}},[t._v(" OPEN ")])])]}},{key:"item.link",fn:function(e){return[a("b",[a("a",{attrs:{href:e.item.link,target:"_blank"}},[t._v(" URL ORIGINAL ")])])]}}],null,!1,3707964962)})],1):t._e(),a("br"),a("v-row",{staticClass:"text-center"},[a("v-col",{staticClass:"mb-4"},[a("blockquote",{attrs:{id:"search-note"}},[t._v("For SPARQL queries go to "),a("a",{attrs:{href:"/sparql?q=SELECT%20DISTINCT%20?s%20WHERE%20%7B%20?s%20?p%20?o%20%7D&project=project1&uri=http://sparql.entigraph.di.pt/corpus",target:"_blank"}},[t._v("API")]),t._v(".")])])],1)],1)},l=[],o=(a("4de4"),a("7db0"),a("caad"),a("d81d"),a("4fad"),a("b64b"),a("d3b7"),a("3ca3"),a("ddb0"),a("2b3d"),a("3835")),c=(a("96cf"),a("1da1")),u=a("bc3a"),d=a.n(u),p=a("cdd9").graph+"?q=",b=a("cdd9").uri,h={name:"Search",data:function(){return{search:"",hdados:[{text:"URL",value:"sourceUrl"},{text:"User",value:"userName"},{text:"Date",value:"dateCreated"},{text:"Type",value:"typePost"},{text:"Sentiment",value:"sentimentAnalysis"},{text:"Text",value:"text"}],classes:[{text:"Animais",id:"animal",subclasses:["Animal","animal"]},{text:"Pessoas",id:"personName",subclasses:["Person","personName"]},{text:"Palavras-chave",id:"keyword",subclasses:["Keyword","keyword"]},{text:"Partidos",id:"politicalParty",subclasses:["PoliticalParty","politicalParty"]},{text:"Cidades",id:"city",subclasses:["City","city"]},{text:"Países",id:"country",subclasses:["Country","country"]},{text:"Continentes",id:"continent",subclasses:["Continent","continent"]},{text:"Outros Lugares",id:"otherPlace",subclasses:["OtherPlace","otherPlace"]},{text:"Dias da Semana",id:"weekday",subclasses:["Weekday","weekday"]},{text:"Meses",id:"month",subclasses:["Month","month"]},{text:"Entidades",id:"entity",subclasses:["Entity","entity"]},{text:"Clubes de Futebol",id:"footbal",subclasses:["Football","footbal"]},{text:"Desportos",id:"sport",subclasses:["Sport","sport"]},{text:"Tags do Jornal",id:"tag",subclasses:["Tag","tag"]},{text:"Marcas de Produtos",id:"brand",subclasses:["Brand","brand"]},{text:"Canais de TV",id:"tvChannel",subclasses:["TvChannel","tvChannel"]},{text:"Marcas de Carros",id:"carBrand",subclasses:["CarBrand","carBrand"]},{text:"Desportos",id:"sport",subclasses:["Sport","sport"]},{text:"Minorias",id:"minority",subclasses:["Minority","minority"]},{text:"Etnias",id:"ethnicity",subclasses:["Ethnicity","ethnicity"]},{text:"Religiões",id:"religion",subclasses:["Religion","religion"]}],filters:[{text:"Contém palavra igual a...",value:"keywordIgual"}],activeClasse:null,subclasses:null,activeSubclasses:null,subclasses3:null,table:null,tableHasData:!1,tableCount:null,loading:!1,filter:null,inputFilter:null,limit:"5000",query:null,db:"project1",articlePage:"http://minors.ilch.uminho.pt/articles"}},computed:{subclassesFilter:function(){return this.subclasses.filter((function(t){return!["311","112","1980s","1981","702","99"].includes(t.row)}))},metadados:function(){var t="";return t="indiferenciado"==this.db?this.articlePage+"?db=indiferenciado&id=":this.articlePage+"?id=",t}},mounted:function(){},created:function(){var t=Object(c["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:t.prev=0,t.next=6;break;case 3:return t.prev=3,t.t0=t["catch"](0),t.abrupt("return",t.t0);case 6:case"end":return t.stop()}}),t,null,[[0,3]])})));function e(){return t.apply(this,arguments)}return e}(),methods:{classeOption:function(t){var e=t.target.value,a=this.findObject(this.classes,"id",e);this.activeClasse=a;var s="\nPREFIX : <"+b+"#>\nSELECT DISTINCT ?row WHERE {\n  ?article a :"+a.subclasses[0]+" .\n  ?article :"+a.subclasses[1]+" ?row .\n}\nORDER BY ?row\n      ";this.loading=!0,this.subclasses=null,this.activeSubclasses=null,this.filter=null,this.inputFilter=null,this.queryClasse(s,a),this.tableQuery(a.subclasses[0],a.subclasses[1],"","")},subclassOption:function(t){this.loading=!0,this.activeSubclasses=null,this.filter=null,this.inputFilter=null,this.activeSubclasses=t.target.value,this.tableQuery(this.activeClasse.subclasses[0],this.activeClasse.subclasses[1],this.activeSubclasses,"")},filtroOption:function(t){this.filter=t.target.value,this.inputFilter=null},inputOption:function(){this.loading=!0;var t="";"dataMaior"==this.filter?t="\n        FILTER(YEAR(?dateCreated) >= "+this.inputFilter+") .":"dataMenor"==this.filter?t="\n        FILTER(YEAR(?dateCreated) <= "+this.inputFilter+") .":"dataIgual"==this.filter?t="\n        FILTER( YEAR(?dateCreated) = "+this.inputFilter+") .":"minoriaIgual"==this.filter?t='\n        ?article :referesMinority ?Minority .\n        ?Minority :minority ?minority .\n        FILTER (CONTAINS(?minority , "'+this.inputFilter.toLowerCase()+'")) .':"keywordIgual"==this.filter&&(t='\n        FILTER (CONTAINS(?text , "'+this.inputFilter.toLowerCase()+'")) .'),""!=t&&this.tableQuery(this.activeClasse.subclasses[0],this.activeClasse.subclasses[1],this.activeSubclasses,t)},queryClasse:function(t,e){this.query=encodeURIComponent(t);var a=p+this.query,s=this;d()({method:"GET",url:a,headers:{Accept:"application/json"}}).then((function(t){var a=t.data;s.newSubClasse(a,e)})).catch((function(t){console.log(t)}))},newSubClasse:function(t,e){var a=t;this.subclasses=a},findObject:function(t,e,a){return t.find((function(t){return t[e]===a}))},myNormalize:function(t){return t.results.bindings.map((function(t){for(var e={},a=0,s=Object.entries(t);a<s.length;a++){var n=Object(o["a"])(s[a],2),r=n[0],i=n[1];e[r]=i.value}return e}))},normalizeArray:function(t){return t.results.bindings.map((function(t){for(var e=[],a=0,s=Object.entries(t);a<s.length;a++){var n=Object(o["a"])(s[a],2),r=(n[0],n[1]);e.push(r.value)}return e}))},tableQuery:function(t,e,a,s){this.tableCounter(t,e,a,s);var n="\nPREFIX : <"+b+"#>\nSELECT DISTINCT ?text (SAMPLE(?article) AS ?article) (SAMPLE(?typePost) AS ?typePost) (SAMPLE(?dateCreated) AS ?dateCreated) (SAMPLE(?id) AS ?id) (SAMPLE(?user) AS ?user) (SAMPLE(?sentimentAnalysis) AS ?sentimentAnalysis) (SAMPLE(?sourceUrl) AS ?sourceUrl) (SAMPLE(?userName) AS ?userName) WHERE {\n  ?article a :Article .\n  ?article :dateCreated ?dateCreated .\n  ?article :text ?text .\n  ?article :id ?id .\n  ?article :user ?user .\n  ?article :typePost ?typePost .\n  ?article :sourceUrl ?sourceUrl .\n  ?article :sentimentAnalysis ?sentimentAnalysis .\n  ?article :userName ?userName .\n  ";n=""!=a?n+"\n    ?article :referes"+t+" ?subclass .\n    ?subclass :"+e+' "'+a+'" .':n+"\n    ?article :referes"+t+" ?classe .",""!=s&&(n+=s),n=n+"\n}\nGROUP BY ?text\nLIMIT "+this.limit+"\n    ",this.query=encodeURIComponent(n);var r=this;d()({method:"GET",url:p+this.query,headers:{Accept:"application/json"},data:{query:n}}).then((function(t){var e=t.data;r.setTable(e)})).catch((function(t){console.log(t)}))},tableCounter:function(t,e,a,s){var n="\nPREFIX : <"+b+"#>\nSELECT (COUNT(DISTINCT ?text) as ?count) WHERE {\n  ?article a :Article .\n  #?article :dateCreated ?dateCreated .\n  ?article :text ?text .\n  #?article :sourceUrl ?sourceUrl .\n  ";n=""!=a?n+"\n    ?article :referes"+t+" ?subclass .\n    ?subclass :"+e+' "'+a+'" .':n+"\n    ?article :referes"+t+" ?classe .",""!=s&&(n+=s),n+="\n}\n#GROUP BY ?text\n    ",this.query=encodeURIComponent(n);var r=this;d()({method:"GET",url:p+this.query,headers:{Accept:"application/json"}}).then((function(t){var e=t.data;r.setCountTable(e)})).catch((function(t){console.log(t)}))},setTable:function(t){this.table=t,Object.keys(t[0]).length>0?this.tableHasData=!0:this.tableHasData=!1,this.loading=!1},setCountTable:function(t){this.tableCount=t[0].count},download:function(){var t=this;d()({method:"GET",url:p+this.query,headers:{Accept:"application/json"}}).then((function(e){t.forceFileDownload(e)})).catch((function(t){console.log(t)}))},forceFileDownload:function(t){var e=window.URL.createObjectURL(new Blob(JSON.stringify([t.data]))),a=document.createElement("a");a.href=e,a.setAttribute("download","data.json"),document.body.appendChild(a),a.click()}}},f=h,v=a("2877"),m=a("6544"),y=a.n(m),g=a("8336"),C=a("b0af"),x=a("99d9"),S=a("62ad"),w=a("a523"),P=a("8fea"),E=a("490a"),_=a("0fd9"),O=a("2fa4"),A=a("8654"),T=Object(v["a"])(f,i,l,!1,null,null,null),k=T.exports;y()(T,{VBtn:g["a"],VCard:C["a"],VCardTitle:x["a"],VCol:S["a"],VContainer:w["a"],VDataTable:P["a"],VProgressCircular:E["a"],VRow:_["a"],VSpacer:O["a"],VTextField:A["a"]});var R={name:"App",components:{Search:k}},F=R,I=a("7496"),j=a("a75b"),L=Object(v["a"])(F,n,r,!1,null,null,null),q=L.exports;y()(L,{VApp:I["a"],VContent:j["a"]});var M=a("f309");s["a"].use(M["a"]);var U=new M["a"]({});s["a"].config.productionTip=!1,new s["a"]({vuetify:U,render:function(t){return t(q)}}).$mount("#app")},cdd9:function(t,e){t.exports.lhost="http://127.0.0.1:8080",t.exports.graphdb="http://127.0.0.1:7200",t.exports.flaskSparql="http://minors.ilch.uminho.pt/sparql",t.exports.flaskDownload="http://minors.ilch.uminho.pt/api/sparql",t.exports.graph="http://localhost:3888/sparql",t.exports.uri="http://sparql.entigraph.di.pt/corpus"}});
//# sourceMappingURL=app.f8902929.js.map