import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

from textnode import TextNode, TextType



class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props ={"href": "https://www.google.com"})
        node2 = HTMLNode(props ={"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(props ={"href": "https://www.google.com"})
        node2 = HTMLNode(value ={"link to google.com"}, props ={"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = HTMLNode(value ={"link to google.com"}, props ={"href": "https://www.google.com"})
        node2 = HTMLNode(value ={"Link to google.com"}, props ={"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is a paragraph of bolded text.")
        self.assertEqual(node.to_html(), "<b>This is a paragraph of bolded text.</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("h1", "Click me!")
        self.assertEqual(node.to_html(), "<h1>Click me!</h1>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_empty_grandchildren_list(self):
        child_node = ParentNode("span", [])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span></span></div>")

    def test_to_html_with_siblings(self):
        child1 = LeafNode("span", "first")
        child2 = LeafNode("span", "second")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><span>first</span><span>second</span></div>")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bolded node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bolded node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_links(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node", {"href": html_node.props})

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is an image node"})

    
if __name__ == "__main__":
    unittest.main()