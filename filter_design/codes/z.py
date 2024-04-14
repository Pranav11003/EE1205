import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s =3.1784e-4 * s**4 / (s**8 + 0.1203*s**7 + 0.7919*s**6 + 0.0709*s**5 + 0.2320*s**4 +  0.0138*s**3 + 0.0298*s**2 + 0.0009*s + 0.0042)
# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)
