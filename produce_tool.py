##Declaring global variables
global testcount
global totalprice
global producePrice
testcount = 0
totalprice = 0
producePrice = 0

##PriceFunction
def PriceFunction(producePrice):
    if producePrice > 100 :
        producePrice = producePrice - (producePrice * 0.05)
        return producePrice
    else :
        return producePrice


##Shipping Function
def ShippingFunction(producePounds):
    if producePounds < 5 :
        shippingCost = 3.50
        return shippingCost
    elif producePounds < 20 :
        shippingCost = 10
        return shippingCost
    else :
        shippingCost = 9.5 + (0.10*producePounds)
        return shippingCost


##Total Price Function
def TotalPriceFunction(producePrice):
    global totalprice
    totalprice = totalprice + producePrice
    return totalprice        
 

##Show menu##
def ShowMenu():
    global artichokes, carrots, beets, choice

    artichokes = input("Pounds of artichokes: ")
    carrots = input("Pounds of carrots: ")
    beets = input("Pounds of beets: ")
    print ("Main Menu")
    print ("Choose one of the following commands")
    print ("1. Submit")
    print ("2. Summary")
    print ("3. Reset")
    print ("4. Exit")
    choice = input ("Enter your command [1-4]: ")
  
    ProcessInput()
    

class InputProcessing:
  global ProcessInput
  #Method for executing the appropriate actions for the right commands
  #Method incomplete
  def ProcessInput():
      global testcount, totalprice, producePrice
      #Output
      if choice == 1:    
          artPrice = artichokes * 2.67
          carPrice = carrots * 1.49
          beePrice = beets * 0.67
          producePounds = artichokes + carrots + beets
          producePrice = artPrice + carPrice + beePrice
          testcount += 1
          totalprice += producePrice
          print ("Produce price: ", PriceFunction(producePrice))
          print ("Shipping cost: ", ShippingFunction(producePounds))
          print ("Total: " , PriceFunction(producePrice) + ShippingFunction(producePounds))
          ShowMenu()
      elif choice == 2:
          averageprice = TotalPriceFunction(producePrice)/testcount
          print ("Total produce price: ", totalprice)
          print ("Count: ", testcount)
          print ("Average produce price: ", averageprice)
          ShowMenu()
      elif choice == 3:
          ShowMenu()
      else:
          print ("Command 4")

#END


ShowMenu()

