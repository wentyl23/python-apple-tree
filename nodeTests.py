import unittest
from node import Node, parser

testTrees = [
    [5, [3, [2], [5]], [7, [1], [0, [2], [8, [5]]]]],
    [5, [3, [2, [1, [0]]]]],
    [52, [20, [10]], [15]],
    [5]
]

averageTestCases = [
    3.8,
    2.2,
    24.25,
    5
]

medianTestCases = [
    4,
    2,
    17.5,
    5
]

sumTestCases = [
    38,
    11,
    97,
    5
]

strTestCases = [
    "5\n \t3\n \t\t2\n \t\t5\n \t7\n \t\t1\n \t\t0\n \t\t\t2\n \t\t\t8\n \t\t\t\t5\n".replace(" ",
                                                                                              ""),
    "5\n \t3\n \t\t2\n \t\t\t1\n \t\t\t\t0\n".replace(" ", ""),
    "52\n \t20\n \t\t10\n \t15\n".replace(" ", ""),
    "5\n"
]


class TestNode(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)

    def test_node(self):
        self.assertEqual(self.root.value, 1)
        self.assertEqual(len(self.root.children), 0)

    def test_node_wrong_type_error(self):
        with self.assertRaises(TypeError):
            self.root=Node("a")

    def test_add_child_as_node(self):
        self.root.add_child(Node(2))
        self.root.add_child(Node(3))
        self.assertEqual(self.root.value, 1)
        self.assertEqual(len(self.root.children), 2)
        self.assertEqual(self.root.children[0].value, 2)
        self.assertEqual(self.root.children[1].value, 3)
        self.assertEqual(len(self.root.children[0].children), 0)
        self.assertEqual(len(self.root.children[1].children), 0)

    def test_add_child_as_int(self):
        self.root.add_child(2)
        self.assertEqual(len(self.root.children), 1)
        self.assertEqual(self.root.children[0].value, 2)
        self.assertEqual(len(self.root.children[0].children), 0)

    def test_add_child_wrong_type_error(self):
        with self.assertRaises(TypeError):
            self.root.add_child("a")

    def test_add_too_many_children(self):
        self.root
        for i in range(self.root.maxChildren):
            self.root.add_child(Node(i))
        with self.assertRaises(ValueError):
            self.root.add_child(Node(0))

    def test_parser(self):
        testTree = [5, [3, [2], [5]], [7, [1], [0, [2], [8, [5]]]]]
        self.root = parser(testTree)
        self.assertEqual(self.root.value, 5)

        self.assertEqual(self.root.children[0].value, 3)
        self.assertEqual(self.root.children[0].children[0].value, 2)
        self.assertEqual(self.root.children[0].children[1].value, 5)

        self.assertEqual(self.root.children[1].value, 7)
        self.assertEqual(self.root.children[1].children[0].value, 1)
        self.assertEqual(self.root.children[1].children[1].value, 0)

        self.assertEqual(self.root.children[1].children[1].children[0].value, 2)
        self.assertEqual(self.root.children[1].children[1].children[1].value, 8)
        self.assertEqual(self.root.children[1].children[1].children[1].children[0].value, 5)

    def test_parser_singe_node(self):
        testTree = [1]
        self.assertEqual(self.root.value, 1)
        self.assertEqual(len(self.root.children), 0)

    def test_str(self):
        for i in range(len(testTrees)):
            self.root = parser(testTrees[i])
            self.assertEqual(str(self.root), strTestCases[i])

    def test_subtree_average(self):
        for i in range(len(testTrees)):
            self.root = parser(testTrees[i])
            self.assertEqual(self.root.subtree_average(), averageTestCases[i])

    def test_subtree_median(self):
        for i in range(len(testTrees)):
            self.root = parser(testTrees[i])
            self.assertEqual(self.root.subtree_median(), medianTestCases[i])

    def test_subtree_sum(self):
        for i in range(len(testTrees)):
            self.root = parser(testTrees[i])
            self.assertEqual(self.root.subtree_sum(), sumTestCases[i])

    def test_child_computation(self):
        self.root=parser([52, [20, [10]], [15]])
        child=self.root.children[0]
        self.assertEqual(child.subtree_average(), 15)
        self.assertEqual(child.subtree_median(), 15)
        self.assertEqual(child.subtree_sum(), 30)
        self.assertEqual(str(child), "20\n\t10\n")



if __name__ == "__main__":
    unittest.main()
