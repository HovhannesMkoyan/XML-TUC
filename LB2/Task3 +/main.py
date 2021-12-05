import xml.sax

articleIds = []

class ConsistencyHandler(xml.sax.ContentHandler):
    def startElement(self, tag, attrs):  # targets opening elements
        if tag == 'article':
            articleIds.append(attrs['id'])

def detectDuplications():
    for id in articleIds:
        duplicatesNumber = 0
        for possibleDuplicateId in articleIds:
            if id == possibleDuplicateId:
                duplicatesNumber += 1
        if duplicatesNumber != 1:
            print(f"Article ID {id} repeats {duplicatesNumber} times")
        removeFromList(id)

def removeFromList(id):
    for value in articleIds:
        if value == id:
            articleIds.remove(id)

handler = ConsistencyHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries.xml')
detectDuplications()
