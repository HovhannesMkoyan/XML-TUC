import xml.dom.minidom

domtree = xml.dom.minidom.parse("/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml")
print(domtree.toxml())
