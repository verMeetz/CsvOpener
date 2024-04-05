import unittest
from Model import Model, Record 
from View import View
from Controller import Controller


class TestModel(unittest.TestCase):
    """
    Test cases.
    This class contains unit tests to ensure that the methods of the Model class
    are functioning correctly, particularly focusing on CRUD (Create, Read, Update, Delete)
    operations for the records.
    """

    @classmethod
    def setUpClass(cls):
        """
        This method initializes a Model instance using a test database.
        """
        cls.model = Model('travel_expenses.db')

    def test_create_record(self):
        """
        This method tests that a record can be successfully added to the database
        and then retrieved to verify its existence.
        """
        record = Record('test_create_123', 'Group Create', 'Title EN Create', 'Title FR Create', 'Name Create', 'Purpose EN Create')
        self.model.add_record(record)
        result = self.model.get_record_by_ref('test_create_123')
        self.assertIsNotNone(result)
        self.model.delete_record('test_create_123')  # Cleanup

    def test_read_record(self):
        """
        This method tests that a record can be retrieved from the database
        and its contents are as expected.
        """
        record = Record('test_read_123', 'Group Read', 'Title EN Read', 'Title FR Read', 'Name Read', 'Purpose EN Read')
        self.model.add_record(record)
        result = self.model.get_record_by_ref('test_read_123')
        self.assertIsNotNone(result)
        self.assertEqual(result.ref_number, 'test_read_123')
        self.model.delete_record('test_read_123')  # Cleanup

    def test_update_record(self):
        """
        This method tests that a record's details can be updated in the database
        and then verified to ensure the update was successful.
        """
        record = Record('test_update_123', 'Group Update', 'Title EN Update', 'Title FR Update', 'Name Update', 'Purpose EN Update')
        self.model.add_record(record)
        updated_record = Record('test_update_123', 'Updated Group', 'Updated Title EN', 'Updated Title FR', 'Updated Name', 'Updated Purpose EN')
        self.model.edit_record('test_update_123', updated_record)
        result = self.model.get_record_by_ref('test_update_123')
        self.assertEqual(result.title_en, 'Updated Title EN')
        self.model.delete_record('test_update_123')  # Cleanup

    def test_delete_record(self):
        """
        This method tests that a record can be deleted from the database
        and then verifies that it no longer exists.
        """
        record = Record('test_delete_123', 'Group Delete', 'Title EN Delete', 'Title FR Delete', 'Name Delete', 'Purpose EN Delete')
        self.model.add_record(record)
        self.model.delete_record('test_delete_123')
        result = self.model.get_record_by_ref('test_delete_123')
        self.assertIsNone(result)

    @classmethod
    def tearDownClass(cls):
        """
        This method closes the database connection.
        """
        cls.model.close_connection()

if __name__ == '__main__':
    unittest.main()
