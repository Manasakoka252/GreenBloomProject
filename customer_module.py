from db_connection import create_connection

def add_customer():
    customer_name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    city = input("Enter city: ")

    if customer_name == "" or phone == "" or city == "":
        print("All fields are required.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers
        (customer_name, phone, city)
        VALUES (%s, %s, %s)
    """

    values = (customer_name, phone, city)

    cursor.execute(query, values)
    connection.commit()

    customer_id = cursor.lastrowid

    print("Customer added successfully!")
    print("Customer ID:", customer_id)

    cursor.close()
    connection.close()
    

def view_customers():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM customers"

    cursor.execute(query)

    customers = cursor.fetchall()

    if len(customers) == 0:
        print("No customers found.")
    else:
        print("\n--- Customer Details ---")

        for customer in customers:
            print("Customer ID:", customer[0])
            print("Customer Name:", customer[1])
            print("Phone:", customer[2])
            print("City:", customer[3])
            print("-----------------------")

    cursor.close()
    connection.close()
    
    
    
def customer_purchase_history():
    try:
        customer_id = int(input("Enter customer ID: "))

        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT *
            FROM sales
            WHERE customer_id = %s
        """

        values = (customer_id,)

        cursor.execute(query, values)
        sales = cursor.fetchall()

        if len(sales) == 0:
            print("No purchase history found.")
        else:
            print("\n--- Purchase History ---")

            for sale in sales:
                print("Sale ID:", sale[0])
                print("Customer ID:", sale[1])
                print("Plant Name:", sale[2])
                print("Quantity:", sale[3])
                print("Total Amount:", sale[4])
                print("Sale Date:", sale[5])
                print("------------------------")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid customer ID.")
    



