import xml.sax
from xml.sax import handler

class AnythingHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentTag = ""

    def startElement(self, tag, attrs): # triggers when reading a tag
        self.currentTag = tag

    def characters(self, content):
        
        

handler = AnythingHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml')
        
