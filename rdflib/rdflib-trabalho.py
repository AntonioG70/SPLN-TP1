import rdflib
import re

#  CARREGAR FICHEIRO
cidades = rdflib.Graph()

cidades.parse('cidades-completo.ttl', format='ttl')

def strip_prefix(s):
    return re.sub(r"^.*?#", "", s)

print(cidades.triples(1))

#  EXECUTAR QUERY
qres = cidades.query( """
                SELECT * WHERE {
                    ?c rdf:type :Cidade .
                    ?c :nome ?n .
                    ?c :distrito ?d
                } ORDER BY ?c
                """
                )

for row in qres:
    print(row)


#  ESCREVER FICHEIRO
cidades.serialize(destination='output.xml', format='xml')