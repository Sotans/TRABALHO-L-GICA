#junta todas clausulas unitarias em uma lista
def unit_clauses(clauses):
    units = []

    for i in clauses:
        if len(i) == 1:
            units.append(i)
    return units

#tratamento de entrada de dados
def get_clauses():
    arq = open("entrada.txt")
    lines = list(arq.readlines())

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        lines[i] = lines[i].split(' ')

    num_clauses = int(lines[0][0])
    num_atoms = int(lines[0][1])
    lines.remove(lines[0])

    clauses = []
    for i in lines:
        lista_unit_clause = []
        for j in i:
            i = (int(j))
            lista_unit_clause.append(i)
        clauses.append(lista_unit_clause)
    
    return clauses
#apaga de F todas clausulas que contem L
def del_clause(unit_clause, clauses):
    new_clauses = []

    for i in clauses:
        if unit_clause not in i:
            new_clauses.append(i)
    return new_clauses 

#apaga -L das clausulas restantes
def erase_literal(unit_clause, clauses):
    new_clauses = []
    
    for i in clauses:
        new_clause = []
        for j in i:
            if -1 * unit_clause != j:
                new_clause.append(j)
        new_clauses.append(new_clause)
                
    return new_clauses

def simplifying(clauses):
    units = unit_clauses(clauses)

    while len(units) != 0:
        unit_clause = units[0][0]

        clauses = del_clause(unit_clause, clauses)
        clauses = erase_literal(unit_clause, clauses)

        units.remove(units[0])
        units = unit_clauses(clauses)

    return clauses

def DPLL(clauses):
    f_line = simplifying(clauses)

    print(f_line)


#inicio
clauses = get_clauses()

print('Original F:',clauses)

DPLL(clauses)





