import xml.sax
import sys

class IndentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentStudent = []
        self.students = {}

    def startElement(self, tag, attrs):  # targets opening elements
        if tag == 'assessment':
            if attrs['verbal'] == "very good":
                self.students.append()
            print("<{tag}>")
        

    def endElement(self, tag):  # targets closing elements
        pass
           

    def characters(self, data):  # targets element text content
        print(data.split())
        #self.currentStudent.append(data.split())

    def printStudents(self):
        print(self.currentStudent)

handler = IndentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/TUC/XML/LB2/deliveries.xml')
handler.printStudents()
