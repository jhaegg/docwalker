from unittest import TestCase
from docwalk.docwalk import DocWalker

class TestWalk(TestCase):
    def testWalk(self):
        recursive_walker = DocWalker('data/simple.py', strategy='depth_first_recursive')
        breadth_first_walker = DocWalker('data/simple.py', strategy='breadth_first')
        depth_first_walker = DocWalker('data/simple.py', strategy='depth_first')
        expected = [('Sample', "Class docstring"),
                    ('Sample.say', "Method docstring"),
                    ('Sample.say_more', "Method docstring 2")]

        self.assertEqual(set(expected), set(recursive_walker.run()))
        self.assertEqual(set(expected), set(breadth_first_walker.run()))
        self.assertEqual(set(expected), set(depth_first_walker.run()))
