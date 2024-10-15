import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Variables globales para el juego
numero_a_adivinar = 0
juego_en_progreso = False

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repite el Mensaje múltiples veces."""
    for i in range(times):
        await ctx.send(content)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Elige entre varias opciones."""
    await ctx.send(random.choice(choices))

# Aquí está el juego de adivinanza
@bot.command()
async def start_game(ctx):
    """Inicia el juego de adivinar el número."""
    global numero_a_adivinar, juego_en_progreso
    if juego_en_progreso:
        await ctx.send("¡Ya hay un juego en progreso!")
    else:
        numero_a_adivinar = random.randint(1, 100)
        juego_en_progreso = True
        await ctx.send("¡El juego ha comenzado! Estoy pensando en un número entre 1 y 100. Adivina cuál es.")

@bot.command()
async def guess(ctx, numero: int):
    """Adivina el número en el juego."""
    global numero_a_adivinar, juego_en_progreso
    if not juego_en_progreso:
        await ctx.send("¡No hay ningún juego en progreso! Usa `!start_game` para iniciar uno.")
    else:
        if numero < numero_a_adivinar:
            await ctx.send("El número es mayor.")
        elif numero > numero_a_adivinar:
            await ctx.send("El número es menor.")
        else:
            await ctx.send(f"¡Felicidades {ctx.author.name}! Has adivinado el número {numero_a_adivinar}.")
            juego_en_progreso = False

# Ejecuta el bot con tu token
bot.run("EL TOKEN SECRETO VA AQUÍ")

