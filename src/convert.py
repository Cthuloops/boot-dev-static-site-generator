from textnode import (
    TextType,
    TextNode
)

from htmlnode import (
    LeafNode,
)


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """Generates a leaf node from a text node.

    Returns
    -------
    LeafNode
        Leaf node created from text node type.

    Exceptions
    ----------
    ValueError
        When text_node.text_type isn't a TextType.
    """
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            assert text_node.url is not None
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            assert text_node.url is not None
            return LeafNode("img", "", {"href": text_node.url,
                                        "alt": text_node.text})
        case _:
            raise ValueError("Must be a node with a type TextType")
