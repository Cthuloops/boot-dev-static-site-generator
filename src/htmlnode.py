from __future__ import annotations


class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None,
                 children: list[HTMLNode] | None = None,
                 props: dict[str, str] | None = None):
        assert isinstance(tag, (str | None)), \
            f"Expected tag to be (str | None) got {type(tag)}"
        self.tag = tag

        assert isinstance(value, (str | None)), \
            f"Expected value to be (str | None) got {type(tag)}"
        self.value = value

        assert isinstance(children, (list | None)), \
            f"Expected value to be (list | None) got {type(tag)}"
        if children is not None:
            for child in children:
                assert isinstance(child, HTMLNode), \
                    f"Expected HTMLNode got {type(tag)}"
        self.children = children

        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        """Create and return an html representation of props.

        The returned string has a leading space:
        ' key=value'

        Returns
        -------
        str
            html representation of props dict.

        Exceptions
        ----------
        ValueError
            If props is None.
        """
        assert self.props, \
            "props is None"

        html_string = ""
        for k, v in self.props.items():
            html_string += f' {k}="{v}"'

        assert html_string != "", \
            "html string is empty"

        return html_string

    def __repr__(self) -> str:
        return f"""
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}
        """


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str,
                 props: dict[str, str] | None = None):
        # Only validate value, since it's a required field.
        # super will validate the other arguments.
        super().__init__(tag=tag, value=value, children=None, props=props)
        if not isinstance(self.value, str):
            raise ValueError("Value must be a string")

    def to_html(self) -> str:
        assert isinstance(self.value, str)

        if self.tag is None:
            return self.value

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode],
                 props: dict[str, str] | None = None):
        if not tag:
            raise ValueError("Parent Node missing tag")
        if tag == "":
            raise ValueError("Parent Node empty tag")

        if not children or len(children) < 1:
            raise ValueError("Parent Node missing children")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        assert isinstance(self.children, list)

        if self.props:
            html_string = f"<{self.tag}{self.props_to_html()}>"
        else:
            html_string = f"<{self.tag}>"

        for child in self.children:
            html_string += child.to_html()

        html_string += f"</{self.tag}>"

        return html_string
