"Customer Management System by Alankrit Upadhyay"
import pymysql
#from pandas.io.sql import execute

# con=pymysql.connect(host="127.0.0.1",user="root",password="alankrit",database="cusdb")
# cur=con.cursor()

def loginSystem():
    try:
        con = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="alankrit",
            database="cusdb"
        )
        cur = con.cursor()

        userid = input("Enter Login ID: ")
        pwd = input("Enter Password: ")

        qry = f"SELECT * FROM userlog WHERE loginid='{userid}' AND loginpas='{pwd}'"
        cur.execute(qry)
        data = cur.fetchone()

        if data:
            print(f"\n✅ Login Successful! Welcome, {userid}.")
            return True
        else:
            print("❌ Invalid Login ID or Password.")
            return False

    except Exception as e:
        print("Error:", e)
        return False
    finally:
        con.close()


def addCustomer(id, name, age, mob):  # mob is INT in MySQL
    try:
        # Connect to MySQL
        con = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="alankrit",
            database="cusdb"
        )
        cur = con.cursor()

        # Prepare and execute query (mob as INT — no quotes)
        qry = f"INSERT INTO custb VALUES ({id}, '{name}', {age}, {mob})"
        cur.execute(qry)

        # Commit changes
        con.commit()

        print("Customer Added Successfully in Alankrit CMS")

    except Exception as e:
        print("Error:", e)

    finally:
        # Always close connection safely
        con.close()

#
def viewCustomer():  # for displaying data of all customers
    try:
        # Connect to database
        con=pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="alankrit",
            database="cusdb"
        )
        cur=con.cursor()

        # Query to get all customers
        qry = "SELECT * FROM custb"
        cur.execute(qry)

        # Fetch all records
        data = cur.fetchall()

        if data:
            print("=== All Customer Records in Alankrit CMS ===")
            for row in data:
                print(f"CustID: {row[0]} | Cust Name: {row[1]} | Cust Age: {row[2]} | Cust Mob: {row[3]}")
        else:
            print("No customer records found in the database.")

    except Exception as e:
        print("Error:", e)

    finally:
        # Always close connection safely
        con.close()


def updateCustomer(key, name, age, mob):#for update customer detail based on id
    try:
        # Connect to database
        con = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="alankrit",
            database="cusdb"
        )
        cur = con.cursor()

        # Query to search by ID
        qry = f"update custb set name='{name}',age={age},mob={mob} where id={key}"
        cur.execute(qry)

        con.commit()
    except Exception as e:
        print("Error:", e)

    finally:
        con.close()

    print("Customer Updated successfully")
def searchCustomer(id):  # for searching customer detail based on id
    try:
        # Connect to database
        con = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="alankrit",
            database="cusdb"
        )
        cur = con.cursor()

        # Query to search by ID
        qry = f"SELECT * FROM custb WHERE id = {id}"
        cur.execute(qry)

        # Fetch one record
        data = cur.fetchone()

        if data:
            print("✅ Customer Found:")
            print("CustID:", data[0], " | Cust Name:", data[1],
                  " | Cust Age:", data[2], " | Cust Mob:", data[3])
        else:
            print("⚠️ No customer found with ID:", id)

    except Exception as e:
        print("❌ Error:", e)

    finally:
        con.close()

def deleteCustomer(id):#for delete customer detail based on id parmanatly
    try:
        # Connect to database
        con = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="alankrit",
            database="cusdb"
        )
        cur = con.cursor()

        # Query to search by ID
        qry = f"delete from custb where id={id}"
        cur.execute(qry)

        con.commit()
    except Exception as e:
        print("Error:", e)

    finally:
        con.close()

    print("customer deleted successfully")


#Prasentation Layer
"welcome to Alankrit CMS"
print("Customer Management System by Alankrit Upadhyay")

if loginSystem():   # ✅ Ask for login first
    print("\nWelcome to Alankrit CMS")

while True:
    try:
        print("----Menu of Alankrit CSM----")
        print("1:Enter Customer detail")
        print("2: View customer")
        print("3: Update Customer")
        print("4: Search Customer")
        print("5: Delete Customer")
        print("6: exit from Alankrit CMS")
        choice=input("Enter The choice")
        if(choice=="1"):
            id = input("Enter Customer id:")
            name = input("Enter Customer Name:")
            age = input("Enter Customer Age:")
            mob = input("Enter Customer Phone:")
            addCustomer(id,name,age,mob)
        elif(choice=="2"):
             viewCustomer()
        elif(choice=="3"):
            key=input("Enter Id of Customer to Update Customer detail")
            name = input("Enter updated Customer Name:")
            age = input("Enter updated Customer Age:")
            mob = input("Enter updated Customer Phone:")
            updateCustomer(key, name, age, mob)
        elif(choice=="4"):
            id = input("Enter Customer id:")
            searchCustomer(id)
        elif(choice=="5"):
            id = input("Enter id of Customer which should delete:")
            deleteCustomer(id)
        elif (choice == "6"):  # Exit
            print("Thanks for using Alankrit's CMS\nBest CMS in World")
            #logo = pyfiglet.figlet_format("Alankrit")
            #print(logo)
            break
        else:
            print("Incorrect Choice")
    except Exception as err:
        print("Error!", err)

