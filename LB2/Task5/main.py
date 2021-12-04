import xml.dom.minidom

dictionary = {}

def transform(articles):
    for article in articles:
        supplier = article.getElementsByTagName('supplier')[0].childNodes[0].nodeValue
        if supplier not in dictionary:
            dictionary[supplier] = []
        dictionary[supplier].append(article.getElementsByTagName('name')[0].childNodes[0].nodeValue)
            
def printSuppliersWithProducts():
    print(dictionary)


domtree = xml.dom.minidom.parse("/Users/hovhannesmkoyan/Desktop/XML/LB2/Task5/deliveries.xml")
group = domtree.documentElement # this is the top element
articles = group.getElementsByTagName('article')

transform(articles)
printSuppliersWithProducts()