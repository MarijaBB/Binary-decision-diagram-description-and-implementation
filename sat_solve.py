from bdd import BDD, bdd_true, bdd_false
from typing import Dict, Optional

def solver_rec(tree: Optional[BDD]):
    if tree is None:
        return False

    # Bazni slučajevi - došli smo do listova
    if tree == bdd_true():
        return True  
    if tree == bdd_false():
        return False  

    # proveri high i low granu, da li neka vodi ka true listu
    high_result = solver_rec(tree.high)
    low_result = solver_rec(tree.low)
  
    return high_result or low_result

def SAT_solver(tree: Optional[BDD]) -> bool:
    if tree is None:
        return False
    if tree == bdd_false():
        return False
    return solver_rec(tree)


def find_valuations(tree: Optional[BDD], valuations: Dict[int, bool]) -> Optional[Dict[int, bool]]:
    if tree is None:
        return None

    # Bazni slucaj: dosli smo do T, vrati trenutnu valuaciju promneljivih
    if tree == bdd_true():
        return valuations
    # Bazni slucaj: dosli smo do F, nema valuacije za koje je formula zadovoljiva
    if tree == bdd_false():
        return None

    # trenutna promenljiva se valuira na T
    valuations[tree.i] = True
    result = find_valuations(tree.high, valuations.copy()) 
    if result is not None: # tree == bdd_true()
        return result  

    # trenutna promenljiva se valuira na F
    valuations[tree.i] = False
    result = find_valuations(tree.low, valuations.copy())  
    if result is not None: # tree == bdd_true()
        return result  

    return None

def SAT_valuations(tree: Optional[BDD]) -> Optional[Dict[int, bool]]:
    if tree is None:
        return None
    if tree == bdd_false():
        return None 
    return find_valuations(tree, {})  

