import modulo

print()
print("modulo imported")
print()

from modulo.submodulo.subsubmodulo import func_b

print()
print("subsubmodulo imported")
print()

print("llamando a funcion")
print(modulo.funcion(32))

print("llamando a funcion")
print(func_b(32))
