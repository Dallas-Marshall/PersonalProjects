# Honeydew Discord Bot
Created by Dallas Marshall

> A utility bot used on Meloncraft Discord to display items for sale on mc.meloncraft.net as well as provide the ability to find an item to purchase.

### Commands
- `.stores`: Returns list of all stores.
- `.add_store`: Adds a store to the list of stores.
  - `.add_store <Store_Name> : <x_Coord> : <z_Coord> : <Description>`
  - e.g. `.add_store All Australian Wool : 300 : 400 : All your wool Needs!`
- `.remove_store`: Removes a store from the list of stores.
  - `.remove_store <Store_Name>`
  - e.g. `.remove_store All Australian Wool`
- `.stock`: Returns a list of items for sale at specified store.
  - `.stock <Store_Name>`
  - e.g. `.stock All Australian Wool`
- `.sell`: Adds an item to list of items for sale at the specified Store.
  - `.sell <Store_Name> : <Item_Name> : <Quantity> : <Cost_in_Diamonds>`
  - e.g. `.add_item All Australian Wool : Red Wool : 2 Stacks : 1` (Note: don't put D or Diamonds in cost)
- `.remove_item`: Removes an item to the list of items for sale at the specified store.
  - `.remove_item <Store_Name> : <Item_Name>`
  - e.g. `.remove_item All Australian Wool : Red Wool`
- `.update_item`: Updates the details of an existing item in the specified store's inventory.
  - `.update_item <Store_Name> : <Old_Item_Name> : <New_Item_Name> : <New_Item_Quantity> : <New_Item_Cost>`
  - e.g. `.update_item All Australian Wool : Red Wool : Blue Wool : 2 Stacks : 1`
- `.update_store`: Updates the details of an existing store.
  - `.update_store <Old_Store_Name> : <New_Store_name> : <New_X_Coord> : <New_Z_Coord> : <New_Description>`
  - e.g. `.update_store All Australian Wool : non-Australian Wool : 50 : -234 : Cheap Wool`
- `.bot_info`: Gives a brief description of the bot.
- `.help`: Provides list of commands.
- `.help <command_name>`: Provides detailed command specific help.
  - e.g. `.help stores`
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
