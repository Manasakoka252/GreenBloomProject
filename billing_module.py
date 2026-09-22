import mysql.connector
from db_connection import create_connection


def generate_bill():

    connection = create_connection()
    cursor = connection.cursor()

    try:
        # Check customer
        customer_id = int(input("Enter customer ID: "))
        query = """
            SELECT customer_id, customer_name
            FROM customers
            WHERE customer_id = %s
        """

        values = (customer_id,)

        cursor.execute(query, values)

        customer = cursor.fetchone()

        if customer is None:
            print("Customer not found.")
            return

        print("Customer:", customer[1])

        # Get plant ID
        plant_id = int(input("Enter plant ID: "))

        # Check plant
        query = """
            SELECT plant_id, plant_name, price, quantity
            FROM plants
            WHERE plant_id = %s
        """

        values = (plant_id,)

        cursor.execute(query, values)

        plant = cursor.fetchone()

        if plant is None:
            print("Plant not found.")
            return

        print("Plant:", plant[1])
        print("Price:", plant[2])
        print("Available Stock:", plant[3])

        # Get quantity
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity > plant[3]:
            print("Insufficient stock.")
            print("Available quantity:", plant[3])
            return

        # Calculate total
        total_amount = plant[2] * quantity

        print("Quantity:", quantity)
        print("Total Amount:", total_amount)

        # Update stock
        new_quantity = plant[3] - quantity

        update_query = """
            UPDATE plants
            SET quantity = %s
            WHERE plant_id = %s
        """

        update_values = (new_quantity, plant_id)

        cursor.execute(update_query, update_values)

        # Insert sale
        sale_query = """
            INSERT INTO sales
            (customer_id, plant_name, quantity, total_amount, sale_date)
            VALUES (%s, %s, %s, %s, CURDATE())
        """

        sale_values = (
            customer_id,
            plant[1],
            quantity,
            total_amount
        )

        cursor.execute(sale_query, sale_values)

        # Save both changes
        connection.commit()

        print("\n===== Bill =====")
        print("Customer ID:", customer_id)
        print("Customer Name:", customer[1])
        print("Plant:", plant[1])
        print("Quantity:", quantity)
        print("Price:", plant[2])
        print("Total Amount:", total_amount)
        print("Remaining Stock:", new_quantity)
        print("Bill generated successfully!")

    except mysql.connector.Error as error:
        connection.rollback()

        print("Billing failed.")
        print("Database error:", error)

    except ValueError:
        connection.rollback()

        print("Please enter valid numeric values.")

    finally:
        cursor.close()
        connection.close()
