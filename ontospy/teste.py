import ontospy
from ontospy.ontodocs.viz.viz_html_single import *

g = ontospy.Ontospy("Periodic_Table.rdf")
p = ontospy.Ontospy("pubs.ttl")

def map_list(lis):
    return list(map(lambda x: x[0].split("#")[1], lis))

def map_classif(lis):
    return list(map(lambda x: (x[1].split("#")[1], x[0].split("#")[1]), lis))    

def map_classes(lis):
    return list(map(lambda x: x.split("#")[1], lis)) 

elems = g.sparql("select * where {?s rdf:type :Element}")
classif = g.sparql("select * where { ?e :classification ?o}")

print("\nÁrvore das classes da ontologia de publicações:\n")
p.printClassTree()
print("\nNúmero de triplos da onotlogia de publicações: " + str(p.triplesCount()))
print("\nElementos da Tabela Periódica:\n")
print(map_list(elems))
print("\nClassificação de cada Elemento:\n")
print(map_classif(classif))



