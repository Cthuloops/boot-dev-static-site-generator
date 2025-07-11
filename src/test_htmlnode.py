import unittest

from htmlnode import HTMLNode


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
