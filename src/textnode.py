from enum import (
    StrEnum,
    auto
)


class TextType(StrEnum):
    TEXT = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    LINK = auto()
    IMAGE = auto()


class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        assert isinstance(text, str), \
            f"text needs to be string, got {type(text)}"

        self.text_type = text_type
        assert isinstance(text_type, TextType), \
            f"text_type needs to be TextType, got {type(text_type)}"

        self.url = url
        assert isinstance(url, (str | None)), \
            f"url needs to be string or none, got {type(url)}"

    def __eq__(self, other):
        assert isinstance(other, TextNode), \
            "Can't compare TextNode to non-TextNode"

        if not isinstance(other, TextNode):
            return False

        text_true = self.text == other.text
        text_type_true = self.text_type == other.text_type
        url_true = self.url == other.url

        return text_true and text_type_true and url_true

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
