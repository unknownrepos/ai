from sympy import symbols, And, Or, Not, Implies, satisfiable

# Define predicates and variables
P = symbols('P')
Q = symbols('Q')
x = symbols('x')

# Define some first-order logic expressions
# For example: P(x) ∧ Q(x)
formula1 = And(P(x), Q(x))

# For example: (P(x) ∧ Q(x)) ∨ ¬P(x)
formula2 = Or(formula1, Not(P(x)))

# For example: (P(x) ∧ Q(x)) → P(x)
formula3 = Implies(formula1, P(x))

# Check satisfiability of a formula
print("Is formula 1 satisfiable?", satisfiable(formula1))

# Check if a formula implies another formula
print("Does formula 2 imply formula 3?", Implies(formula2, formula3).simplify())
