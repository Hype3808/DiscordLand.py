from discordland import AsyncClient
import asyncio

client = AsyncClient('hidden')

async def main():
    result = await client.get_user_voted(812131142290505799)
    print(result)

asyncio.get_event_loop().run_until_complete(main())
