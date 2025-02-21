from molmass import Formula

def calc_massa_molar(formula_molecula):
    formula = Formula(formula_molecula)
    mass = formula.mass
    return mass

entrada_formula = input(str("Digite a formula molecular: "))
massa_molecula = calc_massa_molar(entrada_formula)
print(massa_molecula) 