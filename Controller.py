# Class Definition: Controller
# The Controller class acts as an intermediary between the model (data) and the view (user interface).
# It handles the application's logic and user inputs, directing the flow of data in the application.


class Controller:
    def __init__(self, model, view):
        """
        Initialize the Controller class.
        This constructor initializes the Controller with references to the model and view components,
        allowing for interactions between the data layer (model) and the user interface (view).
        """
        self.model = model
        self.view = view

    def load_data(self, file_name):
        """
        Load data from a specified file into the model.
        This method calls the model's load_data method to read data from a file (here, 'travelq.csv') 
        and populate the model's data structures.
        """
        self.model.load_data("travelq.csv")

    def show_record(self, ref_number):
        """
        Display a specific record based on its reference number.
        This method retrieves a record from the model using the provided reference number and then
        uses the view to display this record.
        """
        record = self.model.get_record_by_ref(ref_number)
        self.view.display_record(record)

    def show_records(self):
        """
        Display all records.
        This method retrieves all records from the model and then uses the view to display these records.
        """
        records = self.model.get_records()
        self.view.display_records(records)

    def add_record(self, record):
        """
        Add a new record to the model.
        This method allows adding a new record to the model's data structure.
        """
        self.model.add_record(record)

    def edit_record(self, ref_number, new_data):
        """
        Edit a record in the model.
        This method allows editing a record in the model's data structure.
        """
        self.model.edit_record(ref_number, new_data)

    def delete_record(self, ref_number):
        """
        Delete a record in the model.
        This method allows deleting a record in the model's data structure.
        """
        self.model.delete_record(ref_number)
        
    def perform_multi_column_search(self):
        """
    Executes a multi-column search based on user input and displays the results.

    This method first retrieves the search criteria from the user through the View.
    It then passes these criteria to the Model to perform the actual search in the database.
    Depending on the search results, it either displays the records or a 'no records found' message.
    """
        search_criteria = self.view.get_multi_column_search_input()
        if not search_criteria:
            print("No search criteria provided.")
            return
        results = self.model.search_multiple_columns(search_criteria)
        if results:
            self.view.display_records(results)
        else:
            self.view.display_message("No records found.")