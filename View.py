class View:
    """
    The View class in the MVC architecture.

    This class is responsible for all the user interface-related aspects of the application.
    It displays menus, records, and messages to the user.
    """
    @staticmethod
    def show_menu():
        """
        Display the main menu options to the user.
        This static method prints out the different operations that the user can perform,
        such as creating, reading, updating, and deleting records.
        """
        print("Choose any one operation")
        print("1 - Create a Record")
        print("2 - Read a Record")
        print("3 - Update a Record")
        print("4 - Delete a Record")
        print("5 - Multiple Column Search")
        print("6 - Exit")
        pass

    @staticmethod
    def display_record(record):
        """
        Display the details of a single record.
        """
        if record:
            print("Record Details:")
            print(f"Reference Number: {record.ref_number}")
            print(f"Title (English): {record.title_en}")
            print(f"Title (French): {record.title_fr}")
            print(f"Name: {record.name}")
            print(f"Purpose (English): {record.purpose_en}")
        else:
            print("Record not found.")

    @staticmethod
    def display_records(records):
        if records:
            print("List of Records:")
            for record in records:
                # Map each tuple index to the corresponding column
                print(f"Reference Number: {record[0]}")    # Index 0 for ref_number
                print(f"Disclosure Group: {record[1]}")    # Index 1 for disclosure_group
                print(f"Title (English): {record[2]}")     # Index 2 for title_en
                print(f"Title (French): {record[3]}")      # Index 3 for title_fr
                print(f"Name: {record[4]}")                # Index 4 for name
                print(f"Purpose (English): {record[5]}")   # Index 5 for purpose_en
                print("-" * 30)
        else:
            print("No records found.")

    @staticmethod
    def get_multi_column_search_input():
        print("Enter search criteria for multiple columns.")
        search_criteria = {}
        while True:
            column = input("Enter column name (or type 'done' to finish): ")
            if column.lower() == 'done':
                break
            term = input(f"Enter search term for {column}: ")
            search_criteria[column] = term
        return search_criteria

    @staticmethod
    def display_message(message):
        """
        Display a generic message to the user.
        """
        print(message)
