import unittest

from textnode import (
    TextNode,
    TextType
)

from convert import (
    text_node_to_html_node
)


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("some bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "some bold text")

    def test_italic(self):
        node = TextNode("some italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "some italic text")

    def test_code(self):
        node = TextNode("some code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "some code")

    def test_link(self):
        node = TextNode("a linkie", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "a linkie")
        self.assertIsInstance(html_node.props, dict)
        self.assertEqual(html_node.props["href"], "https://www.example.com")

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIsInstance(html_node.props, dict)
        self.assertEqual(html_node.props["href"], "https://www.example.com")
        self.assertEqual(html_node.props["alt"], "alt text")
