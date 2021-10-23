# DiscordLand.py
- DiscordLand.py supports async and sync

# Installation
```
pip install -U discordland.py
```

or

```
pip install -U git+https://github.com/Hype3808/DiscordLand.py.git
```

# Documentation

## Client
> `class Client(dland_token: str)`

### Methods:
> *def* `get_bot_info()`
>> Return Type:
>> 
>> discordland.BotInfo

>> Raises:
>>
>> APIError: Raise when status code is not **200**

> *def* `get_user_voted(user_id: int)`
>> Return Type:
>> 
>> [bool](https://docs.python.org/3/library/functions.html#bool)

>> Raises:
>> 
>> APIError: Raise when status code is not **200**

## AsyncClient
> `class AsyncClient(dland_token: str)`

### Methods:
> *async def* `get_bot_info()`

>> Return Type:
>> 
>> discordland.BotInfo

>> Raises:
>> 
>> APIError: Raise when status code is not **200**

> *async def* `get_user_voted(user_id: int)`
>> Return Type:
>> 
>> [bool](https://docs.python.org/3/library/functions.html#bool)

>> Raises:
>> 
>> APIError: Raise when status code is not **200**
