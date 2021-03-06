import unittest
import shlex, subprocess

from node import Node
from avl import AVL

class TestAVLMethods(unittest.TestCase):

    def check_multiline(self, input, answers):
        string_rep = input.strip().split("\n")
        self.assertEqual(len(string_rep), len(answers))
        for line, answer in zip(string_rep, answers):
            self.assertEqual(line.strip().split(), answer) # Array format

    def test_insert_single_node(self):
        print("Running test_insert_single_node")
        h = AVL()
        h.insert(5)
        self.assertEqual(h.get_root().get_key(), 5)
        self.assertEqual(str(h.get_root()), '5')
        self.check_multiline(str(h), [["5"], ["_", "_"], ["5"]])

    def test_insert_1(self):
        print("Running test_insert_1")
        h = AVL([5, 2, 8, 1, 3, 9])
        self.check_multiline(str(h), [["5"], ["2", "8"], ["1", "3", "_", "9"], ["_", "_" , "_", "_", "_", "_"], ["1", "2", "3", "5", "8", "9"]])

    def test_insert_3_nodes_1(self):
        print("Running test_insert_3_nodes_ordered")
        h = AVL([10, 6, 5])
        root = h.get_root()
        self.assertEqual(root.get_key(), 6)
        self.assertEqual(root.get_left_child().get_key(), 5)
        self.assertEqual(root.get_left_child().get_parent().get_key(), 6)
        self.assertEqual(root.get_left_child().get_left_child(), None)
        self.assertEqual(root.get_left_child().get_right_child(), None)
        self.assertEqual(root.get_right_child().get_key(), 10)
        self.assertEqual(root.get_right_child().get_parent().get_key(), 6)
        self.assertEqual(root.get_right_child().get_left_child(), None)
        self.assertEqual(root.get_right_child().get_right_child(), None)

        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])

    def test_insert_3_nodes_2(self):
        print("Running test_insert_3_nodes_ordered")
        h = AVL([6, 5, 10])
        root = h.get_root()
        self.assertEqual(root.get_key(), 6)
        self.assertEqual(root.get_left_child().get_key(), 5)
        self.assertEqual(root.get_left_child().get_parent().get_key(), 6)
        self.assertEqual(root.get_left_child().get_left_child(), None)
        self.assertEqual(root.get_left_child().get_right_child(), None)
        self.assertEqual(root.get_right_child().get_key(), 10)
        self.assertEqual(root.get_right_child().get_parent().get_key(), 6)
        self.assertEqual(root.get_right_child().get_left_child(), None)
        self.assertEqual(root.get_right_child().get_right_child(), None)
        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])

    def test_insert_3_nodes_3(self):
        print("Running test_insert_3_nodes_ordered")
        h = AVL([5, 10, 6])
        root = h.get_root()
        self.assertEqual(root.get_key(), 6)
        self.assertEqual(root.get_left_child().get_key(), 5)
        self.assertEqual(root.get_left_child().get_parent().get_key(), 6)
        self.assertEqual(root.get_left_child().get_left_child(), None)
        self.assertEqual(root.get_left_child().get_right_child(), None)
        self.assertEqual(root.get_right_child().get_key(), 10)
        self.assertEqual(root.get_right_child().get_parent().get_key(), 6)
        self.assertEqual(root.get_right_child().get_left_child(), None)
        self.assertEqual(root.get_right_child().get_right_child(), None)
        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])

    def test_long_tree(self):
        print("Running test_long_tree")
        h = AVL([20, 10, 25, 5, 18, 13, 15])
        self.check_multiline(str(h), [["18"], ["10", "20"], ["5", "13", "_", "25"], ["_", "_", "_", "15", "_", "_"], ['_', '_'], ["5", "10", "13", "15", "18", "20", "25"]])

    def test_unique_insert(self):
        print("Running test_unique_insert")
        h = AVL()
        a = h.insert(5)
        b = h.insert(5)
        c = h.insert(5)
        self.assertEqual(type(a), type(Node(5)))
        self.assertEqual(a.get_left_child(), None)
        self.assertEqual(a.get_right_child(), None)
        self.assertEqual(a.get_parent(), None)
        self.assertEqual(b, None)
        self.assertEqual(b, None)

    def test_build(self):
        print("Running test_build")
        h = AVL([7, 5, 9, 6, 8])
        self.check_multiline(str(h), [["7"], ["5", "9"], ["_", "6", "8", "_"], ["_", "_", "_", "_"], ["5", "6", "7", "8", "9"]])

    def test_child_parent_link(self):
        print("Running test_child_parent_link")
        h = AVL([21, 17, 11, 15, 6, 5, 8, 1, 9])
        n = h.get_root().get_left_child()
        self.assertEqual(n.get_key(), 6)
        self.assertEqual(n.get_right_child().get_key(), 8)
        self.assertEqual(n.get_parent().get_key(), 11)
        self.assertEqual(n.get_left_child().get_left_child().get_key(), 1)
        self.assertEqual(n.get_left_child().get_left_child().get_parent().get_key(), 5)

    def test_height_insert_only_1(self):
        print("Running test_height_insert_only_1")
        h = AVL()
        h.insert(5)
        self.assertEqual(h.get_root().get_height(), 0)
        h.insert(2)
        self.assertEqual(h.get_root().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_height(), 0)
        h.insert(8)
        self.assertEqual(h.get_root().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(1)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(3)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_left_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(9)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_left_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 1)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_height(), 0)
        self.check_multiline(str(h), [["5"], ["2", "8"], ["1", "3", "_", "9"], ["_", "_" , "_", "_", "_", "_"], ["1", "2", "3", "5", "8", "9"]])

    def test_height_insert_only_2(self):
        print("Running test_height_insert_only_2")
        h = AVL()
        h.insert(5)
        self.assertEqual(h.get_root().get_height(), 0)
        h.insert(2)
        self.assertEqual(h.get_root().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_height(), 0)
        h.insert(8)
        self.assertEqual(h.get_root().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(1)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(3)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_left_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(9)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_left_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 1)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_height(), 0)
        # Balancing after this point
        h.insert(10)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_right_child().get_height(), 1)
        self.assertEqual(h.get_root().get_right_child().get_key(), 9)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_key(), 10)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_left_child().get_key(), 8)
        self.assertEqual(h.get_root().get_right_child().get_left_child().get_height(), 0)
        self.check_multiline(str(h), [["5"], ["2", "9"], ["1", "3", "8", "10"], ["_", "_" , "_", "_", "_", "_", "_", "_"], ["1", "2", "3", "5", "8", "9", "10"]])

    def test_height_delete(self):
        print("Running test_height_delete")
        h = AVL()
        h.insert(5)
        self.assertEqual(h.get_root().get_height(), 0)
        h.insert(2)
        self.assertEqual(h.get_root().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_height(), 0)
        h.insert(8)
        self.assertEqual(h.get_root().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(1)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(3)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_left_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 0)
        h.insert(9)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_left_child().get_height(), 1)
        self.assertEqual(h.get_root().get_left_child().get_left_child().get_height(), 0)
        self.assertEqual(h.get_root().get_left_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_height(), 1)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_height(), 0)
        # Balancing after this point
        h.insert(10)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_right_child().get_height(), 1)
        self.assertEqual(h.get_root().get_right_child().get_key(), 9)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_key(), 10)
        self.assertEqual(h.get_root().get_right_child().get_right_child().get_height(), 0)
        self.assertEqual(h.get_root().get_right_child().get_left_child().get_key(), 8)
        self.assertEqual(h.get_root().get_right_child().get_left_child().get_height(), 0)
        self.check_multiline(str(h), [["5"], ["2", "9"], ["1", "3", "8", "10"], ["_", "_" , "_", "_", "_", "_", "_", "_"], ["1", "2", "3", "5", "8", "9", "10"]])
        h.delete(9)
        self.assertEqual(h.get_root().get_height(), 2)
        self.assertEqual(h.get_root().get_right_child().get_height(), 1)
        self.assertEqual(h.get_root().get_right_child().get_key(), 10)
        self.assertEqual(h.get_root().get_right_child().get_left_child().get_key(), 8)
        self.assertEqual(h.get_root().get_right_child().get_left_child().get_height(), 0)
        self.check_multiline(str(h), [["5"], ["2", "10"], ["1", "3", "8", "_"], ["_", "_", "_", "_", "_", "_"], ["1", "2", "3", "5", "8", "10"]])


    def test_simple_delete_1(self): # XX
        print("Running test_simple_delete_1")
        h = AVL([6, 5, 10])
        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])
        h.delete(5)
        self.check_multiline(str(h), [["6"], ["_", "10"], ["_", "_"], ["6", "10"]])

    def test_simple_delete_2(self): # XX
        print("Running test_simple_delete_2")
        h = AVL([6, 5, 10])
        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])
        h.delete(10)
        self.check_multiline(str(h), [["6"], ["5", "_"], ["_", "_"], ["5", "6"]])

    def test_simple_delete_3(self): # XX
        print("Running test_simple_delete_3")
        h = AVL([6, 5, 10])
        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])
        h.delete(6)
        self.check_multiline(str(h), [["10"], ["5", "_"], ["_", "_"], ["5", "10"]])

    def test_simple_delete_4(self): # XX
        print("Running test_simple_delete_4")
        h = AVL([6, 4, 5, 10])
        self.check_multiline(str(h), [["5"], ["4", "6"], ["_", "_", "_", "10"], ["_", "_"], ["4", "5", "6", "10"]])
        h.delete(4)
        self.check_multiline(str(h), [["6"], ["5", "10"], ["_", "_", "_", "_"], ["5", "6", "10"]])

    def test_delete_case_1(self):
        print("Running test_delete_case_1")
        h = AVL([50, 30, 70, 20, 40, 60, 80])
        h.delete(20)
        self.check_multiline(str(h), [["50"], ["30", "70"], ["_", "40", "60", "80"], ["_", "_", "_", "_", "_", "_"], ["30", "40", "50", "60", "70", "80"]])

    def test_delete_case_2(self):
        print("Running test_delete_case_2")
        h = AVL([50, 30, 70, 20, 40, 60, 80])
        h.delete(20)
        self.check_multiline(str(h), [["50"], ["30", "70"], ["_", "40", "60", "80"], ["_", "_", "_", "_", "_", "_"], ["30", "40", "50", "60", "70", "80"]])
        h.delete(30)
        self.check_multiline(str(h), [["50"], ["40", "70"], ["_", "_", "60", "80"], ["_", "_", "_", "_"], ["40", "50", "60", "70", "80"]])

    def test_delete_case_3(self):
        print("Running test_delete_case_3")
        h = AVL([50, 30, 70, 20, 40, 60, 80])
        h.delete(20)
        self.check_multiline(str(h), [["50"], ["30", "70"], ["_", "40", "60", "80"], ["_", "_", "_", "_", "_", "_"], ["30", "40", "50", "60", "70", "80"]])
        h.delete(30)
        self.check_multiline(str(h), [["50"], ["40", "70"], ["_", "_", "60", "80"], ["_", "_", "_", "_"], ["40", "50", "60", "70", "80"]])
        h.delete(50)
        self.check_multiline(str(h), [["60"], ["40", "70"], ["_", "_", "_", "80"], ["_", "_"], ["40", "60", "70", "80"]])

    def test_insert_connections(self):
        print("Running test_delete_case_3")
        h = AVL()
        # Start checking all connections
        node_20 = h.insert(20)
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent(), None)
        self.assertEqual(node_20.get_left_child(), None)
        self.assertEqual(node_20.get_right_child(), None)
        node_25 = h.insert(25)
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent(), None)
        self.assertEqual(node_20.get_left_child(), None)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)
        node_10 = h.insert(10)
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent(), None)
        self.assertEqual(node_20.get_left_child().get_key(), 10)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)
        self.assertEqual(node_10.get_key(), 10)
        self.assertEqual(node_10.get_parent().get_key(), 20)
        self.assertEqual(node_10.get_left_child(), None)
        self.assertEqual(node_10.get_right_child(), None)
        node_18 = h.insert(18)
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent(), None)
        self.assertEqual(node_20.get_left_child().get_key(), 10)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)
        self.assertEqual(node_10.get_key(), 10)
        self.assertEqual(node_10.get_parent().get_key(), 20)
        self.assertEqual(node_10.get_left_child(), None)
        self.assertEqual(node_10.get_right_child().get_key(), 18)
        self.assertEqual(node_18.get_key(), 18)
        self.assertEqual(node_18.get_parent().get_key(), 10)
        self.assertEqual(node_18.get_left_child(), None)
        self.assertEqual(node_18.get_right_child(), None)
        node_13 = h.insert(13)
        # Incase students somehow swap values instead of connections and we do have a rotation here:
        node_20 = h.get_root()
        node_25 = h.get_root().get_right_child()
        node_10 = h.get_root().get_left_child().get_left_child()
        node_18 = h.get_root().get_left_child().get_right_child()
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent(), None)
        self.assertEqual(node_20.get_left_child().get_key(), 13)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)
        self.assertEqual(node_10.get_key(), 10)
        self.assertEqual(node_10.get_parent().get_key(), 13)
        self.assertEqual(node_10.get_left_child(), None)
        self.assertEqual(node_10.get_right_child(), None)
        self.assertEqual(node_18.get_key(), 18)
        self.assertEqual(node_18.get_parent().get_key(), 13)
        self.assertEqual(node_18.get_left_child(), None)
        self.assertEqual(node_18.get_right_child(), None)
        self.assertEqual(node_13.get_key(), 13)
        self.assertEqual(node_13.get_parent().get_key(), 20)
        self.assertEqual(node_13.get_left_child().get_key(), 10)
        self.assertEqual(node_13.get_right_child().get_key(), 18)
        node_5 = h.insert(5)
        # Incase students somehow swap values instead of connections and we do have a rotation here:
        node_13 = h.get_root()
        node_20 = h.get_root().get_right_child()
        node_25 = h.get_root().get_right_child().get_right_child()
        node_10 = h.get_root().get_left_child()
        node_18 = h.get_root().get_right_child().get_left_child()
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent().get_key(), 13)
        self.assertEqual(node_20.get_left_child().get_key(), 18)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)
        self.assertEqual(node_10.get_key(), 10)
        self.assertEqual(node_10.get_parent().get_key(), 13)
        self.assertEqual(node_10.get_left_child().get_key(), 5)
        self.assertEqual(node_10.get_right_child(), None)
        self.assertEqual(node_18.get_key(), 18)
        self.assertEqual(node_18.get_parent().get_key(), 20)
        self.assertEqual(node_18.get_left_child(), None)
        self.assertEqual(node_18.get_right_child(), None)
        self.assertEqual(node_13.get_key(), 13)
        self.assertEqual(node_13.get_parent(), None)
        self.assertEqual(node_13.get_left_child().get_key(), 10)
        self.assertEqual(node_13.get_right_child().get_key(), 20)
        self.assertEqual(node_5.get_key(), 5)
        self.assertEqual(node_5.get_parent().get_key(), 10)
        self.assertEqual(node_5.get_left_child(), None)
        self.assertEqual(node_5.get_right_child(), None)
        node_15 = h.insert(15)
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent().get_key(), 13)
        self.assertEqual(node_20.get_left_child().get_key(), 18)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)
        self.assertEqual(node_10.get_key(), 10)
        self.assertEqual(node_10.get_parent().get_key(), 13)
        self.assertEqual(node_10.get_left_child().get_key(), 5)
        self.assertEqual(node_10.get_right_child(), None)
        self.assertEqual(node_18.get_key(), 18)
        self.assertEqual(node_18.get_parent().get_key(), 20)
        self.assertEqual(node_18.get_left_child().get_key(), 15)
        self.assertEqual(node_18.get_right_child(), None)
        self.assertEqual(node_13.get_key(), 13)
        self.assertEqual(node_13.get_parent(), None)
        self.assertEqual(node_13.get_left_child().get_key(), 10)
        self.assertEqual(node_13.get_right_child().get_key(), 20)
        self.assertEqual(node_5.get_key(), 5)
        self.assertEqual(node_5.get_parent().get_key(), 10)
        self.assertEqual(node_5.get_left_child(), None)
        self.assertEqual(node_5.get_right_child(), None)
        self.assertEqual(node_15.get_key(), 15)
        self.assertEqual(node_15.get_parent().get_key(), 18)
        self.assertEqual(node_15.get_left_child(), None)
        self.assertEqual(node_15.get_right_child(), None)
        self.check_multiline(str(h), [["13"], ["10", "20"], ["5", "_", "18", "25"], ["_", "_", "15", "_", "_", "_"], ['_', '_'], ["5", "10", "13", "15", "18", "20", "25"]])

    def test_delete_connections(self):
        print("Running test_delete_connections")
        h = AVL([20, 25, 10, 18, 13, 5, 15])
        self.check_multiline(str(h), [["13"], ["10", "20"], ["5", "_", "18", "25"], ["_", "_", "15", "_", "_", "_"], ['_', '_'], ["5", "10", "13", "15", "18", "20", "25"]])
        h.delete(5)
        node_18 = h.get_root()
        node_13 = node_18.get_left_child()
        node_20 = node_18.get_right_child()
        node_10 = node_13.get_left_child()
        node_15 = node_13.get_right_child()
        node_25 = node_20.get_right_child()
        self.assertEqual(node_18.get_key(), 18)
        self.assertEqual(node_18.get_parent(), None)
        self.assertEqual(node_18.get_left_child().get_key(), 13)
        self.assertEqual(node_18.get_right_child().get_key(), 20)
        self.assertEqual(node_13.get_key(), 13)
        self.assertEqual(node_13.get_parent().get_key(), 18)
        self.assertEqual(node_13.get_left_child().get_key(), 10)
        self.assertEqual(node_13.get_right_child().get_key(), 15)
        self.assertEqual(node_20.get_key(), 20)
        self.assertEqual(node_20.get_parent().get_key(), 18)
        self.assertEqual(node_20.get_left_child(), None)
        self.assertEqual(node_20.get_right_child().get_key(), 25)
        self.assertEqual(node_10.get_key(), 10)
        self.assertEqual(node_10.get_parent().get_key(), 13)
        self.assertEqual(node_10.get_left_child(), None)
        self.assertEqual(node_10.get_right_child(), None)
        self.assertEqual(node_15.get_key(), 15)
        self.assertEqual(node_15.get_parent().get_key(), 13)
        self.assertEqual(node_15.get_left_child(), None)
        self.assertEqual(node_15.get_right_child(), None)
        self.assertEqual(node_25.get_key(), 25)
        self.assertEqual(node_25.get_parent().get_key(), 20)
        self.assertEqual(node_25.get_left_child(), None)
        self.assertEqual(node_25.get_right_child(), None)

    def test_general_functions(self): # XX
        print("Running test_general_functions")
        # Add a number of elements to at least prevent some possible toy-example working out
        h = AVL([50, 70, 80, 60, 55, 67, 90, 57, 20, 10, 15, 0])
        self.assertEqual(h.find_min(), 0)
        self.assertEqual(h.find_max(), 90)
        self.assertFalse(h.is_empty())
        n = h.search(67)
        m = h.search(99)
        self.assertTrue(isinstance(n, Node))
        self.assertEqual(n.get_key(), 67)
        self.assertEqual(m, None)
        self.assertTrue(h.contains(67))
        self.assertFalse(h.contains(100))

    def test_breadth_first_traversal(self):
        print("Running test_breadth_first_traversal")
        h = AVL()
        n1 = h.insert(20)
        n2 = h.insert(10)
        n3 = h.insert(25)
        n4 = h.insert(5)
        n5 = h.insert(18)
        b = h.breadth_first_traversal()
        ground_truth = [n1, n2, n3, n4, n5, None, None, None, None, None, None]
        for layer in b:
            for element in layer:
                # Check if there are still elements that could be processed
                self.assertTrue(len(ground_truth) > 0)
                gt = ground_truth.pop(0)
                self.assertTrue(isinstance(element, Node) or element is None)
                self.assertEqual(element, gt)
        # All elements should have been processed.
        self.assertTrue(len(ground_truth) == 0)

    def test_in_order_traversal(self):
        print("Running test_in_order_traversal")
        h = AVL()
        n1 = h.insert(20)
        n2 = h.insert(10)
        n3 = h.insert(25)
        n4 = h.insert(5)
        n5 = h.insert(18)
        order = h.in_order_traversal()
        ground_truth = [n4, n2, n5, n1, n3]
        for element in order:
                # Check if there are still elements that could be processed
                self.assertTrue(len(ground_truth) > 0)
                gt = ground_truth.pop(0)
                self.assertTrue(isinstance(element, Node))
                self.assertEqual(element, gt)
        # All elements should have been processed.
        self.assertTrue(len(ground_truth) == 0)

if __name__ == "__main__":
    unittest.main()

# Meerdere Deletes
# Insert-Delete-Insert
# Split into different files, return 0 if successful and 1 otherwise.
