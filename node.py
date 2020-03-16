
"""
Class representation of node which i will be using for creating a tree. 
"""
class Node:

    def __init__(self, value):
        """
        :param value: value of particular node

        function sets value of a node to value passed, creates an array of children, and sets maxChildren to 2
        """
        if not isinstance(value, int):
            raise TypeError("value of the node has to be an integer")
        self.value = value
        self.children = []
        self.maxChildren = 2

    def add_child(self, child):
        """
        :param child: Node object meant to be set as a child of this node or int

        function for adding children to node object
        """
        if isinstance(child, Node):
            if len(self.children) < self.maxChildren:
                self.children.append(child)
            else:
                raise ValueError("This node already has " + str(self.maxChildren) + " children")

        elif isinstance(child, int):
            if len(self.children) < self.maxChildren:
                self.children.append(Node(child))
            else:
                raise ValueError("This node already has " + str(self.maxChildren) + " children")

        else:
            raise TypeError("type of the child has to be an integer or node")

    def subtree_sum(self):
        """
        function for summing values of elements in subtree

        :return: sum of values from subtree
        """
        subtreeSum = self.value
        for child in self.children:
            subtreeSum += child.subtree_sum()
        return subtreeSum

    def count_descendants(self):
        """
        helper function for counting descendants of node

        :return: amount of descendants
        """
        count = 1
        for child in self.children:
            count += child.count_descendants()
        return count

    def subtree_average(self):
        """
        function for calculating average value for elements in subtree

        :return: average value for elements in subtree
        """
        return self.subtree_sum() / self.count_descendants()

    def get_descendants(self):
        """
        helper function for getting array of node descendants

        :return: array of node descendants
        """
        descendants = [self.value]
        for child in self.children:
            descendants.extend(child.get_descendants())
        return descendants

    def subtree_median(self):
        """
        function for calculating median value for elements in subtree

        :return: median value for elements in subtree
        """
        values = self.get_descendants()
        values.sort()
        length = len(values)
        if length % 2 != 0:
            return values[int(length/2)]

        return (values[int((length-1)/2)] + values[int(length/2)])/2

    def __str__(self, level=0):
        """
        :param level: helper param for recursive usage

        function to represent the tree as a string

        :return: string representation of tree
        """
        tree = "\t"*level + str(self.value) + "\n"
        for child in self.children:
            tree += child.__str__(level+1)
        return tree


def parser(array):
    """
    :param array: array representing a tree, each node is represented by a list in which the first element is
    it's value and the next are children

    function parses array into tree using Node class

    :return: root of the Tree created from array
    """
    root = Node(array[0])
    length = len(array)
    if length > 1:
        i = 1
        while i < length:
            root.add_child(parser(array[i]))
            i += 1
    return root
