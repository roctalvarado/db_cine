from persistence.db import get_connection


class Cliente:

    def __init__(self, id=None, nombre=None, telefono=None, email=None, fecha_registro=None):
        # id será el id_cliente de la tabla
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.fecha_registro = fecha_registro

    # CREATE
    def save(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO clientes (nombre, telefono, email, fecha_registro)
                VALUES (%s, %s, %s, %s)
            """
            valores = (self.nombre, self.telefono,
                       self.email, self.fecha_registro)

            cursor.execute(query, valores)
            connection.commit()

            # id_cliente generado
            self.id = cursor.lastrowid
            return self.id

        except Exception as ex:
            print("Error al guardar cliente:", ex)
            return 0
        finally:
            cursor.close()
            connection.close()

    # READ (todos)
    @staticmethod
    def get_all():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                SELECT id_cliente, nombre, telefono, email, fecha_registro
                FROM clientes
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            clientes = []
            for row in rows:
                cliente = Cliente(
                    id=row[0],
                    nombre=row[1],
                    telefono=row[2],
                    email=row[3],
                    fecha_registro=row[4]
                )
                clientes.append(cliente)

            return clientes

        except Exception as ex:
            print("Error al obtener clientes:", ex)
            return []
        finally:
            cursor.close()
            connection.close()

    # UPDATE completo (por si lo usas)
    def update(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                UPDATE clientes
                SET nombre = %s,
                    telefono = %s,
                    email = %s,
                    fecha_registro = %s
                WHERE id_cliente = %s
            """
            valores = (self.nombre, self.telefono, self.email,
                       self.fecha_registro, self.id)

            cursor.execute(query, valores)
            connection.commit()

            print("ROWCOUNT update():", cursor.rowcount)
            return cursor.rowcount > 0

        except Exception as ex:
            print("Error al actualizar cliente:", ex)
            return False
        finally:
            cursor.close()
            connection.close()

    # 🔵 UPDATE de un solo campo
    def update_field(self, campo, valor):
        """
        Actualiza un solo campo del cliente (nombre, telefono, email o fecha_registro)
        usando self.id (que corresponde a id_cliente).
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Seguridad básica para evitar inyección SQL
            campos_permitidos = [
                "nombre", "telefono", "email", "fecha_registro"]
            if campo not in campos_permitidos:
                print("Campo no permitido:", campo)
                return False

            query = f"UPDATE clientes SET {campo} = %s WHERE id_cliente = %s"
            valores = (valor, self.id)

            # Debug para que veas qué se ejecuta
            print("DEBUG SQL:", query, "VALORES:", valores)

            cursor.execute(query, valores)
            connection.commit()

            print("ROWCOUNT update_field():", cursor.rowcount)
            return cursor.rowcount > 0

        except Exception as ex:
            print("Error en update_field:", ex)
            return False
        finally:
            cursor.close()
            connection.close()

    # DELETE
    def delete(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(query, (self.id,))
            connection.commit()

            print("ROWCOUNT delete():", cursor.rowcount)
            return cursor.rowcount > 0

        except Exception as ex:
            print("Error al eliminar cliente:", ex)
            return False
        finally:
            cursor.close()
            connection.close()
