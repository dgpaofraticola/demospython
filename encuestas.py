def show_menu():
    print("")
    print("1. Crear encuesta")
    print("2. Ver encuestas disponibles")
    print("3. Votar en una encuesta")
    print("4. Ver resultados de una encuesta")
    print("5. Salir")

def create_survey(surveys):
    title = input("Título de la encuesta: ")
    surveys[title] = {}
    while True:
        question = input("Ingrese la pregunta (o 'listo' para terminar): ")
        if question.lower() == 'listo':
            break
        surveys[title][question] = {}
        while True:
            option = input("Agregar opción (o 'listo' para terminar): ")
            if option.lower() == 'listo':
                break
            surveys[title][question][option] = 0

def show_surveys(surveys):
    if not surveys:
        print("No hay encuestas disponibles.")
    else:
        for i, title in enumerate(surveys):
            print(f"{i + 1}. {title}")

def select_survey(surveys):
    show_surveys(surveys)
    try:
        choice = int(input("Seleccione una encuesta: ")) - 1
        if 0 <= choice < len(surveys):
            return list(surveys.keys())[choice]
        else:
            print("Encuesta no válida.")
            return None
    except ValueError:
        print("Entrada no válida.")
        return None

def vote(surveys):
    title = select_survey(surveys)
    if title:
        for i, question in enumerate(surveys[title]):
            print(f"\n{i + 1}. {question}")
            for j, option in enumerate(surveys[title][question]):
                print(f"  {j + 1}. {option}")
            while True:
                try:
                    vote = int(input("Elija su opción: ")) - 1
                    if 0 <= vote < len(surveys[title][question]):
                        options = list(surveys[title][question].keys())
                        surveys[title][question][options[vote]] += 1
                        print("Voto registrado con éxito.")
                        break
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("Ingrese un número válido.")

def view_results(surveys):
    title = select_survey(surveys)
    if title:
        for question, options in surveys[title].items():
            print(f"\nPregunta: {question}")
            for option, votes in options.items():
                print(f"  Opción: {option}, Votos: {votes}")

def register_user(users):
    """Registra un nuevo usuario en el sistema."""
    while True:
        username = input("Nombre de usuario: ")
        if username in users:
            print("El nombre de usuario ya existe. Intente con otro.")
        else:
            while True:
                password = input("Contraseña: ")
                confirm_password = input("Confirme la contraseña: ")
                if password == confirm_password:
                    users[username] = password
                    print("Usuario registrado con éxito.")
                    return
                else:
                    print("Las contraseñas no coinciden. Intente de nuevo.")

def login(users):
    """Verifica las credenciales del usuario y permite el inicio de sesión."""
    while True:
        username = input("Nombre de usuario: ")
        if username in users:
            password = input("Contraseña: ")
            if users[username] == password:
                print("Inicio de sesión exitoso.")
                return username
            else:
                print("Contraseña incorrecta. Intente de nuevo.")
        else:
            print("Usuario no encontrado. Intente de nuevo o regístrese.")

def main_menu(surveys):
    actions = {
        "1": create_survey,
        "2": show_surveys,
        "3": vote,
        "4": view_results,
        "5": lambda x: print("Saliendo del programa.")
    }

    while True:
        show_menu()
        option = input("Seleccione una opción: ")
        action = actions.get(option)
        if action:
            if option == "5":
                action(None)
                break
            else:
                action(surveys)
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    users = {}
    surveys = {}
    authenticated_user = None

    while True:
        if authenticated_user:
            main_menu(surveys)
            break
        else:
            print("")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            option = input("Seleccione una opción: ")
            if option == "1":
                register_user(users)
            elif option == "2":
                authenticated_user = login(users)
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
