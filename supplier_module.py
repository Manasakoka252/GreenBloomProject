from db_connection import create_connection


def add_supplier():
    supplier_id = input("Enter supplier ID: ").strip()
    supplier_name = input("Enter supplier name: ")
    phone = input("Enter phone number: ")
    city = input("Enter city: ")

    if supplier_id == "" or supplier_name == "" or phone == "" or city == "":
        print("All fields are required.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO suppliers
        (supplier_id, supplier_name, phone, city)
        VALUES (%s, %s, %s, %s)
    """

    values = (supplier_id, supplier_name, phone, city)

    cursor.execute(query, values)
    connection.commit()

    print("Supplier added successfully.")

    cursor.close()
    connection.close()


def view_suppliers():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM suppliers"

    cursor.execute(query)

    suppliers = cursor.fetchall()

    if len(suppliers) == 0:
        print("No suppliers found.")
    else:
        print("\n--- Supplier Details ---")

        for supplier in suppliers:
            print("Supplier ID:", supplier[0])
            print("Supplier Name:", supplier[1])
            print("Phone:", supplier[2])
            print("City:", supplier[3])
            print("------------------------")

    cursor.close()
    connection.close()


def update_supplier():
    supplier_id = input("Enter supplier ID: ")

    connection = create_connection()
    cursor = connection.cursor()

    new_name = input("Enter new supplier name: ")
    new_phone = input("Enter new phone number: ")
    new_city = input("Enter new city: ")

    query = """
        UPDATE suppliers
        SET supplier_name = %s, phone = %s, city = %s
        WHERE supplier_id = %s
    """

    values = (new_name, new_phone, new_city, supplier_id)

    cursor.execute(query, values)

    if cursor.rowcount == 0:
        print("Supplier not found.")
    else:
        connection.commit()
        print("Supplier updated successfully.")

    cursor.close()
    connection.close()


def delete_supplier():
    supplier_id = input("Enter supplier ID to delete: ")

    connection = create_connection()
    cursor = connection.cursor()

    query = "DELETE FROM suppliers WHERE supplier_id = %s"

    values = (supplier_id,)

    cursor.execute(query, values)

    if cursor.rowcount == 0:
        print("Supplier not found.")
    else:
        connection.commit()
        print("Supplier deleted successfully!")

    cursor.close()
    connection.close()
