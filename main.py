from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message
from responses import get_response

# load discord token from safe location

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

# Message fucntionality

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('message was empty because intents were not enabled')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    if '!' in user_message[0]:
        try:
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(e)

# Handeling bot startup 
@client.event
async def on_ready() -> None:
    print(f'{client.user} in online!')

# Handeling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# handeling add user roles
@client.event    
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1216500022699364412:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        if payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='not playing')

        elif payload.emoji.name == '👤':
            role = discord.utils.get(guild.roles, name="DM available")
        
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji)
        
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)
                print("role added")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

# handeling remove user roles
@client.event    
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1216500022699364412:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        if payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='not playing')

        elif payload.emoji.name == '👤':
            role = discord.utils.get(guild.roles, name="DM available")
        
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji)
        
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("role removed")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

# Main enty point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()