import ontospy
from ontospy.ontodocs.viz.viz_html_single import *

#documentação da ontologia
g = ontospy.Ontospy("Periodic_Table.rdf")

v = HTMLVisualizer(g) # => instantiate the visualization object
v.build() # => render visualization. You can pass an 'output_path' parameter too
v.preview() # => open in browser

#ontospy gendocs pubs.ttl