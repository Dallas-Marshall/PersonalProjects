import discord
from discord.ext import commands

from Item import Item
from catalogue import Catalogue
from store import Store

PATH_TO_DATA_FILE = "store_saves.csv"

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='.', intents=intents)

# Remove default help command
client.remove_command("help")


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(name='list_stores', aliases=['stores', 'list_shops', 'shops', 'Stores', 'Shops'])
async def stores(ctx):
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    embed = discord.Embed(title="MelonCraft Shops", color=13424046)
    for shop in catalogue.list_stores():
        embed.add_field(name=shop.name, value=f'{shop.description} ({shop.location_x},{shop.location_y})',
                        inline=False)
    await ctx.send(embed=embed)


@client.command(name='add_store', aliases=['addstore', 'add_shop', 'addshop', 'add_s'])
async def add_store(ctx, *, details):
    shop_details = details.split(':')
    if len(shop_details) != 4:
        await ctx.send("Error: Incorrect Formatting")
        await help(ctx, 'add_store')
    else:
        shop_name = shop_details[0].strip()
        shop_location_x = shop_details[1].strip()
        shop_location_y = shop_details[2].strip()
        shop_description = shop_details[3].strip()
        catalogue = Catalogue()
        catalogue.load_stores(PATH_TO_DATA_FILE)
        catalogue.add_store(Store(shop_name, shop_location_x, shop_location_y, shop_description))
        catalogue.save_stores(PATH_TO_DATA_FILE)
        await stores(ctx)


@client.command(name='list_inventory', aliases=["list", "List", "Inv", "inv", "list_inv", "List_Inv", 'stock', 'Stock'])
async def list_inventory(ctx, *, store_name):
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    for store in catalogue.list_stores():
        if store.name.lower() == store_name.lower():
            embed = discord.Embed(title=f'{store.name}', color=13424046)
            if store.inventory.__len__() == 0:
                embed.add_field(name="Currently has no Stock!", value="Please check back later.", inline=False)
            for item in store.inventory.list_items():
                embed.add_field(name=item.name, value=f'{item.quantity} / {item.cost}D', inline=False)
            await ctx.send(embed=embed)


@client.command(name='remove_store', aliases=['removestore', 'remove_shop', 'removeshop', 'remove_s'])
async def remove_store(ctx, *, store_name):
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)
    # Attempt to remove store from catalogue.
    is_removed = catalogue.remove_store(store_name)
    if not is_removed:
        embed = discord.Embed(title=f'Store: \'{store_name}\' cannot be found', color=13424046)
        await ctx.send(embed=embed)
    else:
        # Update save file
        catalogue.save_stores(PATH_TO_DATA_FILE)
        embed = discord.Embed(title='Store Removed Successfully', color=13424046)
        await ctx.send(embed=embed)
    await stores(ctx)


