"""PROJECT---> BILLING SYSTEM"""
#Billing system software is an accounting application
#that can be utilized to automate and streamline invoice
#processing and payment services.

#Consider a Example for Hotel make a billing system for hotel.

# Itemname   Quantity    Rate     Amount
# Tea          2          10       20
# Poha         2          20       40
#--------------------------------------
#                                  60


# We have to store Data and price==> For that we are using Dict
#Step1:
items={
  1:"Tea",2:"Poha",3:"Coffee",4:"Samosa",
  5:"Vadapav",6:"Dosa",7:"Upma",8:"Cold Coffee"
}

rate={ 
    1:10, 2:20, 3:15, 4:20,
    5:25, 6:30, 7:15, 8:25
}

it_list=[]
qt_list=[]

while True:
  print('''
      Menu
1.TEA      5.VADAPAV 
2.POHA     6.DOSA
3.COFFEE   7.UPMA
4.SAMOSA   8.COLD COFFEE
''')
  
  i=int(input("Enter your choice=>"))
  q=int(input("Input Quantity:=>"))
  it_list.append(i)
  qt_list.append(q)

  ch=input("Do you want to continue:=>")
  if ch=='n':
    print("-"*85)
    print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format("Item Name","Quantity","Rate","Amount"))
    print("-"*85)
    sum=0
    for i in range(len(it_list)):
      print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format(items[it_list[i]]
                        ,qt_list[i], rate[it_list[i]]
                        ,qt_list[i]* rate[it_list[i]] ))
      print("-"*85)
      sum=sum+qt_list[i]* rate[it_list[i]]
      print(f"Your Total Bill is {sum}\n Thank You!\nVisit Again")

      
    break

'''
Menu
1.TEA      5.VADAPAV
2.POHA     6.DOSA
3.COFFEE   7.UPMA
4.SAMOSA   8.COLD COFFEE

Enter your choice=>5
Input Quantity:=>2
Do you want to continue:=>n
------------------------------------------------------------------------------------- 
|      ItemName      |      Quantity      |        Rate        |       Amount       | 
------------------------------------------------------------------------------------- 
|        Tea         |         1          |         10         |         10         | 
------------------------------------------------------------------------------------- 
|      Vadapav       |         2          |         25         |         50         | 
------------------------------------------------------------------------------------- 
'''


