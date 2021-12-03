from discordland import Client

client = Client('hidden')

result = client.get_bot_info()
print(result.discrim)
