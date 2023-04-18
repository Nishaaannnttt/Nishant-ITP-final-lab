#   PRINTING AS PER THE OUTPUT GIVEN 
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1. Add product to the cart. ")
print("2. Search the product. ")
print("3. Delete the product from the cart. ")
print("4. Quit. ")

shoppingCart={}   # an empty dictionary

while True:    # to run program in loop 
    option=int(input("Enter your choice: "))    # taking the options as input from user 

    if option==1:       # giving condition to add the product when the customers inputs option 1
        x=int(input("Enter the nuumber of items to be added in the stationary: "))  # asling for the no of items to be added
        
        for i in range (x):     # providing a condition to iterate the program in accordance to the no of items user wants to add
            if len(shoppingCart)==5:       # when user inputs more than 5 items to add it prints this 
                print("Cart is full. ")
                
            y=input("Enter an item: ")   #for key 
            z=input("Enter the brand name: ")   # for value
                
                # to add the key-value pair in empty dict
            update_shoppingCart=({y:z})
            shoppingCart.update(update_shoppingCart)  #updated the empty dict in new dict adding all its previous values
            
            print("You added the following items to the cart: ")    
            for key, value in shoppingCart.items():
                print("{}:{}".format(key,value))         # prints the dictionary items as we want wihtout brackets and quotations
                
            # print("You added the following items to the cart: ")
            # print(update_shoppingCart)
      

    elif option==2:   #condition to search
        a=input("Enter the item to be searched: ")
        if a==y:     # when the item we typed matches the key in dictionary
            print(y,":",z)     # it prints this
        else:
            print("No product exits with this name.")   # if its not in key then it prints this 
       
              
    elif option==3:         # to delete the product
        product=input('Enter the product to be deleted: ')      
        if product in shoppingCart:     # to check if product is in key of dict
            del shoppingCart[product]    # to delte the product
        if y==0:
            print("Cart is empty. No items is found ")
       
                
    elif option==4:
        break                  # this breaks the loop
    
    else:
        print("Wrong option entered.")
                
    
                        
            
            
            
            
            
   
        
    
            
            
            
            

