from bdd import add_new_variable, print_bdd, bdd_or, bdd_and, bdd_not, bdd_xor, bdd_imp, bdd_eq
from sat_solve import SAT_solver, SAT_valuations

def main():
    p1 = add_new_variable(1)
    p2 = add_new_variable(2)
    p3 = add_new_variable(3)

    tree1 = bdd_and(p1, p2)
    print_bdd(tree1)
    print("Formula p1 & p2 is satisfiable:", SAT_solver(tree1)) 
    print(SAT_valuations(tree1))
    print("___________________")

    tree2 = bdd_and(p1, bdd_not(p1))
    print_bdd(tree2)
    print("Formula p1 & ~p1 is satisfiable:", SAT_solver(tree2))
    print(SAT_valuations(tree2))
    print("___________________")

    print("BDD for p1 | p2 | p3:")
    tree3 = bdd_or(bdd_or(p1, p2), p3)
    print_bdd(tree3)
    print("Formula p1 | p2 | p3 is satisfiable:", SAT_solver(tree3))
    print(SAT_valuations(tree3))
    print("___________________")

    print("BDD for (p1 | p2) & (`~p1 | p2 ) & ~p2")
    tree4 = bdd_and(bdd_and(bdd_or(p1,p2),bdd_or(bdd_not(p1),p2)),bdd_not(p2))
    print_bdd(tree4)
    print("Formula (p1 | p2) & (`~p1 | p2 ) & ~p2 is satisfiable:", SAT_solver(tree4))
    print(SAT_valuations(tree4))
    print("___________________")

    print("BDD for (p1 | p2) ^ p3:")
    tree5 = bdd_xor(bdd_or(p1, p2), p3)
    print_bdd(tree5)
    print("Formula (p1 | p2) ^ p3 is satisfiable:", SAT_solver(tree5))
    print(SAT_valuations(tree5))
    print("___________________")

    print("BDD for p1 => p2:")
    tree6 = bdd_imp(p1, p2)
    print_bdd(tree6)
    print("Formula (p1 => p2) is satisfiable:", SAT_solver(tree6))
    print(SAT_valuations(tree6))
    print("___________________")

    # test 
    '''
    tree = 
    print_bdd(tree)
    print("Formula is satisfiable:", SAT_solver(tree))
    print(SAT_valuations(tree))
    '''

if __name__ == "__main__":
    main()