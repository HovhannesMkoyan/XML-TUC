import xml.sax
import sys

class CompactHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.closed = False
        self.indent = 0
        self.lastNodeWasText = False

    def startElement(self, tag, attrs):
        if self.closed:
            sys.stdout.write('\n'+self.indent*" ")
            self.closed = False
        self.indent += 1+len(tag)

        sys.stdout.write(tag+'[')
        first = True

        for name in attrs.getNames():
            if not first:
                sys.stdout.write('\n'+self.indent*" ")
            first = False
            sys.stdout.write('@'+name+'['+attrs.getValue(name)+']')
            self.closed = True

        self.lastNodeWasText = False

    def endElement(self, tag):
        self.closed = True
        sys.stdout.write(']')
        self.indent -= 1+len(tag)
        self.lastNodeWasText = False

    def characters(self, data):
        data = data.strip()

        if(len(data) > 0):
            if self.closed and not self.lastNodeWasText:
                sys.stdout.write('\n'+self.indent*" ")
                self.closed = False
            sys.stdout.write(data)
            self.closed = True

        self.lastNodeWasText = True

handler = CompactHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/Task1/deliveries.xml')
