def generic_input(mensaje: str, menor: bool, normalized: int | float | None = None) -> str | int | float: 
    """
    Permite crear un input generico que permite normalizar valores automaticamente.

    Args:
        mensaje (str): El mensaje que se va a mostrar en el input.
        menor(bool): 
        normalized (int, float or None): El tipo de normalización a aplicar al dato, si no pasa se devuelve un str por defecto.
    Returns: 
        result (str, int or float): El valor introducido por el usuario ya normalizado.
    """

    valid = False

    while not valid:
        try:
            user_input = input(mensaje).strip().lower()
            
            if user_input is None:
                print("ingrese un dato valido")

            if menor:
                if user_input <=0:
                    print("ingrese un numero positivo")
            
            
            if normalized is None:
                return user_input
            
            if normalized in [int, float]:
                return normalized(user_input)
            
            return normalized(user_input)

        except ValueError: 
            print("entrada no valida, ingresa un valor correcto")
