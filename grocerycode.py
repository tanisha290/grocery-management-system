def inventory():
    import mysql.connector as x
    mycon = x.connect(host="127.0.0.1", user="root", passwd="Tanisha29123", database="grocerydb")
    if not mycon.is_connected():
        print("Error connecting to MySQL database")
        return

    while True:
        print('''
            Choose one of the following operations:
            1. View all items
            2. View items by stock
            3. Add or delete items
            4. Modify item
        ''')
        ch = int(input("Enter your choice: "))
        cursor = mycon.cursor()

        if ch == 1:
            print("ITEM DETAILS")
            print("Itemid, Name, Itemcateg, Stock, Lastupd, Expdate, CP, SP")
            cursor.execute("SELECT * FROM inventory")
            for row in cursor.fetchall():
                print(row)
            if input("Do you want to continue? (yes/no): ").lower() != "yes":
                return

        elif ch == 2:
            print('''
                In which order?
                1. Ascending
                2. Descending
            ''')
            a = input("Enter option (asc/desc): ").lower()
            if a == 'asc':
                print("ITEM DETAILS IN ASC ORDER (BY STOCK)")
                cursor.execute("SELECT itemid, name, stock FROM inventory ORDER BY stock")
            elif a == 'desc':
                print("ITEM DETAILS IN DESC ORDER (BY STOCK)")
                cursor.execute("SELECT * FROM inventory ORDER BY stock DESC")
            else:
                print("Incorrect input")
                if input("Try again? (yes/no): ").lower() != "yes":
                    return
                continue
            for row in cursor.fetchall():
                print(row)
            if input("Do you want to continue? (yes/no): ").lower() != "yes":
                return

        elif ch == 3:
            print('''
                Do you want to:
                1. Add
                2. Delete
            ''')
            y = int(input("Enter choice: "))
            if y == 1:
                while True:
                    itid = input("Enter item ID: ")
                    itname = input("Enter item name: ")
                    itcateg = input("Enter item category: ")
                    itstock = input("Enter amount in stock: ")
                    itupd = input("Enter updating date: ")
                    itexp = input("Enter expiry date: ")
                    itcp = input("Enter cost price: ")
                    itsp = input("Enter selling price: ")
                    cursor.execute(f'''INSERT INTO inventory VALUES('{itid}','{itname}','{itcateg}',{itstock},
                                      '{itupd}','{itexp}',{itcp},{itsp})''')
                    mycon.commit()
                    print("Successfully added")
                    if input("Add more items? (yes/no): ").lower() != "yes":
                        return
            elif y == 2:
                while True:
                    itid = input("Enter item ID: ")
                    cursor.execute(f"DELETE FROM inventory WHERE itemid='{itid}'")
                    mycon.commit()
                    print("Deleted successfully")
                    if input("Delete another item? (yes/no): ").lower() != "yes":
                        return
            else:
                print("Invalid input")
                return

        elif ch == 4:
            itid = input("Enter item ID: ")
            while True:
                print('''
                    What do you want to modify?
                    1. Name
                    2. Category
                    3. Stock
                    4. Updation date
                    5. Expiry date
                    6. Cost Price
                    7. Selling Price
                ''')
                y = int(input("Enter choice: "))
                if y == 1:
                    new = input("Enter new name: ")
                    cursor.execute(f"UPDATE inventory SET name='{new}' WHERE itemid='{itid}'")
                elif y == 2:
                    new = input("Enter new category: ")
                    cursor.execute(f"UPDATE inventory SET itemcateg='{new}' WHERE itemid='{itid}'")
                elif y == 3:
                    new = int(input("Enter new stock amount: "))
                    cursor.execute(f"UPDATE inventory SET stock={new} WHERE itemid='{itid}'")
                elif y == 4:
                    new = input("Enter new updation date: ")
                    cursor.execute(f"UPDATE inventory SET lastupd='{new}' WHERE itemid='{itid}'")
                elif y == 5:
                    new = input("Enter new expiry date: ")
                    cursor.execute(f"UPDATE inventory SET expdate='{new}' WHERE itemid='{itid}'")
                elif y == 6:
                    new = int(input("Enter new cost price: "))
                    cursor.execute(f"UPDATE inventory SET cp={new} WHERE itemid='{itid}'")
                elif y == 7:
                    new = int(input("Enter new selling price: "))
                    cursor.execute(f"UPDATE inventory SET sp={new} WHERE itemid='{itid}'")
                else:
                    print("Invalid input")
                    if input("Try again? (yes/no): ").lower() != "yes":
                        return
                    continue
                mycon.commit()
                print("Updated successfully")
                if input("Modify another field? (yes/no): ").lower() != "yes":
                    return
        else:
            print("Invalid input")
            return


