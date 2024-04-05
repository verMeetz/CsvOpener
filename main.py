from Model import Model, Record  
from View import View
from Controller import Controller

def initialize_database(model_instance):
    """
    Initialize the database by creating tables.
    """
    model_instance.create_table()

def main():
    """
    Main function to run the application.
    This function initializes the Model, View, and Controller, sets up the database,
    and enters a loop to process user commands.
    """
    print("Created by: Mitin Verma")
    database = "travel_expenses.db"
    csv_file_path = "travelq.csv"

    # Initialize Model, View, and Controller
    model = Model(database, csv_file_path) 
    view = View()
    controller = Controller(model, view)

    # Initialize the database
    initialize_database(model)
    print("MADE BY: MITIN VERMA")
    while True:
        view.show_menu() 
        choice = input("Enter your choice: ")
    
    #CREATE New Record Section
        if choice == '1':
            print("Enter details to create new record:")
            ref_number = input("Enter reference number: ")
            disclosure_group = input("Enter disclosure group: ")
            title_en = input("Enter title (English): ")
            title_fr = input("Enter title (French): ")
            name = input("Enter name: ")
            purpose_en = input("Enter purpose (English): ")
            print("Record CREATED Successfully")
            new_record = Record(ref_number, disclosure_group, title_en, title_fr, name, purpose_en)
            controller.add_record(new_record)

     #Show a record
        elif choice == '2':
            print("Enter details to read record:")
            ref_number = input("Enter reference number: ")
            controller.show_record(ref_number)


    #UPDATE Record Section
        elif choice == '3':
            ref_number = input("Enter reference number of the record to update: ")
            print("Enter new details for the record:")
            new_disclosure_group = input("Enter new disclosure group: ")
            new_title_en = input("Enter new title (English): ")
            new_title_fr = input("Enter new title (French): ")
            new_name = input("Enter new name: ")
            new_purpose_en = input("Enter new purpose (English): ")
            print("Record UPDATED Successfully")
            updated_record = Record(ref_number, new_disclosure_group, new_title_en, new_title_fr, new_name, new_purpose_en)
            controller.edit_record(ref_number, updated_record)

    #DELETE    
        elif choice == '4':
            ref_number = input("Enter reference number of the record to delete: ")
            print("Record DELETED Successfully")
            controller.delete_record(ref_number)

    #MULTI COLUMN SEARCH
        elif choice == '5': 
            controller.perform_multi_column_search()

    #EXIT the loop
        elif choice == '6':
         print("BYE BYE")  
         break

        else:
            print("Invalid choice. Please try again.")
     
       
            
# Run the main function when the script is executed
if __name__ == '__main__':
    main()
