import xml.sax
import sys

class IndentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.isClosed = False
        self.indent = 0
        self.lastNodeWasText = False

    def startElement(self, tag, attrs): # targets opening elements        
        if self.isClosed:
            sys.stdout.write('\n' + self.indent * " ")
            self.isClosed = False
        self.indent += 1 + len(tag)

        sys.stdout.write('<' + tag)
        first = True

        if len(attrs.getNames()) != 0:
            for name in attrs.getNames():
                if not first:
                    sys.stdout.write('\n'+self.indent*" ")
                first = False
                sys.stdout.write(" " + name + "=\"" + attrs.getValue(name) + "\"")
                self.isClosed = True

        sys.stdout.write(">")
        self.lastNodeWasText = False

    def endElement(self, tag): # targets closing elements
        self.isClosed = True
        sys.stdout.write("</" + tag + ">")
        self.indent -= 1+len(tag)
        self.lastNodeWasText = False

    def characters(self, data): # targets element text content
        data = data.strip()

        if(len(data) > 0):
            if self.isClosed and not self.lastNodeWasText:
                sys.stdout.write(self.indent * " ")
                self.isClosed = False
            sys.stdout.write(data)
            self.isClosed = True

        self.lastNodeWasText = True


handler = IndentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/Task1/deliveries.xml')
