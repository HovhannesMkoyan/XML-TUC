import xml.sax
import sys


class ToHTMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.row = ""

    def startElement(self, tag, attrs):
        if tag == 'article':
            sys.stdout.write(f"<tr><td>{attrs['id']}</td>")
        elif tag == 'name' or tag == 'price' or tag == 'supplier':
            sys.stdout.write("<td>")

    def endElement(self, tag):
        if tag == 'article':
            sys.stdout.write("</tr>")
            print(self.row)
            self.row = ""
        elif tag == 'name' or tag == 'price' or tag == 'supplier':
            sys.stdout.write("</td>")

    def characters(self, data):
        sys.stdout.write(data.strip())


handler = ToHTMLHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)

print("<html><head><title>Deliveries</title></head>")
print("<body><h1>Deliveries</h1><hr>")
print("<table border=\"1\"><tr><th>Number</th><th>Article</th><th>Price</th><th>Supplier</th></tr>")
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml')
print("</table>")
print("</body>")
print("</html>")
