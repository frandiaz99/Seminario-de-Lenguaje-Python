import pprint

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR','David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo','Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan','Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias','Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises','Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

## A 
names = nombres.split(',')

print("-"*100)
print("-"*35, " Diccionario Nota ", "-"*35)
print("-"*100)
print()

notes = dict(zip(names,zip(notas_1,notas_2))) #Creacio de diccionario
pprint.pprint(notes) #impresio de diccioario mas linda

print("-"*100)
print("-"*35, " Diccionario Promedios ", "-"*35)
print("-"*100)
print()

## B
prom = dict(map(lambda x: (x, sum(notes[x])/len(notes[x])), notes)) #Creacion diccionario 'prom' a partir de datos del diccionario 'notes'.
pprint.pprint(prom) 

print()
print("-"*100)
print()

## C
prom_total = sum(prom.values()) / len(prom) #promedio de la cursada
print(f"Promedio de la cursada: {prom_total:.2f} ")

## D
mejor_prom = max(prom, key= prom.get) #alumno con mejor promedio
print(f"Estudiante con la nota promedio mas alta: {mejor_prom}")

## E
peor_nota = min(notes, key=lambda x: min(notes[x])) #alumno con peor nota
print("Estudiante con la nota más baja:", peor_nota)

print()