import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextType


class TestHTMLNode(unittest.TestCase):
    def test_props_none(self):
        node = HTMLNode("a", "text value", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_dict(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "text value", None, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_not_none(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "text value", None, props)
        self.assertNotEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "invalid HTML: no children")

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "invalid HTML: no tag")

    def test_to_html_multiple_children(self):
        child_node_1 = LeafNode("span", "child1")
        child_node_2 = LeafNode("span", "child2")
        child_node_3 = LeafNode("span", "child3")
        parent_node = ParentNode("div", [child_node_1, child_node_2, child_node_3])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span><span>child3</span></div>")


if __name__ == "__main__":
    unittest.main()
