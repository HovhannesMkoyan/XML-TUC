import xml.sax
import sys


class IndentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.firstLevelIndent = 3
        self.secondLevelIndent = 7
        self.thirdLevelIndent = 11

    def startElement(self, tag, attrs):  # targets opening elements
        if tag == 'deliveries':
            print(self.firstLevelIndent * " " + f"<{tag}>")
        elif tag == 'article':
            print(self.secondLevelIndent * " " + f"<{tag} id=\"{attrs['id']}\">")
        elif tag == 'name' or tag == 'supplier':
            sys.stdout.write(self.thirdLevelIndent * " " + f"<{tag}>")
        elif tag == 'price':
            sys.stdout.write(self.thirdLevelIndent * " " + f"<{tag} unitprice=\"{attrs['unitprice']}\">")

    def endElement(self, tag):  # targets closing elements
        if tag == 'deliveries':
            print(self.firstLevelIndent * " " + f"</{tag}>")
        elif tag == 'article':
            print(self.secondLevelIndent * " " + f"</{tag}>")
        elif tag == 'name' or tag == 'price' or tag == 'supplier':
            print(f"</{tag}>")

    def characters(self, data):  # targets element text content
        sys.stdout.write(data.strip())


handler = IndentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml')
