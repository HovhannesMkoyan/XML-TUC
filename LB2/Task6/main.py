import xml.dom.minidom
import random

articleIds = []
dictionary = {}

def adjust(group):
    document = xml.dom.minidom.Document()

    # Deliveries element
    topElement = document.createElement("deliveries")
    topElement.setAttribute("xmlns", 'urn:myspace:deliveries')
    topElement.setAttribute("xmlns:xsi", 'http://www.w3.org/2001/XMLSchema-instance')
    topElement.setAttribute("xsi:schemaLocation", 'urn:myspace:deliveries deliveries.xsd')    

    articles = group.getElementsByTagName('article')
    for item in articles:
        # Article element
        id = insertOrGenerate(item.getAttribute('id'))
        articleElement = document.createElement("article")
        articleElement.setAttribute("id", str(id))

        # Name element
        nameElement = document.createElement("name")
        nameElementText = document.createTextNode(item.getElementsByTagName('name')[0].childNodes[0].nodeValue)
        nameElement.appendChild(nameElementText)
        articleElement.appendChild(nameElement)

        # Price element
        priceElement = document.createElement("price")
        priceElementText = document.createTextNode(item.getElementsByTagName('price')[0].childNodes[0].nodeValue)
        priceElement.appendChild(priceElementText)
        priceElement.setAttribute("unitprice", item.getElementsByTagName('price')[0].getAttribute('unitprice'))
        articleElement.appendChild(priceElement)

        # Supplier element
        supplierElement = document.createElement("supplier")
        supplierElementText = document.createTextNode(item.getElementsByTagName('supplier')[0].childNodes[0].nodeValue)
        supplierElement.appendChild(supplierElementText)
        articleElement.appendChild(supplierElement)

        topElement.appendChild(articleElement)

    return topElement


def insertOrGenerate(id):
    if id not in articleIds:
        articleIds.append(id)
        return id
    else:
        newId = random.randint(1000, 9999)
        insertOrGenerate(newId)
        return newId

domtree = xml.dom.minidom.parse("/Users/hovhannesmkoyan/Desktop/XML/LB2/deliveries1.xml")
group = domtree.documentElement  # this is the top element
adjustedXML = adjust(group)
print(adjustedXML.toprettyxml())

