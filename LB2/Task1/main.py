import xml.sax
import sys

class IndentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentElement = ""
        self.firstLevelIndent = 3
        self.secondLevelIndent = 6
        self.thirdLevelIndent = 9

    def startElement(self, tag, attrs): # targets opening elements  
        self.currentElement = tag
        if tag == 'deliveries':
            print(self.firstLevelIndent * " " + f"<{tag}>")
        elif tag == 'article':
            print(self.secondLevelIndent * " " + f"<{tag} id=\"{attrs['id']}\">")
        elif tag == 'name' or tag == 'supplier':
                print(self.thirdLevelIndent * " " + f"<{tag}>")
        elif tag == 'price':
             print(self.thirdLevelIndent * " " + f"<{tag} unitprice=\"{attrs['unitprice']}\">")

    def endElement(self, tag): # targets closing elements
        self.isClosed = True
        if tag == 'deliveries':
            print(self.firstLevelIndent * " " + f"</{tag}>")
        elif tag == 'article':
            print(self.secondLevelIndent * " " + f"</{tag}>")
        elif tag == 'name' or tag == 'supplier' or tag == 'price':
            print(self.thirdLevelIndent * " " + f"</{tag}>")

    # def characters(self, data): # targets element text content
    #     data = data.strip()

    #     if(len(data) > 0):
    #         if self.isClosed and not self.lastNodeWasText:
    #             sys.stdout.write(self.indent * " ")
    #             self.isClosed = False
    #         sys.stdout.write(data)
    #         self.isClosed = True

    #     self.lastNodeWasText = True


handler = IndentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml')
