import discord
from discord.ext import commands

from Item import Item
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


@client.command()
async def add_item(ctx, *, details):
    item_details = details.split(':')
    embed = discord.Embed(title=f'Error in add_item', color=0xff0000)
    if len(item_details) == 4:
        store_name = item_details[0].strip()
        item_name = item_details[1].strip()
        item_quantity = item_details[2].strip()
        item_cost = item_details[3].strip()

        catalogue = Catalogue()
        catalogue.load_stores(PATH_TO_DATA_FILE)
        is_valid_name = False
        for store in catalogue.list_stores():
            if store.name.lower() == store_name.lower():
                is_valid_name = True
                # Add new Item to store inventory
                new_item = Item(item_name, item_quantity, int(item_cost))
                store.inventory.add_item(new_item)
                # Update save file
                catalogue.save_stores(PATH_TO_DATA_FILE)
                embed = discord.Embed(title='Item Added Successfully', color=0xff0000)
                embed.add_field(name=f'{item_name}', value=f'{item_quantity} / {item_cost}D')

            if not is_valid_name:
                embed = discord.Embed(title='Error in add_item', color=0xff0000)
                embed.add_field(name=f'{store_name}', value='cannot be found')
    else:
        embed = discord.Embed(title='Error in add_item', color=0xff0000)
        embed.add_field(name='Please use the following format',
                        value='!add_item store_name : item_name : item_quantity : item_cost\nFor example !add_item '
                              'Mobs Melons : Cooked Chicken : 2 Stacks : 1', inline=False)
        embed.add_field(name='Cooked Chicken', value='2 Stacks / 1D')
    await ctx.send(embed=embed)


client.run('TOKEN GOES HERE')
