import xml.sax
from xml.sax import handler

class DeliveriesHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = "----" + self.current
        
    def characters(self, content):
        self.current = "----" + self.current
        # print(content)
        

handler = DeliveriesHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml')
        
