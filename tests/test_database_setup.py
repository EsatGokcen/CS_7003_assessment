import os
import unittest

class TestDatabaseSetup(unittest.TestCase):
    def test_database_initialized(self):
        self.assertTrue(os.path.exists("src/database/brew_and_bite.db"))
