#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyoxigraph import *

store = MemoryStore()
ex = NamedNode('http://example/')
schema_name = NamedNode('http://schema.org/name')
store.add(Quad(ex, schema_name, Literal('example')))

for binding in store.query('SELECT ?name WHERE { <http://example/> <http://schema.org/name> ?name }'):
    print(binding['name'].value)

if __name__ == '__main__':
	pass#main = Main()
