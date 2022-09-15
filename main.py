import random
import time


# Constantes de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Coleccion de preguntas


def data():
    lista = [
        # Pregunta 1
        [
            # 0
            ["¿Cómo son conocidos los de la Casa de Durin?"],
            # 1
            {'a': "Hobbits que no pertenecen a La Comarca",
             'b': "Enanos",
             'c': "Elfos del bosque",
             'd': "Grandes Águilas",
             'result': 'b'},
            ["La casa de Durin se refiere al clan de enanos que habitaban las Montañas Nubladas. La mayoría de los clanes enanos pueden rastrear a sus ancestros hasta la casa de Durin."]  # 2
        ],
        # Pregunta 2
        [
            ["¿Qué es el puente de Khazad-dûm?"],  # 0
            {'a': "El puente sobre el río Brandivino, que delimita La Comarca.",
             'b': "Las míticas puertas entre la Tierra Media y Valinor, la tierra de los dioses.",
             'c': "El nombre de la espada rota antes de ser forjada otra vez como la legendaria Andúril.",
             'd': "El puente dentro de las Grandes Puertas de Moria, donde Gandalf se enfrentó al Balrog.",
             'result': 'd'},  # 1
            ["La casa de Durin se refiere al clan de enanos que habitaban las Montañas Nubladas. La mayoría de los clanes enanos pueden rastrear a sus ancestros hasta la casa de Durin."]  # 2
        ],
        # Pregunta 3
        [
            ["¿Qué criaturas son los Ungoliant?"],  # 0
            {'a': "Gigantes de montaña",
             'b': "Uruk-hai",
             'c': "Arañas gigantes",
             'd': "Bestias aladas",
             'result': 'c'},  # 1
            ["Ungoliant era una antigua criatura con forma de araña gigante. Ungoliant era la mamá de Ella-Laraña, contra quien se enfrentaron Frodo y Samsagaz Gamyi."]  # 2
        ],
        # Pregunta 4
        [
            ["¿Cuál de estos no es el nombre de un lugar para hospedarte?"],  # 0
            {'a': "La Antigua Casa de Huéspedes",
             'b': "El Dragón Verde",
             'c': "El Póney Pisador",
             'd': "La Estrella Sureña",
             'result': 'd'},  # 1
            ["Estrella Sureña es una variedad de \"hierba de pipa\" cultivada en La Comarca."]  # 2
        ],
        # Pregunta 5
        [
            ["¿Quiénes participaron en la Batalla de Isengard?"],  # 0
            {'a': "Las fuerzas de Saruman contra los Rohirrim del rey Théoden",
             'b': "Las fuerzas de Saruman contra los Ents",
             'c': "Los Orcos de Dol Guldur contra los Galadhrim de Lothlórien",
             'd': "Las fuerzas del Señor Oscuro, Sauron, contra las fuerzas de Gondor",
             'result': 'b'},  # 1
            ["La Batalla de Isengard también es conocida como La Destrucción de Isengard, porque los Ents destrozaron todo."]  # 2
        ],
        # Pregunta 6
        [
            ["¿Cuál de estas armas no fue encontrada en la cueva del Troll?"],  # 0
            {'a': "Orcrist, la hendedora de trasgos",
             'b': "Glamdring, el Martillo de enemigos",
             'c': "Dardo",
             'd': "Angrist",
             'result': 'd'},  # 1
            ["Angrist era una antigua espada forjada por Telchar de Nogrod. Fue utilizada para sacar un Silmaril de la Corona de Hierro de Melkor."]  # 2
        ],
        # Pregunta 7
        [
            ["¿Quién era Eleanor Gardner?"],  # 0
            {'a': "La hija de Samsagaz Gamyi y Rosita Coto",
             'b': "La reina del Bosque Negro y madre de Legolas",
             'c': "Una de los nueve humanos que recibieron un Anillo de Poder",
             'd': "La esposa de Bardo el arquero, de Ciudad del Lago",
             'result': 'a'},  # 1
            ["Elanor fue uno de los doce hijos que tuvieron Samsagaz Gamyi y Rosa Coto."]  # 2
        ],
        # Pregunta 8
        [
            ["¿Qué deciden Aragorn, Imrahil, Gandalf, Éomer, Elladan y Elrohir en la Última Deliberación?"],  # 0
            {'a': "A quién enviar a destruir el Anillo de Poder",
             'b': "Quién lideraría el Concilio Blanco. Gandalf fue escogido, pero rechazó el puesto, entonces Saruman asumió en su lugar.",
             'c': "El número de soldados que enviarían a luchar contra Sauron en la Batalla del Morannon",
             'd': "Cómo castigarían a los Uruk-hai por su levantamiento",
             'result': 'c'},  # 1
            ["Después de la Última Deliberación, Aragorn lideró un ejército de 6000 soldados para distraer a las fuerzas de Sauron y permitir que Frodo destruyera el Anillo Único."]  # 2
        ],
        # Pregunta 9
        [
            ["¿Qué son las heridas morgul?"],  # 0
            {'a': "Los montículos de tierra corrompidos de los que nacen los Uruk-hai.",
             'b': "Las heridas infligidas por los Nazgûl.",
             'c': "Las torres de asedio usadas por los orcos durante el ataque a Minas Tirith.",
             'd': "El nombre que recibe un elfo que ha renunciado a su inmortalidad.",
             'result': 'b'},  # 1
            ["Las heridas morgul son heridas infligidas por las armas encantadas de los Nazgûl, como la herida que recibió Frodo que casi lo transforma en un espectro."]  # 2
        ],
        # Pregunta 10
        [
            ["¿Cómo le dicen los elfos a los hobbits?"],  # 0
            {'a': "Los mellon",
             'b': "Los periannath",
             'c': "Los onodrim",
             'd': "Los Urulóki",
             'result': 'b'},  # 1
            ["La palabra en Sindarin \"perian\" significa literalmente \"mediano\". \"Periannath\" es el plural."]  # 2
        ]
    ]
    return lista

