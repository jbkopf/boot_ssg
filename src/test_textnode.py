import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a link node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a link node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()