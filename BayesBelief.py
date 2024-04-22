from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian network
model = BayesianModel([('A', 'C'), ('B', 'C')])

# Define conditional probability distributions (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.3], [0.7]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.6], [0.4]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.9, 0.7, 0.1],   # P(C | A, B)
                           [0.2, 0.1, 0.3, 0.9]],
                   evidence=['A', 'B'],
                   evidence_card=[2, 2])

# Add CPDs to the model
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Check if the model is valid (i.e., if the CPDs are consistent)
assert model.check_model()

# Perform inference
inference = VariableElimination(model)
posterior_c = inference.query(variables=['C'])
print("P(C):")
print(posterior_c)

# You can also perform inference for specific evidence
posterior_c_given_a = inference.query(variables=['C'], evidence={'A': 0})
print("P(C | A=0):")
print(posterior_c_given_a)
