from persistence.db import get_connection


class Pelicula:

    def __init__(self, id=None, titulo=None, duracion_minutos=None, clasificacion=None, genero=None):
        # id será el id_pelicula de la tabla
        self.id = id
        self.titulo = titulo
        self.duracion_minutos = duracion_minutos
        self.clasificacion = clasificacion
        self.genero = genero

    # CREATE
    def save(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO peliculas (titulo, duracion_minutos, clasificacion, genero)
                VALUES (%s, %s, %s, %s)
            """
            valores = (self.titulo, self.duracion_minutos,
                       self.clasificacion, self.genero)

            cursor.execute(query, valores)
            connection.commit()

            self.id = cursor.lastrowid
            return self.id

        except Exception as ex:
            print("Error al guardar película:", ex)
            return 0
        finally:
            cursor.close()
            connection.close()

    # READ (todas)
    @staticmethod
    def get_all():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                SELECT id_pelicula, titulo, duracion_minutos, clasificacion, genero
                FROM peliculas
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            peliculas = []
            for row in rows:
                pelicula = Pelicula(
                    id=row[0],
                    titulo=row[1],
                    duracion_minutos=row[2],
                    clasificacion=row[3],
                    genero=row[4]
                )
                peliculas.append(pelicula)

            return peliculas

        except Exception as ex:
            print("Error al obtener películas:", ex)
            return []
        finally:
            cursor.close()
            connection.close()

    # UPDATE completo
    def update(self):
        if self.id is None:
            print("No se puede actualizar: la película no tiene id.")
            return False

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                UPDATE peliculas
                SET titulo = %s,
                    duracion_minutos = %s,
                    clasificacion = %s,
                    genero = %s
                WHERE id_pelicula = %s
            """
            valores = (self.titulo, self.duracion_minutos,
                       self.clasificacion, self.genero, self.id)

            cursor.execute(query, valores)
            connection.commit()

            print("ROWCOUNT update():", cursor.rowcount)
            return cursor.rowcount > 0

        except Exception as ex:
            print("Error al actualizar película:", ex)
            return False
        finally:
            cursor.close()
            connection.close()

    # 🔵 UPDATE de un solo campo (igual que Cliente)
    def update_field(self, campo, valor):
        """
        Actualiza un solo campo de la película (titulo, duracion_minutos, clasificacion o genero)
        usando self.id (que corresponde a id_pelicula).
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            campos_permitidos = [
                "titulo", "duracion_minutos", "clasificacion", "genero"
            ]
            if campo not in campos_permitidos:
                print("Campo no permitido:", campo)
                return False

            query = f"UPDATE peliculas SET {campo} = %s WHERE id_pelicula = %s"
            valores = (valor, self.id)

            print("DEBUG SQL Pelicula:", query, "VALORES:", valores)

            cursor.execute(query, valores)
            connection.commit()

            print("ROWCOUNT update_field() Pelicula:", cursor.rowcount)
            return cursor.rowcount > 0

        except Exception as ex:
            print("Error en update_field (Pelicula):", ex)
            return False
        finally:
            cursor.close()
            connection.close()

    # DELETE
    def delete(self):
        if self.id is None:
            print("No se puede eliminar: la película no tiene id.")
            return False

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "DELETE FROM peliculas WHERE id_pelicula = %s"
            cursor.execute(query, (self.id,))
            connection.commit()

            print("ROWCOUNT delete() Pelicula:", cursor.rowcount)
            return cursor.rowcount > 0

        except Exception as ex:
            print("Error al eliminar película:", ex)
            return False
        finally:
            cursor.close()
            connection.close()

