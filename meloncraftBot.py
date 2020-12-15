import discord
from discord.ext import commands

from catalogue import Catalogue
from store import Store

PATH_TO_DATA_FILE = "store_saves.csv"

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['store', 's', 'S', 'list_stores', 'list_s', 'shops'])
async def stores(ctx):
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    embed = discord.Embed(title="MelonCraft Shops", color=0xff0000)
    for shop in catalogue.list_stores():
        embed.add_field(name=shop.name, value=f'{shop.description} ({shop.location_x},{shop.location_y})',
                        inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['add_s', 's+', 'add_shop', 'addshop', 'addstore'])
async def add_store(ctx, *, details):
    shop_details = details.split(':')
    shop_name = shop_details[0].strip()
    shop_location_x = shop_details[1].strip()
    shop_location_y = shop_details[2].strip()
    shop_description = shop_details[3].strip()
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    catalogue.add_store(Store(shop_name, shop_location_x, shop_location_y, shop_description))
    catalogue.save_stores(PATH_TO_DATA_FILE)
    await stores(ctx)


@client.command(aliases=["list", "List", "Inv", "inv", "list_inv", "List_Inv"])
async def list_inventory(ctx, *, store_name):
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    for store in catalogue.list_stores():
        if store.name.lower() == store_name.lower():
            embed = discord.Embed(title=f'{store.name}', color=0xff0000)
            if store.inventory.__len__() == 0:
                embed.add_field(name="Currently has no Stock!", value="Please check back later.", inline=False)
            for item in store.inventory.list_items():
                embed.add_field(name=item.name, value=f'{item.quantity} / {item.cost}D', inline=False)
            await ctx.send(embed=embed)


@client.command(aliases=['s-', 'removestore', 'remove_shop', 'removeshop'])
async def remove_store(ctx, *, store_name):
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    for store in catalogue.list_stores():
        if store.name.lower() == store_name.strip().lower():
            catalogue.remove_store(store.name)
            catalogue.save_stores(PATH_TO_DATA_FILE)
    await stores(ctx)


client.run('TOKEN GOES HERE')
