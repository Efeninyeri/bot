import discord
import random

import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot olarak giriş yaptık: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('!bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('!en büyük kim'):
        await message.channel.send("FERRARİ")

    if message.content.startswith("şifre"):
        def gen_pass(length=12):
            """Rastgele bir şifre üretir."""
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        generated_password = gen_pass()
        await message.channel.send(f"Oluşturulan şifre: {generated_password}")

# Çevre değişkeninden tokeni al

client.run("token")
