"""
Variables are container and it is used to store the values.
"""
print("Declaration of variables:")
# Store int value
v1 = 1
print(v1)
# store float value
v2 = 10.4
print(v2)
# store string value
v3 = "hello sandeep"
print(v3)

print("\n*****************\n")

print("Assign same value to multiple variables:")
x = y = z = 13
print(x)
print(y)
print(z)

print("\n*****************\n")

print("Assign multiple values to multiple variables:")
v_int, v_numeric, v_string, v_bool = 12, 12.5, "Hello", True
print(v_int)
print(v_numeric)
print(v_string)
print(v_bool)

print("\n*****************\n")

print("Variables are case-sensitive")
# small a store "hello" and capital A store "Sandeep"
a = "hello"
A = "Sandeep"
print(a + " " + A)
