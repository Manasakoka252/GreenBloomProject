from db_connection import create_connection
def add_plant():
    plant_id = int(input("Enter plant ID: "))
    plant_name = input("Enter plant name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    supplier_name = input("Enter supplier name: ")

    connection = create_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO plants
        (plant_id, plant_name, category, price, quantity, supplier_name)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        plant_id,
        plant_name,
        category,
        price,
        quantity,
        supplier_name
    )

    cursor.execute(query, values)

    connection.commit()

    print("Plant added successfully!")

    cursor.close()
    connection.close()


def view_plants():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM plants"

    cursor.execute(query)

    plants = cursor.fetchall()

    if len(plants) == 0:
        print("No plants found.")
    else:
        print("\n--- Plant Details ---")

        for plant in plants:
            print("Plant ID:", plant[0])
            print("Plant Name:", plant[1])
            print("Category:", plant[2])
            print("Price:", plant[3])
            print("Quantity:", plant[4])
            print("Supplier Name:", plant[5])
            print("--------------------")

    cursor.close()
    connection.close()


def update_plant():
    try:
        plant_id = int(input("Enter plant ID: "))
        new_price = float(input("Enter new price: "))
        new_quantity = int(input("Enter new quantity: "))

        connection = create_connection()
        cursor = connection.cursor()

        query = """
            UPDATE plants
            SET price = %s, quantity = %s
            WHERE plant_id = %s
        """

        values = (new_price, new_quantity, plant_id)

        cursor.execute(query, values)

        if cursor.rowcount == 0:
            print("Plant not found.")
        else:
            connection.commit()
            print("Plant updated successfully.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter valid numeric values.")
        
        
def delete_plant():
    try:
        plant_id = int(input("Enter plant ID: "))

        connection = create_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM plants
            WHERE plant_id = %s
        """

        values = (plant_id,)

        cursor.execute(query, values)

        if cursor.rowcount == 0:
            print("Plant not found.")
        else:
            connection.commit()
            print("Plant deleted successfully.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid plant ID.")       
        
        
    
def search_plant():
    plant_name = input("Enter plant name to search: ")
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM plants
        WHERE plant_name LIKE %s
    """

    values = (f"%{plant_name}%",)

    cursor.execute(query, values)

    plants = cursor.fetchall()

    if len(plants) == 0:
        print("Plant not found.")
    else:
        print("\n--- Search Results ---")

        for plant in plants:
            print("Plant ID:", plant[0])
            print("Plant Name:", plant[1])
            print("Category:", plant[2])
            print("Price:", plant[3])
            print("Quantity:", plant[4])
            print("Supplier Name:", plant[5])
            print("----------------------")

    cursor.close()
    connection.close()
