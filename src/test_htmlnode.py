import unittest

from htmlnode import (
    HTMLNode,
    LeafNode
)


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("tag")
        self.assertEqual(node.tag, "tag")

    def test_value(self):
        node = HTMLNode(value="value")
        self.assertEqual(node.value, "value")

    def test_children(self):
        node = HTMLNode(children=[HTMLNode(value=str(n)) for n in range(3)])
        assert node.children is not None
        self.assertEqual(len(node.children), 3)
        self.assertEqual(node.children[0].value, "0")
        self.assertEqual(node.children[1].value, "1")
        self.assertEqual(node.children[2].value, "2")

    def test_repr(self):
        node = HTMLNode(tag="tag", value="value", children=None,
                        props={"href": "link"})
        self.assertEqual(node.__repr__(), f"""
        Tag: tag
        Value: value
        Children: None
        Props: {({'href': 'link'})}
        """)


class TestLeafNode(unittest.TestCase):
    def test_is_LeafNode(self):
        node = LeafNode(tag=None, value="")
        assert isinstance(node, LeafNode)

    def test_value(self):
        with self.assertRaises(ValueError):
            _ = LeafNode(tag=None, value=None)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
