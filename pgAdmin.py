host = "127.0.0.1"
user = "postgres"
password = "Solo2005"
db_name = "programmer_bot"

import psycopg2
import time

from parse import start_request


class PgAdmin:

    def minimum_code(self, id_discord):
        try:
            # connect to exist database

            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT id_discord FROM settings WHERE id_discord = '{id_discord}';"""
                )

                if cursor.fetchone() is None:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f"""INSERT INTO settings (id_discord) VALUES
                            ('{id_discord}');"""
                        )

            print("[INFO] Data was succefully inserted")

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")

    def insert_id_group_main(self, id_discord, id_group):
        try:
            # connect to exist database

            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT id_discord FROM settings WHERE id_discord = '{id_discord}';"""
                )

                if cursor.fetchone() is None:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f"UPDATE settings SET id_group_main = '{id_group}' where id_discord = '{id_discord}'")

            print("[INFO] Data was succefully update")

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")

    def insert_id_group_news(self, id_discord, id_group):
        id_discord = str(id_discord)
        id_group = str(id_group)
        try:

            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT id_discord FROM settings WHERE id_discord = '{id_discord}';"""
                )

                if cursor.fetchone() is not None:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f"UPDATE settings SET id_group_news = '{id_group}' where id_discord = '{id_discord}'")

            print("[INFO] Data was succefully update")


        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")

    def get_id_group_news(self,id_discord):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT id_group_news FROM settings WHERE id_discord = '{id_discord}';"""
                )

                result = cursor.fetchall()
            return result

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")



    def news(self):
        data = start_request()
        try:
            # connect to exist database

            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM news WHERE idd='1'")
            for data_one in data:
                with connection.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO news (id, title_text, title_a, img_a, description_text, 
                    idd) VALUES ('{data.index(data_one)}','{data_one[0]}','{data_one[1]}','{data_one[2]}','{data_one[3]}','1');""")

            print("[INFO] Data was succefully")




        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)

        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")


print(str(PgAdmin().get_id_group_news(974615605237936168)[0][0]))