# Funcion random me retorna una lista con numeros random agregados sin repetirse


def aleatorynumber(data):
    i, lista = 0, []
    while i < len(data):
        L = random.randint(0, len(data)-1)
        if L not in lista:
            lista.append(L)
            i += 1
    return lista

# Funcion trivia contiene toda la logica de la trivia


def trivia(data, nombre, aleatory):
    count, incorrectos, score = 0, 0, 0
    """ Creo un ciclo que recorra mi lista de numeros aleatorios sin repeticion"""
    for num in aleatory:
        for item in data[num]:  # Recorre los elementos que esten en data[i]
            if isinstance(item, dict):  # Si el elemento e es de tipo dict entonces ejecuta el bloque
                # recorre el diccionario en busca de las opciones - la key result
                for key in item:
                    if key != 'result':  # Si es diferente a result ejecuta el codigo
                        # Imprime la key y la pregunta item[key]
                        print(
                            f"{GREEN}{key}){RESET} {MAGENTA}{item[key]}{RESET}")
                    else:
                        # Evalua la respuesta
                        while True:
                            opcion = input(f"{YELLOW}>>> {RESET}").lower().strip()

                            if opcion == 'x':  # Opcion especial
                                while True:  # Valide el input
                                    inpt = input(
                                        CYAN+"Deseas ver las respuestas [Presiona (s/n)] "+RESET).lower().strip()
                                    if inpt:
                                        if inpt == 's':
                                            # number al rango de (0, len(data) retorna 10 - 9 )
                                            for number in range(len(data)):
                                                print(
                                                    f"{BLUE}{''.join(data[number][0])}{RESET}" + f" respuesta : {GREEN}{data[number][1]['result']}{RESET}")  # Imprime la key y la pregunta uso join para convertir la lista a str
                                            exit()
                                        elif inpt == 'n':
                                            exit()
                                        else:
                                            print(
                                                RED+"Valor ingresado incorrecto"+RESET)

                            elif opcion == 'exit' or opcion == 'salir':  # Opcion exit
                                exit()
                            # recorre la opcion ingresada este en las opciones establecidas en data
                            # Tambien se puede poner >> n in ['a', 'b', 'c', 'd']
                            elif opcion in list(item.keys())[:-1]:
                                # Se compara la opcion con el item[key]
                                if opcion == item[key]:
                                    count += 1
                                    score += 10
                                    print(GREEN+'Correcto'+RESET)
                                    time.sleep(1.0)
                                    break
                                else:
                                    incorrectos += 1
                                    score -= 10
                                    print(RED+"Incorrecto"+RESET)
                                    time.sleep(1.0)
                                    break
                            else:  # En el caso que no sea una opcion establecida en data ni en las opciones te pedira volver a ingresar ya que el bucle es while True y solo en las opciones tiene un break
                                print(
                                    RED+"Valor ingresado incorrecto vuelve ingresar un valor"+RESET)
            else:  # Imprime todo lo que no sea diccionario
                # join convierte una lista a str
                print(f'\n{YELLOW}{"".join(item)}{RESET}')
                time.sleep(1.0)
    # Imprime los resultado
    print(f"""

{RED}{'*' * 5} Resultados : de {RESET}{YELLOW}{nombre}{RESET}
\n{GREEN}correcto' :{RESET} {YELLOW}{count}{RESET}
{GREEN}incorrecto' :{RESET} {YELLOW}{incorrectos}{RESET}
{BLUE}{nombre} {RESET}{WHITE}tu puntuacion es :{RESET} {YELLOW}{score}{RESET}
""")
    # Condicional evalua si se desea volver a ejecutar la trivia
    #trivia(data, nombre, aleatory) if input(CYAN+"¿Deseas volver intentar la trivia? [s]  "+RESET)  == 's' else print(WHITE+"\nEspero que lo hayas pasado muy bien, hasta pronto."+RESET)

    while True:  # Valide el input
        inpt = input(
            CYAN+"¿Deseas volver intentar la trivia? [Presiona (s/n)] "+RESET).lower().strip()
        if inpt:
            if inpt == 's':
                trivia(data, nombre, aleatory)
            elif inpt == 'n':
                print(WHITE+"\nEspero que lo hayas pasado muy bien, hasta pronto."+RESET)
                exit()
            else:
                print(RED+"Valor ingresado incorrecto"+RESET)


# La funcion banners recorre banner.txt, lo uso como inicio a la trivia
def banners():
    banners = ['./resources/banner.txt']
    for i in banners:
        with open(i) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                print(MAGENTA+line+RESET)
            time.sleep(1.0)


if __name__ == '__main__':
    print(f"""
{BLUE}Bienvenido a la trivia del Señor de los anillos
¿Quieres realizar este reto?
La trivia consta de 10 preguntas
{RESET}""")
    while True:
        inpt = input(RED+"¿Quieres iniciar? [Presiona (s/n)] "+RESET).lower().strip()
        if inpt:
            if inpt == 's':
                while True:
                    nom = input(MAGENTA + "Ingresa tu usuario : " +
                                RESET).lower().capitalize().strip()
                    if nom :
                        banners()
                        trivia(data(), nom, aleatorynumber(data()))
            elif inpt == 'n':
                break
            else:
                print(RED+"Valor ingresado incorrecto"+RESET)