@client.command(name='sell', aliases=['add_item', 'additem', 'Sell'])
async def add_item(ctx, *, details):
    item_details = details.split(':')
    embed = discord.Embed()
    if len(item_details) == 4:  # Correct number of arguments given
        store_name = item_details[0].strip()
        item_name = item_details[1].strip()
        item_quantity = item_details[2].strip()
        item_cost = item_details[3].strip()

        catalogue = Catalogue()
        catalogue.load_stores(PATH_TO_DATA_FILE)
        is_valid_store_name = False
        for store in catalogue.list_stores():
            if store.name.lower() == store_name.lower():
                is_valid_store_name = True

                # Add new Item to store inventory
                new_item = Item(item_name, item_quantity, int(item_cost))
                store.inventory.add_item(new_item)

                # Update save file
                catalogue.save_stores(PATH_TO_DATA_FILE)
                embed = discord.Embed(title='Item Added Successfully', color=13424046)
                embed.add_field(name=f'{item_name}', value=f'{item_quantity} / {item_cost}D')

        if not is_valid_store_name:
            embed = discord.Embed(title=f'Store: \'{store_name}\' cannot be found', color=13424046)
    else:
        embed = discord.Embed(title="Error: Please use the following format", color=13424046)
        embed.add_field(name=".sell <Store_Name> : <Item_Name> : <Quantity> : <Cost_in_Diamonds>",
                        value="e.g. .sell All Australian Wool : Red Wool : 2 Stacks : 1", inline=False)
        embed.add_field(name="Red Wool", value="2 Stacks / 1D")
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def help(ctx, *args):
    embed = discord.Embed(title="Meloncraft Commands List:", color=13424046)
    if len(args) == 0:  # Command not specified
        embed.add_field(name=".stores", value="Returns list of all stores.", inline=False)
        embed.add_field(name=".add_store", value="Adds Store to list of stores.", inline=False)
        embed.add_field(name=".remove_store", value="Removes Store from list of stores.", inline=False)
        embed.add_field(name=".list_inventory", value="Returns list of items for sale at Store.", inline=False)
        embed.add_field(name=".sell", value="Adds an Item to list of items for sale at Store.", inline=False)
        embed.add_field(name=".remove_item", value="Removes an Item to list of items for sale at Store.", inline=False)
        embed.add_field(name=".update_item", value="Updates an existing Item in Stores inventory.", inline=False)
        embed.add_field(name="For detailed command specific help:", value="Use .help <command_name> e.g. .help stores",
                        inline=False)
    elif len(args) == 1:  # Command specified
        embed = discord.Embed(title="Meloncraft Commands Help:", color=13424046)
        requested_command_name = args[0]
        if requested_command_name == "stores":
            embed.add_field(name=".stores", value="Returns list of all stores.", inline=False)
        elif requested_command_name == "add_store":
            embed.add_field(name=".add_store <Store_Name> : <x-Coord> : <y-Coord> : <Description>",
                            value="e.g. .add_store All Australian Wool : 300 : 400 : All your wool Needs!",
                            inline=False)
        elif requested_command_name == "remove_store":
            embed.add_field(name=".remove_store <Store_Name>",
                            value="e.g. .remove_store All Australian Wool", inline=False)
        elif requested_command_name == "list_inventory":
            embed.add_field(name=".list_inventory <Store_Name>",
                            value="e.g. .list_inventory All Australian Wool", inline=False)
        elif requested_command_name == "add_item":
            embed.add_field(name=".sell <Store_Name> : <Item_Name> : <Quantity> : <Cost_in_Diamonds>",
                            value="e.g. .add_item All Australian Wool : Red Wool : 2 Stacks : 1", inline=False)
        elif requested_command_name == "remove_item":
            embed.add_field(name=".remove_item <Store_Name> : <Item_Name>",
                            value="\te.g. .remove_item All Australian Wool : Red Wool", inline=False)
        elif requested_command_name == "update_item":
            embed.add_field(
                name=".update_item <Store_Name> : <Old_Item_Name> : <New_Item_Name> : <New_Item_Quantity> : "
                     "<New_Item_Cost>",
                value="\t.update_item All Australian Wool : Red Wool : Blue Wool : 2 Stacks : 1", inline=False)
        else:  # Unknown command
            embed = discord.Embed(title="Error", color=13424046)
            embed.add_field(name=f'Command \'{requested_command_name}\', could not be found.',
                            value="Use .help for a list of commands.", inline=False)
    elif len(args) > 1:  # Too many inputs
        embed = discord.Embed(title="Error: Please use the following format", color=13424046)
        embed.add_field(name=".help <command>", value="e.g. .help list_inventory", inline=False)
    await ctx.send(embed=embed)


