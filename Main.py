
from builtins import str

print("Write the following data")
#productName=input("Product Name")
#productPriceNet=input("Product Price Net")
#clientEmail=input("Client Email")
#clientPhone=input("Client phone")


try:
    productName=str(input("Product Name"))
    print(productName,",",type(productName))
except:
    print("Problem with the price data type")
    exit()

try:
    # Calculating the tax
    productPriceNet = float(input("Product Price Net"))
    print(productPriceNet, ",", type(productPriceNet))
    grossPrice = (productPriceNet * 0.23) + productPriceNet
except:
    print("Problem with the price data type")
    exit()

try:
    clientEmail=str(input("Client Email"))
    print(clientEmail, ",", type(clientEmail))
except:
    print("Problem with the price data type")
    exit()

try:
    clientPhone=int(input("Client phone"))
    print(clientPhone, ",", type(clientPhone))
except:
    print("Problem with the price data type")
    exit()




information = {"productName": productName,
               "netPrice": productPriceNet,
               "grossPrice": grossPrice,
               "clientEmail": clientEmail,
               "clientPhone": clientPhone}

print(information)


print("Now testing the Morgan's law:")
#Morgan's Law

p=[True,True,False,False]
q=[True,False,True,False]

x = not(p and q)==(not p) or (not q)
y = not(p or q)==((not p) and (not q))
print('x is :', x, '\ny is :' ,y)



