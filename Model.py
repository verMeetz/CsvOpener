import sqlite3
import csv

class Record:
    """
    Represents a single record of travel expense data.

    Attributes:
        ref_number: Reference number of the record.
        disclosure_group: Disclosure group of the record.
        title_en: English title.
        title_fr: French title.
        name: Name of the individual.
        purpose_en: Purpose of the expense in English.
    """
    def __init__(self, ref_number, disclosure_group, title_en, title_fr, name, purpose_en):
        self.ref_number = ref_number
        self.disclosure_group = disclosure_group
        self.title_en = title_en
        self.title_fr = title_fr
        self.name = name
        self.purpose_en = purpose_en

class Model:
    """
    Manages the database operations for the application.
    This class handles all interactions with the SQLite database, including creating tables,
    loading data from CSV files, and performing CRUD operations on records.
    """
    def __init__(self, db_file, csv_file_path=None):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.create_table()
        if csv_file_path:
            self.load_data(csv_file_path) 

    def search_multiple_columns(self, search_criteria):
        """
        Search records based on multiple columns.
        :param search_criteria: Dictionary with column names as keys and search terms as values.
        :return: List of the records that match the search criteria.
        """
        query = "SELECT * FROM travel_expenses WHERE "
        conditions = []
        for column, term in search_criteria.items():
            conditions.append(f"{column} LIKE '%{term}%'")
        query += " AND ".join(conditions)
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)
        return conn

    def create_table(self):
        """Create a table from the create_table_sql statement."""
        with sqlite3.connect(self.db_file) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS travel_expenses (
                        ref_number TEXT PRIMARY KEY,
                        disclosure_group TEXT,
                        title_en TEXT,
                        title_fr TEXT,
                        name TEXT,
                        purpose_en TEXT
                    );
                """)
                conn.commit()
            except sqlite3.Error as e:
                print(e)

    def load_data(self, csv_file_path):
        """Load data from a CSV file into the database.
         This method reads travel expense records from a CSV file and inserts them into the database.
        """
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if len(row) == 6:
                        record = Record(*row[:6])
                        existing_record = self.get_record_by_ref(record.ref_number)
                        if existing_record is None:
                            print(f"Adding record: {record.__dict__}")
                            self.add_record(record)
        except FileNotFoundError:
            print(f"File not found: {csv_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def get_records(self):
        """Retrieve all records from the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM travel_expenses")
            rows = cursor.fetchall()
            return [Record(*row) for row in rows]
        except sqlite3.Error as e:
            print(e)

    # Add Record Method
    def add_record(self, record):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO travel_expenses (ref_number, disclosure_group, title_en, title_fr, name, purpose_en)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (record.ref_number, record.disclosure_group, record.title_en, record.title_fr, record.name, record.purpose_en))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    # Edit Record Method
    def edit_record(self, ref_number, new_data):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE travel_expenses
                SET disclosure_group=?, title_en=?, title_fr=?, name=?, purpose_en=?
                WHERE ref_number=?
                """, (new_data.disclosure_group, new_data.title_en, new_data.title_fr, new_data.name, new_data.purpose_en, ref_number))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    # Delete Record Method
    def delete_record(self, ref_number):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM travel_expenses WHERE ref_number=?", (ref_number,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    # Fetch Record by Reference Number Method
    def get_record_by_ref(self, ref_number):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM travel_expenses WHERE ref_number = ?", (ref_number,))
            row = cursor.fetchone()
            if row:
                return Record(*row)
            else:
                return None
        except sqlite3.Error as e:
            print(e)
