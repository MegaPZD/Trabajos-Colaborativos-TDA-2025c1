import pulp as p 

# Creamos una instancia del problema de Programacion Lineal / Declaramos el Modelo:
modelo = p.LpProblem("Concesiones Argentina 2000 SRL", p.LpMaximize)

# Creamos de variables:

#Variables binarias:
c_a = p.LpVariable("Cliente A", cat = "Binary")
c_b1 = p.LpVariable("Cliente B primera oferta", cat = "Binary")
c_b2 = p.LpVariable("Cliente B segunda oferta", cat = "Binary")
c_c = p.LpVariable("Cliente C", cat = "Binary")
c_d = p.LpVariable("Cliente D", cat = "Binary")
c_e = p.LpVariable("Cliente E", cat = "Binary")
c_f = p.LpVariable("Cliente F", cat = "Binary")
c_g = p.LpVariable("Cliente G", cat = "Binary")

# Definimos la funcion objetivo
modelo += 50000 * c_a + 100000 * c_b1 + 120000 * c_b2 +  100000 * c_c + 80000 * c_d + 5000 * c_e + 40000 * c_f + 90000 * c_g, "Beneficio Total"

# Definimos las restricciones
modelo += 30 * c_a + 80 * c_b1 + 120 * c_b2 + 75 * c_c + 50 * c_d + 2 * c_e + 20 * c_f + 100 * c_g <= 200, "Restriccion sobre la cantidad de paradas" 

modelo += c_b1 + c_b2 <= 1, "Restriccion sobre el cielnte B, solo puede haber una oferta"

modelo += c_a + c_d <= 1, "Restriccion por incompatibilidad entre los clientes A y D"
 
# Resolvemos el problema
modelo.solve()

with open("resultado_concesiones.txt", "w") as f:
    f.write(f"Estado de la solucion: {p.LpStatus[modelo.status]}\n")
    f.write(f"Beneficio total optimo: ${p.value(modelo.objective)}\n\n")
    f.write("Clientes seleccionados:\n")
    for variable in modelo.variables():
        f.write(f"{variable.name} = {int(variable.varValue)}\n")


