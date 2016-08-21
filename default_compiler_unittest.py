import unittest

from DefaultCompiler import DefaultCompiler

class TestDefaultCompiler   (unittest.TestCase):

    def setUp(self):
        self.compiler = DefaultCompiler(None)

    def test_levelOneHeading(self):
        output = self.compiler.compile("#this is a test")
        self.assertEqual("<h1>this is a test</h1>", output)

    def test_levelTwoHeading(self):
        output = self.compiler.compile("##this is a test")

        self.assertEqual("<h2>this is a test</h2>", output)

    def test_numberedList(self):
        output = self.compiler.compile("..this is a test")

        self.assertEqual("<ol><li>this is a test</li>", output)

    def test_unOrderedList(self):
        output = self.compiler.compile("-this is a test")

        self.assertEqual("<ul><li>this is a test</li>", output)

if __name__ == '__main__':
    unittest.main()
