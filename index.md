# Honeydew Discord Bot
Created by Dallas Marshall

> A utility bot used on Meloncraft Discord to display items for sale on mc.meloncraft.net as well as provide the ability to find an item to purchase.

### Commands
- `.stores`: Returns list of all stores.
- `.add_store`: Adds a store to the list of stores.
  - `.add_store <Store_Name> : <x_Coord> : <z_Coord> : <Description>`
- `.remove_store`: Removes a store from the list of stores.
  - `.remove_store <Store_Name>`
- `.stock`: Returns a list of items for sale at specified store.
  - `.stock <Store_Name>`
- `.sell`: Adds an item to list of items for sale at the specified Store.
  - `.sell <Store_Name> : <Item_Name> : <Quantity> : <Cost_in_Diamonds>`
- `.remove_item`: Removes an item to the list of items for sale at the specified store.
  - `.remove_item <Store_Name> : <Item_Name>`
- `.update_item`: Updates the details of an existing item in the specified store's inventory.
  - `.update_item <Store_Name> : <Old_Item_Name> : <New_Item_Name> : <New_Item_Quantity> : <New_Item_Cost>`
- `.find`: Returns list of stores (if any) with specified item in stock.
  - `.find <Item_Name>`
- `.update_store`: Updates the details of an existing store.
  - `.update_store <Old_Store_Name> : <New_Store_name> : <New_X_Coord> : <New_Z_Coord> : <New_Description>`
- `.bot_info`: Gives a brief description of the bot.
- `.help`: Provides list of commands.
- `.help <command_name>`: Provides detailed command specific help.
  - Please note using `.help <command_name>` will only work with default command names and not aliases.

### Command Aliases
> Commands have one or more aliases that can be used when making a command call. There is no benefit for using a command aliases over the names stated above, simply a matter of preference for different users and all aliases will perform equally.

#### .stores:
- `.list_stores`
- `.Stores`
#### .add_store:
- `.addstore`
- `.add_s`
#### .stock:
- `.list`
- `.List`
- `.Inv`
- `.inv`
- `.list_inv`
- `.List_Inv`
- `.list_inventory`
- `.Stock` 
#### .remove_store:
- `.removestore`
- `.remove_s`
#### .sell:
- `.add_item`
- `.additem`
- `.Sell`
#### .remove_item:
- `.delete_item`
- `.removeitem`
- `.deleteitem`
#### .update_item:
- `.edit_item`
- `.edititem`
- `.updateitem`
#### .find:
- `.find_item`
- `.locate`
- `.finditem`
- `.locateitem`
- `.locate_item`
#### .update_store:
- `.edit_store`
- `.editstore`
- `.updatestore`

### How To

> A List of step-by-step examples for completing a range of tasks. Note: For commands that can perform multiple changes, seperate examples are provided for each possible change however, these changed can be combined into the one command. (See .update_item and .update_store)

#### View stores:
- `.stores`

#### Add a new store:
> In this example we will add a new store with the following details:
> - Store Name: Squelon's Wood Stall
> - Store Coordinates: x: 50, z: -285
> - Store Description: Stockists of all overworld wood types
- `.add_store Squelon's Wood Stall : 50 : -285 : Stockists of all overworld wood types`

#### Remove a store:
> In this example we will remove the store 'Squelon's Wood Stall'
- `.remove_store Squelon's Wood Stall`

#### Update a store:
> In this example we will rename 'Squelon's Wood Stall' to 'Meloncraft Lumberjacks'
- `.update_store Squelon's Wood Stall : Meloncraft Lumberjacks : 50 : -285 : Stockists of all overworld wood types`

> In this example we will update the x coordinate of  Squelon's Wood Stall to '300'
- `.update_store Squelon's Wood Stall : Squelon's Wood Stall : 300 : -285 : Stockists of all overworld wood types`

> In this example we will update the z coordinate of  Squelon's Wood Stall to '22'
- `.update_store Squelon's Wood Stall : Squelon's Wood Stall : 50 : 22 : Stockists of all overworld wood types`

> In this example we will update the description of Squelon's Wood Stall to 'Man's Got WOOD!'
- `.update_store Squelon's Wood Stall : Squelon's Wood Stall : 50 : -285 : Man's Got WOOD!`

#### Add an item for sale:
> In this example we will add an item for sale with the following details:
> - Store Name: Squelon's Wood Stall
> - Item Name: Oak Logs
> - Item Quantity: 2 Stacks
> - Item Cost: 1 Diamond
- `.sell Squelon's Wood Stall : Oak Logs : 2 Stacks : 1` 
- Note: don't put D or Diamonds in cost

> In this example we will add an item for sale with the following details:
> - Store Name: Squelon's Wood Stall
> - Item Name: Diamond Axe
> - Item Quantity: 1
> - Item Cost: 5 Diamonds
- `.sell Squelon's Wood Stall : Diamond Axe : 1 : 1` 
- Note: don't put D or Diamonds in cost

#### Remove an item from a store:
> In this example we will remove 'Diamond Axe' from 'Squelon's Wood Stall'
- `.remove_item Squelon's Wood Stall : Diamond Axe`

#### Update an item at a store:
> In this example we will rename 'Oak Wood' at Squelon's Wood Stall to 'Birch Wood'
- `.update_item Squelon's Wood Stall : Oak Wood : Birch Wood : 2 Stacks : 1`

> In this example we will update the price of 'Oak Wood' at Squelon's Wood Stall to '3 Diamonds'
- `.update_item Squelon's Wood Stall : Oak Wood : Oak Wood : 2 Stacks : 3`

> In this example we will update the quantity of 'Oak Wood' at Squelon's Wood Stall to '3 Stacks'
- `.update_item Squelon's Wood Stall : Oak Wood : Oak Wood : 3 Stacks : 1`

#### Check a store's stock:
> In this example we will check the stock at Squelon's Wood Stall
- `.stock Squelon's Wood Stall`

#### Find an item:
> In this example we will search for 'Blast Potion' in the catalogue
- `.find Blast Potion`

#### Get command specific help in Discord:
> In this example we will get command specific help in Discord for the '.add_store' command
- `.help add_store`
