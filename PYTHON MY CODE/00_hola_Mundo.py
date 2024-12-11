print("Hello Word")

print("hello world")

# Diferenciar cadenas de String cuando el codigo tiene mayusculas o minusculas o mas caracteres
print("Hello World")
print("MY WORLD IS WONDERFUL")

# comando type indica el tipo de dato es fuck the world
print(type("HOLA WORLD"))

# este comando concadena strings mediante +
print(type("El Examen es " + " mañana "))
print("Si no estudias " + " No sabras contestar")

# Numbers . entero(into entero) o decimal(float o punto flotante )

# Integer
print(2854)

# Float ( datos de temperratura por ejemplo )
print(2.021)

# dato Boolean ( para definir tipo de estado )
True
False

# List para agrupar listas de datos se usa la coma para separar elementos
[10, 20, 30, 40, 7272]
["hello", "bye", "fuck"]

# en lista puedo incluir cualquier tipo de dato que se conozca
[True, 283, "COME BIEN", 28367.75]

# Tuples (se le conoce como inmutable a esta otra manera,otra manera de agrupar datos, para datos que no cambian como podemos hacer en la lista )
(10, 20, 30)


# tupla vacia
()

# Dictionaries te permiten agrupar datos que pertenecen a una misma entidad, Note que cada dato se separa con : separando la clave(key) del valor (value)
{"Name": "Marcus", "Empleo": "Alumno", "Indicativo": "311"}

print(type({"Avena": "tresTazas", "HUevos": "dosHuevos", "Banana": "mediaBanana"}))


# tipo de dato None es un tipo de dato que no tiene nada , no esta definido aun por ningun tipo de dato
None


# Escribe un programa que pregunte tu nombre y te salude.


nombre_servidor = "srvinfotdw01"
cantidad_memoria = 2048
uso_cpu = 85.5
estado = True
# Se utiliza type para saber el tipo de variable
print(type(nombre_servidor))
print(type(cantidad_memoria))
print(type(uso_cpu))
print(type(estado))
# Aqui vemos dos formas de concadenar, con comas y con `+` y el formato string. tambien existe otra que nombrare en el siguiente comentario.
print(f'mi servidor {nombre_servidor}'+'usa un tipo de variable', type((nombre_servidor)), ',la cantidad de memoria de mi servidor usa el tipo de variable',type((cantidad_memoria)) , ', en cambio el uso la variable uso de cpu usa una '+ str(type((uso_cpu))))

#
nombre= ' Marcus '
edad= 42
dinero_en_el_banco= 0.001
trabajador= False

# print( f'Este tio {nombre}'+ str(f'tiene una edad  de {edad} años de tipo '+ str(type(edad)) ), 'no tiene un duro en el banco solo tiene ', dinero_en_el_banco, 'euros')

# nombre = input('¿Cómo te llamas? ')  # Captura el nombre del usuario
# print('Hola' + str(nombre) ) # Saluda al usuario


# ingresarNombre = input("introduzca su nombre:")
# print(ingresarNombre)

# age = bool( input("introduzca su edad"))
# print (type(age))

# num1 = int(input(" Introduzca un numero : "))
# num2 = int(input(" Introduzca un numero : "))
# print (num1+num2)

#lista
lista = [ "pepe", 45, 1.69, 'Salamanca', True]

#tuplas
empleosSuboficiales=('Sargento', 'Sargento 1º', 'Brigada')
print (empleosSuboficiales)

print(lista[3])

#Dictionary

datosAlumno ={
    'Nombre': ' Marcus',
    'edad': 42,
    'casado': False,
    'Direccion': 'Psje Pezuela 32',
    'Ciudad': 'Malaga'
    
}
print(datosAlumno)
print(datosAlumno["edad"])
print('Este caballero vive en:', datosAlumno["Direccion"])

# El siguiente comando me sirve para imprimir datos por indice de la string nombre 
nombre = 'Marcus Hinestroza Torres'
print(nombre[4])
#el siguiente me dira la longitud de la cadena nombre, cuentan los espacios.
print(len(nombre))

# para crear subconjuntos, esto nos servira para mostrar informacion requerida , o filtrar informacion de listas
cadena = 'cadena De texto'
print(cadena[2:8])
print(cadena[2:8:1])# El ultimo numero indica el paso, como este es uno es como si no lo indicaramos, porque avanzara imprimiendo de uno en uno cada ubicacion del indice.
print(cadena[0:4])
print(cadena[0:12:2])# los pasos le indicaran que debe imprimir de 2 en 2 en este caso el paso es el 2 el ultimo numero.
print(cadena[0:20])#Aunque nos pasemos de indice en el fin del codigo

#metodos de las cadenas, estan hechos , codificados y entonces nos valemos de estos para determinadas tareas. utilizamos el mombre de la cadena un punto '.' y el metodo con sus argumentos si los requiere.
#primer metodo que vemos es capitalize

