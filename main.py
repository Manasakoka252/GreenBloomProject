import plant_module
import supplier_module
import customer_module
import customer_module
import billing_module
import reports_module

def plant_menu():
    while True:
        print("\n===== Plant Module =====")
        print("1. Add Plant")
        print("2. View Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Search Plant")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            plant_module.add_plant()

        elif choice == "2":
            plant_module.view_plants()

        elif choice == "3":
            plant_module.update_plant()

        elif choice == "4":
            plant_module.delete_plant()

        elif choice == "5":
            plant_module.search_plant()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

def supplier_menu():
    while True:
        print("\n===== Supplier Module =====")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            supplier_module.add_supplier()

        elif choice == "2":
            supplier_module.view_suppliers()

        elif choice == "3":
            supplier_module.update_supplier()

        elif choice == "4":
            supplier_module.delete_supplier()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
            

def customer_menu():
    while True:
        print("\n===== Customer Module =====")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Customer Purchase History")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_module.add_customer()

        elif choice == "2":
            customer_module.view_customers()

        elif choice == "3":
            customer_module.customer_purchase_history()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
            
    
def billing_menu():
    while True:
        print("\n===== Billing Module =====")
        print("1. Generate Bill")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            billing_module.generate_bill()

        elif choice == "2":
            break

        else:
            print("Invalid choice. Please try again.")
            
def reports_menu():
    while True:
        print("\n===== Reports Module =====")
        print("1. Total Sales")
        print("2. Available Stock")
        print("3. Low Stock Plants")
        print("4. Customer Purchase History")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            reports_module.total_sales()
        elif choice == "2":
            reports_module.available_stock()
        elif choice == "3":
            reports_module.low_stock_plants()
        elif choice == "4":
            reports_module.customer_purchase_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            
                                  
def main_menu():
    while True:
        print("\n===== Green Bloom Plants =====")
        print("1. Plant Module")
        print("2. Supplier Module")
        print("3. Customer Module")
        print("4. Billing Module")
        print("5. Reports Module")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            plant_menu()

        elif choice == "2":
            supplier_menu()

        elif choice == "3":
            customer_menu()

        elif choice == "4":
            billing_menu()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            print("Thank you for using Green Bloom Plants!")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()