@client.command(name='remove_item', aliases=['delete_item', 'removeitem', 'deleteitem'])
async def remove_item(ctx, *, details):
    item_details = details.split(':')
    embed = discord.Embed()
    if len(item_details) == 2:  # Correct number of arguments given
        store_name = item_details[0].strip()
        item_name = item_details[1].strip()

        catalogue = Catalogue()
        catalogue.load_stores(PATH_TO_DATA_FILE)
        is_valid_store_name = False
        for store in catalogue.list_stores():
            if store.name.lower() == store_name.lower():
                is_valid_store_name = True
                # Attempt to remove Item from store inventory
                is_removed = store.inventory.remove_item(item_name)
                if not is_removed:
                    embed = discord.Embed(title=f'Item: \'{item_name}\' cannot be found', color=13424046)
                else:
                    # Update save file
                    catalogue.save_stores(PATH_TO_DATA_FILE)
                    embed = discord.Embed(title='Item Removed Successfully', color=13424046)

        if not is_valid_store_name:
            embed = discord.Embed(title=f'Store Name: \'{store_name}\' cannot be found', color=13424046)
    else:
        embed = discord.Embed(title="Error: Please use the following format", color=13424046)
        embed.add_field(name=".remove_item <Store_Name> : <Item_Name>",
                        value="\te.g. .remove_item All Australian Wool : Red Wool", inline=False)
    await ctx.send(embed=embed)


@client.command(name='update_item', aliases=['edit_item', 'edititem', 'updateitem'])
async def update_item(ctx, *, details):
    item_details = details.split(':')
    embed = discord.Embed()
    if len(item_details) == 5:  # Correct number of arguments provided
        store_name = item_details[0].strip()
        old_item_name = item_details[1].strip()
        new_item_name = item_details[2].strip()
        new_item_quantity = item_details[3].strip()
        new_item_cost = int(item_details[4].strip())

        catalogue = Catalogue()
        catalogue.load_stores(PATH_TO_DATA_FILE)
        is_valid_store_name = False
        for store in catalogue.list_stores():
            if store.name.lower() == store_name.lower():
                is_valid_store_name = True
                # Attempt to remove old Item from inventory
                is_removed = store.inventory.remove_item(old_item_name)
                if not is_removed:
                    embed = discord.Embed(title=f'Item: \'{old_item_name}\' cannot be found', color=13424046)
                else:
                    # Add updated Item
                    updated_item = Item(new_item_name, new_item_quantity, new_item_cost)
                    store.inventory.add_item(updated_item)

                    # Update save file
                    catalogue.save_stores(PATH_TO_DATA_FILE)
                    embed = discord.Embed(title='Item Updated Successfully', color=13424046)
                    embed.add_field(name=f'{new_item_name}', value=f'{new_item_quantity} / {new_item_cost}D')

        if not is_valid_store_name:
            embed = discord.Embed(title=f'Store: \'{store_name}\' cannot be found', color=13424046)
    else:
        embed = discord.Embed(title="Error: Please use the following format", color=13424046)
        embed.add_field(name=".update_item <Store_Name> : <Old_Item_Name> : <New_Item_Name> : <New_Item_Quantity> : "
                             "<New_Item_Cost>",
                        value="\t.update_item All Australian Wool : Red Wool : Blue Wool : 2 Stacks : 1", inline=False)
        embed.add_field(name="Blue Wool", value="2 Stacks / 1D")
    await ctx.send(embed=embed)


@client.command(name='find', aliases=['find_item', 'locate', 'finditem', 'locateitem', 'locate_item'])
async def find_item(ctx, *, item_name):
    number_of_instances_found = 0
    catalogue = Catalogue()
    catalogue.load_stores(PATH_TO_DATA_FILE)

    embed = discord.Embed(title=f'\'{item_name}\' was found in stock at:', color=13424046)
    for store in catalogue.list_stores():
        for item in store.inventory.list_items():
            if item_name.lower() == item.name.lower():  # Matching item
                number_of_instances_found += 1
                embed.add_field(name=store.name, value=f'{item.name} - {item.quantity} / {item.cost}D', inline=False)

    if number_of_instances_found == 0:  # No matching items found
        embed = discord.Embed(title=f'\'{item_name}\' was not found in stock anywhere!', color=13424046)
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Incorrect Command Usage", color=13424046)
        embed.add_field(name="For Command Specific Help Use", value=".help <command> e.g. .help list_inventory",
                        inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Error: Invalid Command")
        await help(ctx)
    else:
        raise error


client.run('TOKEN GOES HERE')