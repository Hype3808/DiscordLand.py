from discordland import AsyncClient
import asyncio

client = AsyncClient('uTAutcfsTKVn5ZStEP')

async def main():
    result = await client.get_bot_info()
    print(result.discrim)

asyncio.get_event_loop().run_until_complete(main())