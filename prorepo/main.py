# create cafe menu
menu={
    "coffee":50,
    "pasta":70,
    "maggi":60,
    "salad":50,
    "burger":80,
}
# greeting
print("welcome to cafe")

# print cafe menu items
print("coffee:50 \npasta:70 \nmaggi:60 \nsalad:50 \nburger:80")

total_order=0
# order 1 item
item1=input("\nEnter your first item to be ordered:")

# check item in menu then add in total order
if item1 in menu:
    total_order += menu[item1]
    print(f"your {item1} added to your order")
else:
    print(f"your{item1}not be ordered yet!")  

# ask the another order
another_order=input("Do you want to add another order item ?(yes/no):")  
if another_order=="yes":
# oeder 2 item
 item2=input("\nEnter your second item to be ordered:")

# check item in menu then add in total order
 if item2 in menu:
    total_order += menu[item2]
    print(f"your {item2} added to your order")
 else:
    print(f"your{item2}not be ordered yet!")  
    

#print the total amount item bill
print(f"the total amount of item to be pay is:{total_order}")