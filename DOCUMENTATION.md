# DiscordLand.py
Welcome, and thank you for using DiscordLand.py! This wrapper support asynchronous and synchronous. I am not a part in DiscordLand API, I just made this wrapper! 

## Note
You may open an issue or a pull requests if you have any suggestion regarding this **wrapper**

**If you have issues, questions or suggestion regarding discord land api, consider join the [Discord Land Support Server](https://discord.gg/myFQXQctsb)**

# Important Links

- [Discord Land](https://discordland.gg)
- [Discord Land Support Server](https://discord.gg/myFQXQctsb)
- [Discord Land API Docs](https://discordland.gg/docs)

# Getting Started
To begin, you have to install *discordland.py* using the following commands

```
pip install -U discordland.py
```

or 

```
python -m pip install -U discordland.py
```

or

```
pip install -U git+https://github.com/Hype3808/DiscordLand.py
```

After that, start by creating a **Client**:
```py
# Synchronous client

import discordland

client = discordland.Client("your_discordland_bot_token_here")
# the token is not your bot token from your discord developers page,
# it is your bot's discord land token,
# you can get it from https://discordland.gg/bot/:bot_id/stats
```

or

```py
# Asynchronous client

import discordland

client = discordland.AsyncClient("your_discordland_bot_token_here")
# the token is not your bot token from your discord developers page, 
# it is your bot's discord land token, 
# you can get it from https://discordland.gg/bot/:bot_id/stats
```

## Methods
Asynchronous and synchronous methods

### get_bot_info()
Get the bot's info and stats

#### Returns
[BotInfo](https://github.com/Hype3808/DiscordLand.py/blob/main/DOCUMENTATION.md#botinfo)

#### Raises
**APIError:** Raise when API is having problem or your token is invalid

### get_user_votes(user_id)

#### Parameters
**user_id**: int
> The user's discord id

#### Returns
[bool](https://docs.python.org/3/library/functions.html#bool)

### Raises
**APIError:** Raise when API is having problem or your token is invalid


# Results

## BotInfo
Returns the bots information and stats

### Attributes
> id

Your bot's Discord ID

> username

Your bot's username

> discriminator

Your bot's discriminator

> discrim

An alias for *discriminator*

> prefix

Your bot's prefix

> website

Your bot's website

> support_server

Your bot's support_server

> server

An alias for *support_server*

> tags

Your bot's tags

> owner

Bot's owner

> owners

Bot's owners, the list will be nothing if the owner only have one

> added_on

The timestamp when your bot is added on

> votes

The votes your bot gains

> invites

See how many invites your bot gained

> servers

The server's your bot joined

> members

Members your bot's have
