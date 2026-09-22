from db_connection import create_connection


def total_sales():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT SUM(total_amount) FROM sales"

    cursor.execute(query)

    result = cursor.fetchone()

    if result[0] is None:
        print("No sales found.")
    else:
        print("Total Sales:", result[0])

    cursor.close()
    connection.close()


def available_stock():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT plant_id, plant_name, category, price, quantity
        FROM plants
    """

    cursor.execute(query)

    plants = cursor.fetchall()

    if len(plants) == 0:
        print("No plants found.")
    else:
        print("\n===== Available Stock =====")

        for plant in plants:
            print("Plant ID:", plant[0])
            print("Plant Name:", plant[1])
            print("Category:", plant[2])
            print("Price:", plant[3])
            print("Available Quantity:", plant[4])
            print("-------------------------")

    cursor.close()
    connection.close()


def low_stock_plants():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT plant_id, plant_name, category, quantity
        FROM plants
        WHERE quantity < 5
    """

    cursor.execute(query)

    plants = cursor.fetchall()

    if len(plants) == 0:
        print("No low stock plants found.")
    else:
        print("\n===== Low Stock Plants =====")

        for plant in plants:
            print("Plant ID:", plant[0])
            print("Plant Name:", plant[1])
            print("Category:", plant[2])
            print("Available Quantity:", plant[3])
            print("--------------------------")

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
            print("\n===== Customer Purchase History =====")

            for sale in sales:
                print("Sale ID:", sale[0])
                print("Customer ID:", sale[1])
                print("Plant Name:", sale[2])
                print("Quantity:", sale[3])
                print("Total Amount:", sale[4])
                print("Sale Date:", sale[5])
                print("-------------------------------")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid customer ID.")