import unittest
from pymongo.connection import Connection
from pymongo.son_manipulator import AutoReference, NamespaceInjector
import time

class TestAutoReferencePatch(unittest.TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.drop_database("test_autoreference_patch")
        self.db = self.connection["test_autoreference_patch"]
        self.db.add_son_manipulator(NamespaceInjector())
        self.db.add_son_manipulator(AutoReference(self.db))
        messages = [{'title': i} for i in range(1000)]
        self.db.messages.insert(messages)
        user = {'name': 'tom', 'messages': messages}
        self.db.users.save(user)
        
    def test_patch(self):
        start = time.time()
        original = self.db.users.find_one()
        print time.time() - start
        import autoreference_patch
        start = time.time()
        patched = self.db.users.find_one()
        print time.time() - start
        self.assertEqual(original, patched)
        
if __name__ == "__main__":
    unittest.main()