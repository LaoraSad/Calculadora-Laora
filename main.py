#calcular formulas de 4 figuras 2D (area, perometro) y 4 figuras 3D(volumen) y un triangulo rectangulo(angulo)
#saber qué figuras voy a utilizar y qué formulas quiero que saque por cada figura
#necesito funciones para cada formula de las figuras(puedes usar los datos enseguida)
#uso while para mostras el menu y pedirle al usuario que figura desea conocer, el usuario debe colocar los valores (poner el tipo de numero) y yo los voy a poner en la formula que me pida
#cuando escoja la figura necesito que se muestre que formulas estan disponibles
#cuando escoja la formula y muestre el resultado preguntar si quiere escoger otra figura
#TENER EN CUENTA: el usuario debe poner los parametros para rellenar la formula, debe saber que va a colocar un numero
#usar try para que no me rompa nada o usar else


continuar = "si"

while continuar == "si":
    print("----CALCULADORA GEOMETRICA\n")

    print("----------opciones disponibles de figuras 2D------------\n")
    print(
        "circulo\n"
        "cuadrado\n"
        "trapecio\n"
        "rombo\n"
        "triangulo rectangulo\n"
    )

    print("-----------opciones disponibles de figuras 3D------------\n")
    print(
        "cubo\n"
        "esfera\n"
        "piramide\n"
        "cono\n"
    )

    opcion_valida = False
    while not opcion_valida:
        try:
            figura = int(input("-----Qué tipo de figuras deseas?\n1 (2D) o 2 (3D)-----: "))
            if figura == 1 or figura == 2:
                opcion_valida = True
            else:
                print("solo puedes escoger 1 o 2, intenta nuevamente")

        except ValueError:
            print("Debes ingresar un número valido.")
            

    # FIGURAS 2D-------------
    if figura == 1:
        figuras_2d_validas = ["circulo", "cuadrado", "trapecio", "rombo", "triangulo rectangulo"]

        print("figuras 2D disponibles:")
        print(
            "circulo\n"
            "cuadrado\n"
            "trapecio\n"
            "rombo\n"
            "triangulo rectangulo\n"
        )

        figura_2d = input("Escribe la figura que deseas: ").strip().lower()
        while figura_2d not in figuras_2d_validas:
            print("figura no valida. Revise la ortigrafia e intente nuevamente.")
            
            figura_2d = input("Escribe la figura que deseas: ").strip().lower()
        

        if figura_2d == "circulo": #CIRCULO--------

            print("\nFORMULAS DISPONIBLES")
            print("1. area")
            print("2. perimetro")
            print("3. diametro")

            formula = input("Escoge una formula: ")
            while formula not in ["1", "2", "3"]:
                print("Formula no válida.")
                formula = input("Escoge una formula: ")
                
            radio_valido = False
            while not radio_valido:
                try:
                    radio = float(input("Ingresa el radio del circulo: "))
                    if radio > 0:
                        radio_valido = True
                    else:
                        print("La medida debe ser un numero positivo")
                    
                except ValueError:
                    print("Debes ingresar un número.")
                

            pi = 3.1416

            if formula == "1":
                area = pi * radio ** 2
                print("El area del circulo es:", area)

            elif formula == "2":
                perimetro = 2 * pi * radio
                print("El perimetro del circulo es:", perimetro)

            elif formula == "3":
                diametro = 2 * radio
                print("El diametro es:", diametro)

        elif figura_2d == "cuadrado": #CUADRADO

            print("\nFORMULAS DISPONIBLES")
            print("1. area")
            print("2. perimetro")
            print("3. diagonal")

            formula = input("Escoge una formula: ")
            while formula not in ["1", "2", "3"]:
                print("Formula no válida.")
                formula = input("Escoge una formula: ")
            
            lado_valido = False
            while not lado_valido: 
                try:
                    lado = float(input("Ingresa el lado del cuadrado: "))
                    if lado > 0:
                        lado_valido = True
                    else:
                        print("La medida debe ser positiva")
                    
                except ValueError:
                    print("Debes ingresar un número.")
                

            if formula == "1":
                area = lado ** 2
                print("El area es:", area)

            elif formula == "2":
                perimetro = 4 * lado
                print("El perimetro es:", perimetro)

            elif formula == "3":
                diagonal = lado * 1.414
                print("La diagonal es:", diagonal)

        elif figura_2d == "trapecio": #TRAPECIO---------

            print("\nFORMULAS DISPONIBLES")
            print("1. area")
            print("2. perimetro")
            print("3. base media") # es el segmento de recta que une los puntos medios de los lados no paralelos

            formula = input("Escoge una formula: ")
            while formula not in ["1", "2", "3"]:
                print("Formula no válida.")
                formula = input("Escoge una formula: ")
            
            base_mayor_valida = False
            while not base_mayor_valida:
                try:
                    base_mayor = float(input("Ingresa la base mayor: "))
                    if  base_mayor > 0:
                        base_mayor_valida = True
                    else:
                        print("la medida debe ser un numero positivo")
                except ValueError:
                    print("Debes ingresar un numero valido. intente nuevamete.")
            
            base_menor_valida = False
            while not base_menor_valida:
                try:
                    base_menor = float(input("Ingresa la base menor: "))
                    if base_menor <= 0:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                    elif base_menor >= base_mayor:
                        print(f"La base menor debe ser menor que la base mayor ({base_mayor} cm). Intenta de nuevo.")
                    else:
                        base_menor_valida = True
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            altura_valida = False
            while not altura_valida:
                try:
                    altura = float(input("Ingresa la altura: "))
                    if altura > 0:
                        altura_valida = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")
 
            lado1_valido = False
            while not lado1_valido:
                try:
                    lado1 = float(input("Ingresa lado 1 (cm): "))
                    if lado1 > 0:
                        lado1_valido = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")
 
            lado2_valido = False
            while not lado2_valido:
                try:
                    lado2 = float(input("Ingresa lado 2 (cm): "))
                    if lado2 > 0:
                        lado2_valido = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            if formula == "1":
                area = ((base_mayor + base_menor) * altura) / 2
                print("El area es:", area)

            elif formula == "2":
                perimetro = base_mayor + base_menor + lado1 + lado2
                print("El perimetro es:", perimetro)

            elif formula == "3":
                base_media = (base_mayor + base_menor) / 2
                print("La base media es:", base_media)

        elif figura_2d == "rombo": #ROMBO---------

            print("\nFORMULAS DISPONIBLES")
            print("1. area")
            print("2. perimetro")
            print("3. altura")

            formula = input("Escoge una formula: ")
            while formula not in ["1", "2", "3"]:
                print("Formula no válida.")
                formula = input("Escoge una formula: ")

            diagonal_mayor_valida = False
            while not diagonal_mayor_valida:
                try:
                    diagonal_mayor = float(input("Ingresa la diagonal mayor(cm): "))
                    if diagonal_mayor > 0:
                        diagonal_mayor_valida = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            diagonal_menor_valida = False
            while not diagonal_menor_valida:
                try:
                    diagonal_menor = float(input("Ingresa la diagonal menor(cm): "))
                    if diagonal_menor <= 0:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                    elif diagonal_menor >= diagonal_mayor:
                        print(f"La diagonal menor debe ser menor que la diagonal mayor ({diagonal_mayor} cm). Intenta de nuevo.")
                    else:
                        diagonal_menor_valida = True
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            lado_valido = False
            while not lado_valido:
                try:
                    lado = float(input("Ingresa el lado(cm): "))
                    if lado > 0:
                        lado_valido = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            if formula == "1":
                area = (diagonal_mayor * diagonal_menor) / 2
                print("El area es:", area)

            elif formula == "2":
                perimetro = 4 * lado
                print("El perimetro es:", perimetro)

            elif formula == "3":
                area = (diagonal_mayor * diagonal_menor) / 2
                altura = area / lado
                print("La altura es:", altura)
        
        elif figura_2d == "triangulo rectangulo": #TRIANGULO

            print("\nFORMULAS DISPONIBLES")
            print("1. area")
            print("2. hipotenusa")
            print("3. perimetro")

            formula = input("Escoge una formula: ")
            while formula not in ["1", "2", "3"]:
                print("Formula no válida.")
                formula = input("Escoge una formula: ")
 
            cateto1_valido = False
            while not cateto1_valido:
                try:
                    cateto1 = float(input("Ingresa el primer cateto (cm): "))
                    if cateto1 > 0:
                        cateto1_valido = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")
 
            cateto2_valido = False
            while not cateto2_valido:
                try:
                    cateto2 = float(input("Ingresa el segundo cateto (cm): "))
                    if cateto2 > 0:
                        cateto2_valido = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            if formula == "1":
                area = (cateto1 * cateto2) / 2
                print("El area es:", area)

            elif formula == "2":
                hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
                print("La hipotenusa es:", hipotenusa)

            elif formula == "3":
                hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
                perimetro = cateto1 + cateto2 + hipotenusa
                print("El perimetro es:", perimetro)

    # FIGURAS 3D
    elif figura == 2:
        figuras_3d_validas = ["cubo", "esfera", "piramide", "cono"]

        print("figuras 3D disponibles:")
        print(
            "cubo\n"
            "esfera\n"
            "piramide\n"
            "cono\n"
        )

        figura_3d = input("Escribe la figura que deseas: ").strip().lower()

        figuras_3d_validas = ["cubo", "esfera", "piramide", "cono"]

        while figura_3d not in figuras_3d_validas:
            print("Figura no válida. Revisa la ortografía e intenta de nuevo.")
            figura_3d = input("Escribe la figura que deseas: ").strip().lower()

        if figura_3d == "cubo": #CUBO----------

            print("\nFORMULAS DISPONIBLES")
            print("1. volumen")
            print("2. area superficial")
            print("3. aristas")

            formula = input("Escoge una formula: ")
            while formula not in ["1", "2", "3"]:
                print("Formula no válida. Las opciones son: 1, 2, 3")
                formula = input("Escoge una formula: ")

            lado_valido = False
            while not lado_valido:
                try:
                    lado = float(input("Ingresa el lado del cubo (cm): "))
                    if lado > 0:
                        lado_valido = True
                    else:
                        print("La medida debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Debes ingresar un número válido. Intenta de nuevo.")

            if formula == "1":
                volumen = lado ** 3
                print("El volumen es:", volumen)

            elif formula == "2":
                area = 6 * lado ** 2
                print("El area superficial es:", area)

            elif formula == "3":
                aristas = 12 * lado
                print("La suma de aristas es:", aristas)

        elif figura_3d == "esfera": #ESFERA------

                print("\nFORMULAS DISPONIBLES")
                print("1. volumen")
                print("2. area superficial")
                print("3. circunferencia maxima")

                formula = input("Escoge una formula: ")
                while formula not in ["1", "2", "3"]:
                    print("Formula no válida.")
                    formula = input("Escoge una formula: ")
                
                radio_valido = False
                while not radio_valido:
                    try:
                        radio = float(input("Ingresa el radio de la esfera (cm): "))
                        if radio > 0:
                            radio_valido = True
                        else:
                            print("La medida debe ser un número positivo. Intenta de nuevo.")
                    except ValueError:
                        print("Debes ingresar un número válido. Intenta de nuevo.")

                pi = 3.1416

                if formula == "1":
                    volumen = (4/3) * pi * radio ** 3
                    print("El volumen es:", volumen)

                elif formula == "2":
                    area = 4 * pi * radio ** 2
                    print("El area superficial es:", area)

                elif formula == "3":
                    circunferencia = 2 * pi * radio
                    print("La circunferencia maxima es:", circunferencia)

        elif figura_3d == "cono": #CONO----

                print("\nFORMULAS DISPONIBLES")
                print("1. volumen")
                print("2. area lateral")
                print("3. generatriz") #línea recta que forma parte de una figura tridimensional

                formula = input("Escoge una formula: ")
                while formula not in ["1", "2", "3"]:
                    print("Formula no válida.")
                    formula = input("Escoge una formula: ")

                radio_valido = False
                while not radio_valido:
                    try:
                        radio = float(input("Ingresa el radio (cm): "))
                        if radio > 0:
                            radio_valido = True
                        else:
                            print("La medida debe ser un número positivo. Intenta de nuevo.")
                    except ValueError:
                        print("Debes ingresar un número válido. Intenta de nuevo.")
 
                altura_valida = False
                while not altura_valida:
                    try:
                        altura = float(input("Ingresa la altura: "))
                        if altura > 0:
                            altura_valida = True
                        else:
                            print("La medida debe ser un número positivo. Intenta de nuevo.")
                    except ValueError:
                        print("Debes ingresar un número válido. Intenta de nuevo.")

                pi = 3.1416
                generatriz = (radio**2 + altura**2) ** 0.5

                if formula == "1":
                    volumen = (pi * radio**2 * altura) / 3
                    print("El volumen es:", volumen)

                elif formula == "2":
                    area_lateral = pi * radio * generatriz
                    print("El area lateral es:", area_lateral)

                elif formula == "3":
                    generatriz = (radio**2 + altura**2) ** 0.5
                    print("La generatriz es:", generatriz)
            
        elif figura_3d == "piramide": #PIRAMIDE-----------

                print("\nFORMULAS DISPONIBLES")
                print("1. volumen")
                print("2. area de la base")
                print("3. area total aproximada")

                formula = input("Escoge una formula: ")
                while formula not in ["1", "2", "3"]:
                    print("Formula no válida.")
                    formula = input("Escoge una formula: ")

                lado_valido = False
                while not lado_valido:
                    try:
                        lado = float(input("Ingresa el lado de la base (cm): "))
                        if lado > 0:
                            lado_valido = True
                        else:
                            print("La medida debe ser un número positivo. Intenta de nuevo.")
                    except ValueError:
                        print("Debes ingresar un número válido. Intenta de nuevo.")
 
                altura_valida = False
                while not altura_valida:
                    try:
                        altura = float(input("Ingresa la altura (cm): "))
                        if altura > 0:
                            altura_valida = True
                        else:
                            print("La medida debe ser un número positivo. Intenta de nuevo.")
                    except ValueError:
                        print("Debes ingresar un número válido. Intenta de nuevo.")

                if formula == "1":
                    volumen = (lado ** 2 * altura) / 3
                    print("El volumen es:", volumen)

                elif formula == "2":
                    area_base = lado ** 2
                    print("El area de la base es:", area_base)

                elif formula == "3":
                    area_base = lado ** 2
                    area_lateral = 2 * lado * ((lado/2)**2 + altura**2) ** 0.5
                    area_total = area_base + area_lateral
                    print("El area total aproximada es:", area_total)
            

    continuar = input("\n¿Quieres calcular otra figura? (si/no): ").strip().lower()
    while continuar != "si" and continuar != "no":
        print("Responde 'si' o 'no'.")
        continuar = input("¿Quieres calcular otra figura? (si/no): ").strip().lower()
 
print("¡Hasta luego!")