import unittest

from textnode import (
    TextNode,
    TextType
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD,
                         "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_init(self):
        with self.assertRaises(AssertionError):
            _ = TextNode(2, TextType.BOLD)

    def test_texttype_init(self):
        with self.assertRaises(AssertionError):
            _ = TextNode("text", "not a TextType")

    def test_url_init(self):
        with self.assertRaises(AssertionError):
            _ = TextNode("text", TextType.TEXT, 3)


if __name__ == "__main__":
    unittest.main()
