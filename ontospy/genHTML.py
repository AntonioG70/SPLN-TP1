import ontospy
from ontospy.ontodocs.viz.viz_html_single import *

#documentação da ontologia
g = ontospy.Ontospy("Periodic_Table.rdf")

v = HTMLVisualizer(g) 
v.build() 
v.preview() 

#ontospy gendocs pubs.ttl