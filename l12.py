bitPrice = input ( "What is Bitcoin price today? " )
dollaAtCard = input ( "How much $ do you have? " )
canBuy = float(dollaAtCard) / float(bitPrice)
print("You can buy " + str(canBuy) + " BTC" )

