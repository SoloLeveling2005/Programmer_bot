# Задачи
# Удаление x количества сообщений
# Рассылка

# Импортируем библиотеки
import os
import threading
from threading import Thread
import datetime
import time
import asyncio

import psycopg2

import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.ext.commands import bot

# Свои импорты
from help import get_chanel_id, get_discord_id
from pgAdmin import PgAdmin
from parse import start_request
from get_time import start_time

# Орк вопросы
token = "OTg3MDA5NzMwODQ3MzA5ODM1.GOiTmO.I7NjBGz1dwPSgLTOCh_rPYXN6bvogAoqdOhfJU"
client = commands.Bot(command_prefix=".")
client.remove_command("help")


# Функционал
def send_message(id_group, text_message):
    async def send_msg(channel, text):
        channel = client.get_channel(channel)
        await channel.send(text)

    while True:
        @client.event
        async def on_ready():
            asyncio.run_coroutine_threadsafe(send_msg(id_group, text_message), client.loop)
            await client.change_presence(status=discord.Status.online, activity=discord.Game(".help"))

        break


id_group = 974615690659110963
send_message(id_group, text_message=f"Привет. Меня зовут <@{987009730847309835}>. И я Бот.")
print('Bot connected')


# @client.event
# async def on_message(ctx):
#     text = ctx.content
#     if ctx.author.id == 813350277812846623:
#         await ctx.reply(text)


@client.command()
async def setting(ctx):
    await ctx.send(
        f'Привет. Давайте настроим рассылку. Команды:\n.setting_main - в какой канал отправлять основную информацию(Введите эту команду в котором хотите отображать контент) \n.setting_news - в какой канал отправлять новости IT(Введите эту команду в котором хотите отображать контент)')
    global discord_id
    discord_id = get_chanel_id(ctx)


    while True:
        now = start_time()
        if now == "12:17:40" or now == "12:17:50":
            print(discord_id)
            await clear(ctx, amount=10)
            datas = start_request()
            try:
                for data in datas:
                    @client.event
                    async def print_emb():
                        print(discord_id)
                        title = data[0]
                        url_title = "https://habr.com" + str(data[1])
                        url_image = data[2]
                        description = data[3]
                        emb = discord.Embed(title=title, color=discord.Color.green(),
                                            url=url_title)
                        # emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
                        emb.set_thumbnail(
                            url=url_image)
                        emb.add_field(name=data[0], value=description)
                        channel = client.get_channel(discord_id)
                        await channel.send(embed=emb)

                    await print_emb()
            except:
                continue
        else:
            print(now)

        time.sleep(1)



#
#     def start_loop(loop):
#         asyncio.set_event_loop(loop)
#
# loop.run_forever()
#
# new_loop = asyncio.new_event_loop()
# t = Thread(target=start_loop, args=(new_loop,))
# t.start()
#
# _thread = threading.Thread(target=asyncio.run, args=(start_timer(discord_id)))
# _thread.start()


@client.command()
async def setting_main(ctx):
    print(get_discord_id(ctx))
    print(get_chanel_id(ctx))

    PgAdmin().insert_id_group_main(get_discord_id(ctx), get_chanel_id(ctx))


@client.command()
async def setting_news(ctx):
    print(get_discord_id(ctx))
    print(get_chanel_id(ctx))

    PgAdmin().insert_id_group_news(get_discord_id(ctx), get_chanel_id(ctx))


@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command()
async def help(ctx):
    emb = discord.Embed(title="Навигация по командам")
    emb.add_field(name='.clear', value="Очистка чата(по умолчанию 2)")

    await ctx.send(embed=emb)


client.run(token)
