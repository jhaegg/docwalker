from unittest import TestCase
from docwalk.docwalk import DocWalker

class TestWalk(TestCase):
    def testWalk(self):
        walker = DocWalker('data/simple.py')
        expected = ['Sample', 'Sample.say', 'Sample.say_more']
        results = walker.run()

        self.assertEqual(set(expected), set(results))
