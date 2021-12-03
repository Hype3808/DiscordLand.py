from discordland import AsyncClient
import asyncio

client = AsyncClient('token')

async def main():
    result = await client.get_bot_info()
    print(result.discrim)

asyncio.get_event_loop().run_until_complete(main())
