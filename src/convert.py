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


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str,
                          text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if not node.text_type.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) & 1:
            index = node.text.rindex(f"{delimiter}")
            view = 3
            end = index + view if index + view < len(node.text) else len(node.text)
            error_message = "Mismatched delimiter, did you forget to close" \
                f" {node.text[index - view: end]}"
            raise ValueError(error_message)

        if node.text.find(delimiter) == -1:
            error_message = f"""
            Delimiter ({delimiter}), missing from node text.
            Node may be mistyped:
            {node}
            """
            raise ValueError(error_message)

        try:
            new_nodes.extend(_process_text(delimiter, node.text, text_type))
        except ValueError:
            raise

    return new_nodes


def _process_text(delim: str, text: str, text_type: TextType) -> list[TextNode]:
    delim_len = len(delim)
    results = []

    start = 0
    while (open := text.find(delim, start)) != -1:
        # Collect text before opening delimiter if the delimiter isn't the
        # first character of the string.
        if start != open:
            results.append(TextNode(text[start:open], TextType.TEXT))

        close = text.find(delim, open + delim_len)
        results.append(TextNode(text[open + delim_len:close], text_type))
        start = close + delim_len

    # If there's text left in the string, create a text node
    if start < len(text):
        results.append(TextNode(text[start:], TextType.TEXT))

    return results
