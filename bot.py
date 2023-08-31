import discord
from discord.ext import commands
import dictionary

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
	print('Dictbot Ready')

@client.command()
async def ping(ctx):
	print('EVENT MONITOR: ping command called from guild = {}'.format(ctx.guild))
	await ctx.send('Ping: {}ms'.format(round(client.latency * 1000)))

@client.command()
async def help(ctx):
	print(print('EVENT MONITOR: help command called from guild = {}'.format(ctx.guild)))
	embed = discord.Embed(title = "DictBot", description='A dictionary database for discord.', color = discord.Colour.orange())
	embed.add_field(name=".ping", value="Checks bot ping.", inline=False)
	embed.add_field(name = ".define (word)", value = "Returns definition of a given word.", inline = False)
	embed.add_field(name = ".random", value = "Returns a random word and its definition.", inline = False)
	await ctx.send(embed=embed)

@client.command()
async def define(ctx, word):
	print('EVENT MONITOR: define command called from guild = "{}" for "{}"'.format(ctx.guild, word))
	embed = discord.Embed(title="Definition: {}".format(word), color = discord.Colour.blue())
	i = 1
	for definition in dictionary.get_definition(word):
		embed.add_field(name="Definition #{}:".format(i), value = definition)
		i += 1
	await ctx.send(embed=embed)

@client.command()
async def random(ctx):
	print('EVENT MONITOR: random command called from guild = "{}"'.format(ctx.guild))
	word, definition = dictionary.random_word()
	embed = discord.Embed(title="Definition: {}".format(word), color = discord.Colour.red())
	i = 1
	for definition in definition:
		embed.add_field(name="Definition #{}:".format(i), value = definition)
		i += 1
	await ctx.send(embed=embed)

client.run('token here')