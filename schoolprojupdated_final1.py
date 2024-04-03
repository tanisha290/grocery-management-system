## Declaring functions
def inventory():
    import mysql.connector as x
    mycon=x.connect(host='localhost',user="root",passwd="Tanisha29@",database="abc")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")
    

    while True:
        print('''
            Choose one of the following operation:
            1.View all items
            2.View items by stock
            3.Add or delete items
            4.Modify item
            ''')
        ch=int(input("Enter your choice:"))

        if ch==1:#view all items
            cursor=mycon.cursor()
            print("ITEM DETAILS")
            print("Itemid, Name, Itemcateg, Stock, Lastupd, Expdate, CP, SP")
            cursor.execute("Select * from inventory")
            data=cursor.fetchall()
            for row in data:
                print(row)
            ans=input("Do you want to continue?(yes/no):")
            if ans=="yes":
                continue
            elif ans=="no":
                break

        
        elif ch==2:#view items by stock
            print('''
                In which order?
                  1.ascending
                  2.descending''')
            a=input("Enter option(asc/desc):")
            if a=='asc':
                cursor=mycon.cursor()
                print("ITEM DETAILS IN ASC ORDER (BY STOCK)")
                print("Itemid, Name, Stock")
                cursor.execute("Select itemid, name, stock from inventory order by stock")
                data=cursor.fetchall()
                for row in data:
                    print(row)
                ans=input("Do you want to continue?(yes/no):")
                if ans=="yes":
                    continue
                elif ans=="no":
                    break
            
            elif a=="desc":
                cursor=mycon.cursor()
                print("ITEM DETAILS IN DESC ORDER (BY STOCK)")
                print("Itemid, Name, Itemcateg, Stock, Lastupd, Expdate, CP, SP")
                cursor.execute("Select * from inventory order by stock desc")
                data=cursor.fetchall()
                for row in data:
                    print(row)
                ans=input("Do you want to continue?(yes/no):")
                if ans=="yes":
                    continue
                elif ans=="no":
                    break
                
            else:
                print("incorrect input")
                ans=input("Do you want to try again?(yes/no):")
                if ans=='yes':
                    continue
                elif ans=='no':
                    print("Thank you for visiting")
                    break

                
        elif ch==3:#add or delete items
            print('''Do you want to :
                  1.add
                  2.delete''')
            y=int(input("Enter choice:"))
            print()
            if y==1:
                
                while True:
                    cursor=mycon.cursor()
                    itid=input("Enter itemid:")
                    itname=input("Enter item name:")
                    itcateg=input("Enter item category:")
                    itstock=input("Enter amount in stock")
                    itupd=input("Enter updating date")
                    itexp=input("Enter item expiry date:")
                    itcp=input("Enter item cost price:")
                    itsp=input("Enter item selling price:")
                    cursor.execute('''insert into inventory values('{}','{}','{}',{},'{}',
                                   '{}',{},{})'''.format(itid,itname,itcateg,itstock,itupd,
                                                         itexp,itcp,itsp))
                    mycon.commit()
                    print("successfully added")
                    ans=input("Do you want to add more items?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
            elif y==2:
            
                while True:
                    cursor=mycon.cursor()
                    itid=input("Enter item id:")
                    cursor.execute("delete from inventory where itemid='{}'".format(itid))
                    mycon.commit()
                    print("deleted successfully")
                    ans=input("Do you want to delete another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
            else:
                print("invalid input")

               
        elif ch==4:#modify item
            itid=input("Enter item id:")
            print('''What do you want to modify?-
                  1.name
                  2.category
                  3.amount in stock
                  4.updation date
                  5.expiry date
                  6.CP
                  7.SP''')
            
            
            while True:
                y=int(input("enter choice:"))
                if y==1:
                    cursor=mycon.cursor()
                    new=input("Enter new name:")
                    cursor.execute('''Update inventory set name='{}'
                                        where itemid='{}' '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                elif y==2:
                    cursor=mycon.cursor()
                    new=input("Enter new category:")
                    cursor.execute('''Update inventory set itemcateg='{}'
                                        where itemid='{} '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                elif y==3:
                    cursor=mycon.cursor()
                    new=int(input("Enter new stock amount:"))
                    cursor.execute('''Update inventory set stock={}
                                       where itemid='{}' '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                elif y==4:
                    cursor=mycon.cursor()
                    new=input("Enter new updation date:")
                    cursor.execute('''Update inventory set lastupd='{}'
                                        where itemid='{}' '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                elif y==5:
                    cursor=mycon.cursor()
                    new=input("Enter new expiry date:")
                    cursor.execute('''Update inventory set expdate='{}'
                                        where itemid='{}' '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                elif y==6:
                    cursor=mycon.cursor()
                    new=int(input("Enter new cost price:"))
                    cursor.execute('''Update inventory set cp={}
                                        where itemid='{}' '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                elif y==7:
                    cursor=mycon.cursor()
                    new=int(input("Enter new sellipng price:"))
                    cursor.execute('''Update inventory set sp={}
                                        where itemid='{}' '''.format(new,itid))
                    mycon.commit()
                    print("updated successfully")
                    ans=input("Do you want to modify another item?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                else:
                    print("invalid input")
                    ans=input("Do you want to try again?(yes/no):")
                    if ans=='yes':
                        continue
                    elif ans=='no':
                        print("Thank you for visiting")
                        break
        break





#################################
def supplier():
    import mysql.connector as x
    mycon=x.connect(host='localhost',user="root",passwd="Tanisha29@",database="abc")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")

    
    while True:
        print('''Choose one of the following operations:
              1.View all suppliers
              2.View suppliers item wise
              3.add or remove supplier
              4.modify supplier name''')
        ch=int(input("Enter choice:"))

        #view all suppliers       
        if ch==1:
            cursor=mycon.cursor()
            print("SUPPLIER DETAILS")
            print("Supid, Name")
            cursor.execute("Select * from supplier order by ID")
            data=cursor.fetchall()
            for row in data:
                print(row)
            ans=input("Do you want to continue?(yes/no):")
            if ans=="yes":
                continue
            elif ans=="no":
                break

        #view suppliers item wise
        elif ch==2:
            cursor=mycon.cursor()
            print("ITEM AND SUPPLIER DETAILS")
            print("Itemid, ItemName, Supid, Supplier")
            cursor.execute('''select inventory.itemid,inventory.name as 'itemname',ID,
                            supplier.name as 'supplier name' from inventory,supplier,
                            itemsup where inventory.itemid=itemsup.itemid and ID=supid;''')
            data=cursor.fetchall()
            for row in data:
                print(row)
            ans=input("Do you want to continue?(yes/no):")
            if ans=="yes":
                continue
            elif ans=="no":
                break

        #add or remove supplier
        elif ch==3:
            print('''Do you want to :
                  1.add
                  2.remove''')
            y=int(input("Enter choice:"))
            print()
            if y==1:
                while True:
                    cursor=mycon.cursor()
                    sid=input("Enter supplier id")
                    sname=input("Enter supplier name")
                    cursor.execute("Insert into supplier values('{}','{}')".format(sid,sname))
                    mycon.commit()
                    print("successfully added")
                    ans=input("Do you want to add more?(yes/no):")
                    if ans=="yes":
                        continue
                    else:
                        break
            elif y==2:
                while True:
                    cursor=mycon.cursor()
                    sid=input("Enter supplier id:")
                    cursor.execute("delete from supplier where ID='{}'".format(sid))
                    mycon.commit()
                    print("removed successfully")
                    ans=input("Do you want to remove more?(yes/no):")
                    if ans=="yes":
                        continue
                    else:
                        break

        #modify supplier
        elif ch==4:
            while True:
                cursor=mycon.cursor()
                sid=input("Enter supplier id:")
                new=input("Enter new name:")
                cursor.execute("update supplier set name='{}' where ID='{}'".format(new,sid))
                mycon.commit()
                print("updated successfully")
                ans=input("Do you want to update another supplier?(yes/no):")
                if ans=="yes":
                    continue
                else:
                    return
        
###################################
def orders():
    import mysql.connector as x
    mycon=x.connect(host='localhost',user="root",passwd="Tanisha29@",database="abc")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")


    while True:
        print('''Choose one of the following operations:
              1.View orders
              2.add or delete order
              ''')
        ch=int(input("Enter choice:"))

        #view order
        if ch==1:
            cursor=mycon.cursor()
            print("ORDER DETAILS")
            print("itemid, itemName, curorder, orddate")
            cursor.execute('''select orders.itemid,name,ordcnt,orddate from inventory,
                           orders where inventory.itemid=orders.itemid order by orddate''')
            data=cursor.fetchall()
            for row in data:
                print(row)
            ans=input("Do you want to continue?(yes/no):")
            if ans=="yes":
                continue
            elif ans=="no":
                break
            

        #add or delete order
        elif ch==2:
            cursor=mycon.cursor()
            print('''Do you want to :
                  1.add
                  2.delete''')
            y=int(input("Enter choice:"))
            print()
            if y==1:
                while True:
                    cursor=mycon.cursor()
                    itid=input("Enter item id:")
                    curord=int(input("Enter current orders of this item:"))
                    orddate=input("Enter order date:")
                    cursor.execute('''Insert into orders values('{}',{},'{}')
                                                    '''.format(itid,curord,orddate))
                    mycon.commit()
                    print("successfully added")
                    ans=input("Do you want to add more?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break

                    
            elif y==2:
                while True:
                    cursor=mycon.cursor()
                    itid=input("Enter item id:")
                    cursor.execute("delete from orders where itemid='{}'".format(itid))
                    mycon.commit()
                    print("deleted successfully")
                    ans=input("Do you want to delete another order?(yes/no):")
                    if ans=="yes":
                        continue
                    elif ans=="no":
                        break
                    
            else:
                print("invalid input")
                                
#main
import mysql.connector as x
mycon=x.connect(host='localhost',user="root",passwd="Tanisha29@",database="abc")
if mycon.is_connected()==False:
    print("Error connecting to mysql database")
    
while True:
    print('''
    ********************!!!!!  TPT MARKET  !!!!!**********************
    GREETINGS!!

    WELCOME TO TPT MARKET...

    What would you like to manage?
    1.Inventory
    2.Supplier
    3.Orders
    4.Exit
    ''')
    op=int(input("Enter option:"))
    if op==1:
        inventory()
    elif op==2:
        supplier()
    elif op==3:
        orders()
    elif op==4:
        print("Thank You for visiting!")
        break
    else:
        print("Wrong input")






    
