# await message.author.send("Text")


# Получение текста
# @client.event
# async def on_message(ctx):
#     text = ctx.content


def get_chanel_id(ctx):
    return ctx.channel.id

def get_discord_id(ctx):
    return ctx.message.guild.id




#
#
#
#
# import psycopg2
#
# try:
#     # connect to exist database
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name
#     )
#     connection.autocommit = True
#
#     # the cursor for perfoming database operations
#     # cursor = connection.cursor()
#
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT version();"
#         )
#
#         print(f"Server version: {cursor.fetchone()}")
#
#     # create a new table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """CREATE TABLE settings(
#                 id_discord text,
#                 id_group_main text,
#                 id_group_news text);"""
#         )
#
#         # connection.commit()
#         print("[INFO] Table created successfully")
#
#     # insert data into a table
#     # with connection.cursor() as cursor:
#     #     cursor.execute(
#     #         """INSERT INTO settings (setting_main, setting_news) VALUES
#     #         ('974615690659110963', '975715730593038386');"""
#     #     )
#     #
#     #     print("[INFO] Data was succefully inserted")
#
#     # get data from a table
#     # with connection.cursor() as cursor:
#     #     cursor.execute(
#     #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
#     #     )
#     #
#     #     print(cursor.fetchone())
#
#     # delete a table
#     # with connection.cursor() as cursor:
#     #     cursor.execute(
#     #         """DROP TABLE users;"""
#     #     )
#     #
#     #     print("[INFO] Table was deleted")
#
# except Exception as _ex:
#     print("[INFO] Error while working with PostgreSQL", _ex)
# finally:
#     if connection:
#         # cursor.close()
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")