print(cadena.capitalize())

#metodo .count
print(cadena.count('de'))# me devuelve cuantas veces existe ese caracter en la variable o string.Recuerda que es caseSensitive, identificara mayusculas o minusculas y discriminara entre ellas, aqui por ejemplo me indicara que tememos un solo caracter similar, diferenciando 'de' de 'De'.

print(cadena.find('e')) # Con este comando me devolvera el indice donde esta ubicado 

print(cadena.upper()) # Este comando devuelve la cadena o variable en mayusculas

print(cadena.replace('e', 'i')) # Este comando reemplazara las e por las i, podemos usarlo para quitar cosas de un documento extenso con muchisimas cosas  que queremos cambiar.

print(cadena.lower()) # Este comando devuelve todo en minisculas

cadena2='esto es una cadena, es de texto muy larga'
lista_palabras = cadena2.split(',')# Esto nos cortara donde le indiquemos , en este caso en las ',' comas
print(lista_palabras)
print('la cadena de texto tiene: ', len(lista_palabras),' palabras ') #

#Condicionales

# funciones observe que hay un if dentro de otro if, lo que llamamos if anidado

pepe = 'Jose'
persona = False
if pepe == 'Jose':
    print('Pepe Cabron')
    if persona == True:
        print('Que pasa Pepe? ')
    else:
        print('vamos a beber Pepe !!')
else:
    print('quien eres ?')
    
    
    #Condicionales Multiples ira por una sola rama que ejecutara un codigo determinado de opciones multiples dependiendo del resultado.
    
distancia = 8

if distancia < 2:
    print('Puedes Caminar')
elif distancia <= 10:
    print('usa bike')
else:
    print('correeee !!!')
    
    
    # operadores de comparacion logica
    
    clima = input('como esta el clima ? ( Soleado o lluvioso)').lower()
    temperatura = int(input('cual es la temperatura (Cº):'))
    # horario = input('el evento es de dia o de noche ?: ').lower()
    #Variables predefinidas
    clima_predefinido = 'soleado'
    temperatura_predeterminada = 24
    # horario_predefinido = 'dia'
    
    if clima == 'soleado' and temperatura > 20:
        print('Es un buen dia para salir ')
    elif clima == 'lluvioso' or temperatura < 10:
        print('Mejor quedate en casa ')
    else:
        print('Sal si te sientes comodo')



# ingresarActividad = input("Que quieres hacer entrenar o jugar ?:")  
# temperatura_comida = int(input(" Cuantos años tienes?  : ")) 


# Actividad = 'Comer'
# temperatura_comida = 8


# if ingresarActividad == 'entrenar' and temperatura_comida < 10:
#     print('te sugiero un helado')
# elif ingresarActividad != 'entrenar':
#     print(ingresarActividad + ' !! ?, esto no es una actividad. '+ 'Eres muy joven para hacer eso, Aqui solo se hace lo que yo diga :')
# else:
#     print('Parece que eres mayor ya, ¡realiza otra actividad  de adultos!')
    
corte = ''   
peinado = ''
corteLargo = ''  
peinar = ''  
corte = input('Como te quieres cortar el pelo hoy Largo o Corto ? ').lower()


if corte == "largo":
    print('Me Parece Buena Idea Largo !')
    corteLargo = input('Lo quieres por debajo del hombro ? ').lower()   
    if corteLargo == 'si':
        print(' Te va a quedar Genial')
    else:
        print('Corte corto sera pues !! ')
else :
    print('Te va a hacer ver muy redonda la cara de marrana que tienes tia')
    peinar = input('Te vas a peinar tambien ? ').lower()   
    if peinar == 'si':
        print(peinar, ('Vale '),(input('y Como te vas a peinar?')).lower())
            
        if peinado == 'liso':
            print(' Vale genial liso')      
        elif peinado == 'ondas':
            print(' Me gustan las ondas')
        else:
            print('entonces sin peinado')
    else:
        print(input('Vale entonces secar solamente'))
    
if corteLargo == 'no':
    print(input('Te corto con maquina ?'))    
elif corte == 'ovalado':
        print('Ovalado es mas caro pero tu veras !! ')
        peinado = (input('y Como te vas a peinar?')).lower()
           
        if peinado == 'liso':
             print(' Vale liso te queda genial')      
        elif peinado == 'ondas':
             print(' Me gustan las ondas')
        else:
            print('entonces sin peinado')
    
elif peinado == 'liso' and corte == 'lo quiero recto':
        print('Mejor en pico, no ? ')
elif corte == 'con flequillo ':
    print('va a parecer que llevas un tazon en la cabeza  !! ')
elif peinado == 'liso' and corte == 'largo':
    print('Ok, Liso y largo te quedara perfecto !! ')
else:
    print(' Corto te queda muy bien ')
    
    corteLargo = input('Lo quieres por debajo del hombro ? ').lower()   