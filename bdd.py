import random
from typing import List, Optional

class BDD:
    def __init__(self, i: int, high: Optional['BDD'], low: Optional['BDD']):  
        self.i = i  
        self.high = high  
        self.low = low  

listOfNodes: List = [BDD(129, None, None),BDD(130, None, None)]

def bdd_false() -> BDD:
    return listOfNodes[0]

def bdd_true() -> BDD:
    return listOfNodes[1]

def create_node(index: int, high: Optional[BDD], low: Optional[BDD]) -> BDD:
    for node in listOfNodes:
        if node.i == index and node.high == high and node.low == low:
            return node
    new_node = BDD(index, high, low)
    listOfNodes.append(new_node)
    return new_node

def add_new_variable(i: int) -> BDD:
    return create_node(i, bdd_true(), bdd_false())

def compute_value(subtree: Optional[BDD], index: int, value: bool) -> Optional[BDD]:
    if subtree is None:
        return None
    if subtree.i > index:  
        return subtree
    elif subtree.i < index:  
        return create_node(
            subtree.i,
            compute_value(subtree.high, index, value),
            compute_value(subtree.low, index, value),
        )
    else:  # subtree.i == index
        return compute_value(subtree.high if value else subtree.low, index, value)

def ITE(if_node: Optional[BDD], then_node: Optional[BDD], else_node: Optional[BDD]) -> Optional[BDD]:
    if if_node == bdd_true():
        return then_node
    if if_node == bdd_false():
        return else_node
    if then_node == else_node:
        return then_node
    if then_node == bdd_true() and else_node == bdd_false():
        return if_node

    smallest_index = min(if_node.i, then_node.i,else_node.i)

    if_node_computed_true = compute_value(if_node, smallest_index, True)
    then_node_computed_true = compute_value(then_node, smallest_index, True)
    else_node_computed_true = compute_value(else_node, smallest_index, True)
    ITE_true = ITE(if_node_computed_true, then_node_computed_true, else_node_computed_true)

    if_node_computed_false = compute_value(if_node, smallest_index, False)
    then_node_computed_false = compute_value(then_node, smallest_index, False)
    else_node_computed_false = compute_value(else_node, smallest_index, False)
    ITE_false = ITE(if_node_computed_false, then_node_computed_false, else_node_computed_false)

    return create_node(smallest_index, ITE_true, ITE_false)

# Logicke operacije
def bdd_not(f: Optional[BDD]) -> Optional[BDD]:
    return ITE(f, bdd_false(), bdd_true())

def bdd_and(f: Optional[BDD], g: Optional[BDD]) -> Optional[BDD]:
    return ITE(f, g, bdd_false())

def bdd_or(f: Optional[BDD], g: Optional[BDD]) -> Optional[BDD]:
    return ITE(f, bdd_true(), g)

def bdd_xor(f: Optional[BDD], g: Optional[BDD]) -> Optional[BDD]:
    return ITE(f, bdd_not(g), g)

def bdd_eq(f: Optional[BDD], g: Optional[BDD]) -> Optional[BDD]:
    return ITE(f, g, bdd_not(g))

def bdd_imp(f: Optional[BDD], g: Optional[BDD]) -> Optional[BDD]:
    return ITE(f, g, bdd_true())

# BFS
def print_bdd(root: Optional[BDD]):
    if root is None:
        return

    queue = [root]
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.pop(0)
            if current == bdd_true():
                print("T ", end="")
            elif current == bdd_false():
                print("F ", end="")
            else:
                print(f"p{current.i} ", end="")
                if current.low:
                    queue.append(current.low)
                if current.high:
                    queue.append(current.high)
        print()