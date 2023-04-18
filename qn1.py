#   PRINTING AS PER THE OUTPUT GIVEN 
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1. Add product to the cart. ")
print("2. Search the product. ")
print("1. Delete the product from the cart. ")
print("1. Quit. ")

shoppingCart={}   # an empty dictionary
option=int(input("Enter your choice: "))    # taking the options as input from user 

if option==1:       # giving condition to add the product when the customers inputs option 1
    x=input("Enter the nuumber of items to be added in the stationary: ")   # asling for the no of items to be added
    for i in range(x):       # providing a range in accordance to the no of items user wants to add
        if len(x)>=5:       # when user inputs more than 5 items to add it prints this 
            print("Cart is full. ")
            
            y=input("Enter an item: ")   #for key 
            z=input("Enter the brand name: ")   # for value
            
            # to add the key-value pair in empty dict
            update_shoppingCart=({y:z})
            shoppingCart.update(update_shoppingCart)  #updated the empty dict in new dict adding all its previous values
            print(shoppingCart)
            
            
            
            
            

