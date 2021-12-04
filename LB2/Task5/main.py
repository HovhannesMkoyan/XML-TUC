import xml.dom.minidom

domtree = xml.dom.minidom.parse("/Users/hovhannesmkoyan/Desktop/XML/LB2/Task5/deliveries.xml")
group = domtree.documentElement # this is the top element
articles = group.getElementsByTagName('article')

resultDictionary = {}

def manipulate():
    for article in articles:
        supplier = article.getElementsByTagName('supplier')[0].childNodes[0].nodeValue
        resultDictionary[supplier] = []
        resultDictionary[supplier].append(article.getElementsByTagName('name')[0].childNodes[0].nodeValue)
        
        # supplierProduct = article.getElementsByTagName('name')[0].childNodes[0].nodeValue
        # outputText = f"{supplier} supplies: {supplierProduct}"
        # for iarticle in articles:
        #     isupplier = iarticle.getElementsByTagName('supplier')[0].childNodes[0].nodeValue
        #     isupplierProduct = iarticle.getElementsByTagName('name')[0].childNodes[0].nodeValue
        #     if supplier == isupplier and supplierProduct != isupplierProduct:
        #         outputText += " " + isupplierProduct
            
        
def printResult():
    manipulate()
    print(resultDictionary)


printResult()