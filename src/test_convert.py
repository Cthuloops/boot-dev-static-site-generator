import unittest

from textnode import (
    TextNode,
    TextType
)

from convert import (
    text_node_to_html_node,
    split_nodes_delimiter,
    _process_text
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


class TestSplitNodesDelimiter(unittest.TestCase):
    ...


class TestProcessText(unittest.TestCase):
    def test_bold_delim(self):
        nodes = _process_text("**", "This is **bold** text", TextType.BOLD)
        self.assertEqual(3, len(nodes))
        text_node_1 = TextNode(text="This is ", text_type=TextType.TEXT)
        bold_node = TextNode(text="bold", text_type=TextType.BOLD)
        text_node_2 = TextNode(text=" text", text_type=TextType.TEXT)
        self.assertEqual(nodes[0], text_node_1)
        self.assertEqual(nodes[1], bold_node)
        self.assertEqual(nodes[2], text_node_2)

    def test_italic_delim(self):
        nodes = _process_text("_", "This is _italic_ text", TextType.ITALIC)
        self.assertEqual(3, len(nodes))
        text_node_1 = TextNode(text="This is ", text_type=TextType.TEXT)
        bold_node = TextNode(text="italic", text_type=TextType.ITALIC)
        text_node_2 = TextNode(text=" text", text_type=TextType.TEXT)
        self.assertEqual(nodes[0], text_node_1)
        self.assertEqual(nodes[1], bold_node)
        self.assertEqual(nodes[2], text_node_2)

    def test_code_delim(self):
        nodes = _process_text("`", "This is `italic` text", TextType.CODE)
        self.assertEqual(3, len(nodes))
        text_node_1 = TextNode(text="This is ", text_type=TextType.TEXT)
        bold_node = TextNode(text="italic", text_type=TextType.CODE)
        text_node_2 = TextNode(text=" text", text_type=TextType.TEXT)
        self.assertEqual(nodes[0], text_node_1)
        self.assertEqual(nodes[1], bold_node)
        self.assertEqual(nodes[2], text_node_2)

    def test_multiple_nonoverlapping_bold_delim(self):
        nodes = _process_text("**", "**This is** bold **text**", TextType.BOLD)
        self.assertEqual(3, len(nodes))
        bold_node_1 = TextNode(text="This is", text_type=TextType.BOLD)
        text_node = TextNode(text=" bold ", text_type=TextType.TEXT)
        bold_node_2 = TextNode(text="text", text_type=TextType.BOLD)
        self.assertEqual(nodes[0], bold_node_1)
        self.assertEqual(nodes[1], text_node)
        self.assertEqual(nodes[2], bold_node_2)
