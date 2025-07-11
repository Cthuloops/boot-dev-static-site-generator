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
        if not self.props:
            raise ValueError("Props has no value")

        html_string = ""
        for k, v in self.props:
            html_string += f" {k}={v}"

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
