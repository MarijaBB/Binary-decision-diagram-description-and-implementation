BDD.pdf sadrži opis rada BDD-a, opis metoda, implementaciju, primene...

Program se na Windows-u pokreće sa python main.py.

Na Linux-u sa python3 main.py.

Svoj input možete testirati u samom main-u. Možete dodati još atoma, ali koristiti samo slovo p.

Na primer:<br>
p5 = add_new_variable(5)<br>
p6 = add_new_variable(6)<br>
tree = bdd_eq(p5, p6)       # p5 <=> p6 <br>
print_bdd(tree)<br>
print(SAT_solver(tree))<br>
print(SAT_valuations(tree))<br>