def supplier():
    import mysql.connector as x
    mycon = x.connect(host="127.0.0.1", user="root", passwd="Tanisha29123", database="grocerydb")
    if not mycon.is_connected():
        print("Error connecting to MySQL database")
        return

    while True:
        print('''
            Choose one of the following operations:
            1. View all suppliers
            2. View suppliers item-wise
            3. Add or remove supplier
            4. Modify supplier name
        ''')
        ch = int(input("Enter choice: "))
        cursor = mycon.cursor()

        if ch == 1:
            cursor.execute("SELECT * FROM supplier ORDER BY ID")
            print("SUPPLIER DETAILS")
            for row in cursor.fetchall():
                print(row)
            if input("Continue? (yes/no): ").lower() != "yes":
                return

        elif ch == 2:
            cursor.execute('''SELECT inventory.itemid, inventory.name AS itemname, ID,
                              supplier.name AS supplier_name
                              FROM inventory, supplier, itemsup
                              WHERE inventory.itemid = itemsup.itemid AND ID = supid''')
            print("ITEM AND SUPPLIER DETAILS")
            for row in cursor.fetchall():
                print(row)
            if input("Continue? (yes/no): ").lower() != "yes":
                return

        elif ch == 3:
            print('''
                Do you want to:
                1. Add
                2. Remove
            ''')
            y = int(input("Enter choice: "))
            if y == 1:
                while True:
                    sid = input("Enter supplier ID: ")
                    sname = input("Enter supplier name: ")
                    cursor.execute(f"INSERT INTO supplier VALUES('{sid}','{sname}')")
                    mycon.commit()
                    print("Successfully added")
                    if input("Add more? (yes/no): ").lower() != "yes":
                        return
            elif y == 2:
                while True:
                    sid = input("Enter supplier ID: ")
                    cursor.execute(f"DELETE FROM supplier WHERE ID='{sid}'")
                    mycon.commit()
                    print("Removed successfully")
                    if input("Remove more? (yes/no): ").lower() != "yes":
                        return

        elif ch == 4:
            while True:
                sid = input("Enter supplier ID: ")
                new = input("Enter new name: ")
                cursor.execute(f"UPDATE supplier SET name='{new}' WHERE ID='{sid}'")
                mycon.commit()
                print("Updated successfully")
                if input("Update another? (yes/no): ").lower() != "yes":
                    return

        else:
            print("Invalid input")
            return


def orders():
    import mysql.connector as x
    mycon = x.connect(host="127.0.0.1", user="root", passwd="Tanisha29123", database="grocerydb")
    if not mycon.is_connected():
        print("Error connecting to MySQL database")
        return

    while True:
        print('''
            Choose one of the following operations:
            1. View orders
            2. Add or delete order
        ''')
        ch = int(input("Enter choice: "))
        cursor = mycon.cursor()

        if ch == 1:
            cursor.execute('''SELECT orders.itemid, name, ordcnt, orddate
                              FROM inventory, orders
                              WHERE inventory.itemid = orders.itemid
                              ORDER BY orddate''')
            print("ORDER DETAILS")
            for row in cursor.fetchall():
                print(row)
            if input("Continue? (yes/no): ").lower() != "yes":
                return

        elif ch == 2:
            print('''
                Do you want to:
                1. Add
                2. Delete
            ''')
            y = int(input("Enter choice: "))
            if y == 1:
                while True:
                    itid = input("Enter item ID: ")
                    curord = int(input("Enter current order count: "))
                    orddate = input("Enter order date: ")
                    cursor.execute(f"INSERT INTO orders VALUES('{itid}', {curord}, '{orddate}')")
                    mycon.commit()
                    print("Successfully added")
                    if input("Add more? (yes/no): ").lower() != "yes":
                        return
            elif y == 2:
                while True:
                    itid = input("Enter item ID: ")
                    cursor.execute(f"DELETE FROM orders WHERE itemid='{itid}'")
                    mycon.commit()
                    print("Deleted successfully")
                    if input("Delete more? (yes/no): ").lower() != "yes":
                        return

        else:
            print("Invalid input")
            return


# ======================== MAIN ===========================

import mysql.connector as x
mycon = x.connect(host="127.0.0.1", user="root", passwd="Tanisha29123", database="grocerydb")
if not mycon.is_connected():
    print("Error connecting to MySQL database")
    exit()

while True:
    print('''
    ********************!!!!!  TPT MARKET  !!!!!**********************
    GREETINGS!!

    WELCOME TO TPT MARKET...

    What would you like to manage?
    1. Inventory
    2. Supplier
    3. Orders
    4. Exit
    ''')
    op = int(input("Enter option: "))
    if op == 1:
        inventory()
    elif op == 2:
        supplier()
    elif op == 3:
        orders()
    elif op == 4:
        print("Thank You for visiting!")
        break
    else:
        print("Wrong input")
