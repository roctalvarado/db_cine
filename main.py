from entities.cliente import Cliente
from entities.pelicula import Pelicula


def mostrar_script(sql):
    print("\n=== SCRIPT SQL CORRESPONDIENTE ===")
    print(sql)
    print("=================================\n")


def menu_clientes():
    while True:
        print("\n=== CRUD CLIENTES ===")
        print("1. Ver clientes")
        print("2. Crear cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Elige opción: ")

        if opcion == "1":
            clientes = Cliente.get_all()
            for c in clientes:
                print(
                    f"{c.id} | {c.nombre} | {c.telefono} | {c.email} | {c.fecha_registro}"
                )

            script_select = """
SELECT id_cliente, nombre, telefono, email, fecha_registro
FROM clientes;
"""
            mostrar_script(script_select)

        elif opcion == "2":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            fecha = input("Fecha registro (YYYY-MM-DD): ")

            c = Cliente(nombre=nombre, telefono=telefono,
                        email=email, fecha_registro=fecha)
            c.save()
            print("Cliente creado con ID:", c.id)

            script_insert = f"""
INSERT INTO clientes (nombre, telefono, email, fecha_registro)
VALUES ('{nombre}', '{telefono}', '{email}', '{fecha}');
"""
            mostrar_script(script_insert)

        elif opcion == "3":
            id_cliente = int(input("ID del cliente a actualizar: "))

            print("\n¿Qué campo deseas actualizar?")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. Email")
            print("4. Fecha de registro")
            campo_opcion = input("Elige opción: ")

            campos_sql = {
                "1": "nombre",
                "2": "telefono",
                "3": "email",
                "4": "fecha_registro"
            }

            if campo_opcion not in campos_sql:
                print("Opción inválida.")
                continue

            campo = campos_sql[campo_opcion]
            nuevo_valor = input(f"Nuevo valor para {campo}: ")

            c = Cliente(id=id_cliente)

            if c.update_field(campo, nuevo_valor):
                print("Cliente actualizado.")
            else:
                print("No se pudo actualizar.")

            script_update = f"""
UPDATE clientes
SET {campo} = '{nuevo_valor}'
WHERE id_cliente = {id_cliente};
"""
            mostrar_script(script_update)

        elif opcion == "4":
            id_cliente = int(input("ID del cliente a eliminar: "))
            c = Cliente(id=id_cliente)
            if c.delete():
                print("Cliente eliminado.")
            else:
                print("No se pudo eliminar.")

            script_delete = f"""
DELETE FROM clientes
WHERE id_cliente = {id_cliente};
"""
            mostrar_script(script_delete)

        elif opcion == "5":
            print("Saliendo de CRUD CLIENTES...")
            break
        else:
            print("Opción inválida")


def menu_peliculas():
    while True:
        print("\n=== CRUD PELÍCULAS ===")
        print("1. Ver películas")
        print("2. Crear película")
        print("3. Actualizar película")
        print("4. Eliminar película")
        print("5. Salir")
        opcion = input("Elige opción: ")

        if opcion == "1":
            peliculas = Pelicula.get_all()
            for p in peliculas:
                print(
                    f"{p.id} | {p.titulo} | {p.duracion_minutos} min | {p.clasificacion} | {p.genero}"
                )

            script_select = """
SELECT id_pelicula, titulo, duracion_minutos, clasificacion, genero
FROM peliculas;
"""
            mostrar_script(script_select)

        elif opcion == "2":
            titulo = input("Título: ")
            duracion = input("Duración (minutos): ")
            clasificacion = input("Clasificación (ej. B15, C, etc.): ")
            genero = input("Género: ")

            p = Pelicula(
                titulo=titulo,
                duracion_minutos=duracion,
                clasificacion=clasificacion,
                genero=genero
            )
            p.save()
            print("Película creada con ID:", p.id)

            script_insert = f"""
INSERT INTO peliculas (titulo, duracion_minutos, clasificacion, genero)
VALUES ('{titulo}', {duracion}, '{clasificacion}', '{genero}');
"""
            mostrar_script(script_insert)

        elif opcion == "3":
            id_pelicula = int(input("ID de la película a actualizar: "))

            print("\n¿Qué campo deseas actualizar?")
            print("1. Título")
            print("2. Duración (minutos)")
            print("3. Clasificación")
            print("4. Género")
            campo_opcion = input("Elige opción: ")

            campos_sql = {
                "1": "titulo",
                "2": "duracion_minutos",
                "3": "clasificacion",
                "4": "genero"
            }

            if campo_opcion not in campos_sql:
                print("Opción inválida.")
                continue

            campo = campos_sql[campo_opcion]
            nuevo_valor = input(f"Nuevo valor para {campo}: ")

            p = Pelicula(id=id_pelicula)

            if p.update_field(campo, nuevo_valor):
                print("Película actualizada.")
            else:
                print("No se pudo actualizar.")

            # ojo: duracion_minutos es numérico, pero tu script es solo ilustrativo
            script_update = f"""
UPDATE peliculas
SET {campo} = '{nuevo_valor}'
WHERE id_pelicula = {id_pelicula};
"""
            mostrar_script(script_update)

        elif opcion == "4":
            id_pelicula = int(input("ID de la película a eliminar: "))
            p = Pelicula(id=id_pelicula)
            if p.delete():
                print("Película eliminada.")
            else:
                print("No se pudo eliminar.")

            script_delete = f"""
DELETE FROM peliculas
WHERE id_pelicula = {id_pelicula};
"""
            mostrar_script(script_delete)

        elif opcion == "5":
            print("Saliendo de CRUD PELÍCULAS...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    # Si quieres elegir qué CRUD usar:
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. CRUD Clientes")
        print("2. CRUD Películas")
        print("3. Salir")
        op = input("Elige opción: ")

        if op == "1":
            menu_clientes()
        elif op == "2":
            menu_peliculas()
        elif op == "3":
            print("Adiós :)")
            break
        else:
            print("Opción inválida")
