import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_text_property(self):
        node = TextNode([1,2,3], "test text")
        node2 = TextNode([1,2,3], "test text")
        self.assertEqual(node, node2)
    
    def test_text_not_equal(self):
        node = TextNode([1,2,3], "test text")
        node2 = TextNode([1,2,3], "test text")
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode([1,2,3], "test text", 'sample url')
        node2 = TextNode([1,2,3], "test text", 'sample url')
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
