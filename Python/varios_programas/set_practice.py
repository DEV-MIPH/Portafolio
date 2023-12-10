#Set es como una lista pero sin ningun orden
planetas = {"Marte", "Jupiter", "Venus"}
print (planetas)
print(len(planetas))
#revisar si un elemento esta presente
print ("Marte" in planetas)
#Agregar mas elemento mas al set
planetas.add("Tierra")
print(planetas)
#No se puede duplicar un item
planetas.add("Tierra")
print(planetas)
#Eliminar elementos (En caso de no estar el item tira KeyError)
planetas.remove("Tierra")
print(planetas)
#Discard tambien sirve para eliminar un item pero si no esta no tira error
planetas.discard("Jupiter")
print(planetas)
planetas.discard("Jupiter")
print(planetas)
#limpiar set
planetas.clear()
print(planetas)
#Eliminar Set
del planetas
print(planetas)