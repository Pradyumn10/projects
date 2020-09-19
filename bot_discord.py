'''
* @file discord_bot.py
* @author Pradyumn Joshi
* @brief A generalised discord bot playing music
* @version 0.1.0
* @date 2020-09-19
*
* @copyright Copyright (c) 2020
'''
import discord
from discord.ext import commands, tasks
from random import choice
import datetime
from ruamel.yaml import YAML
import youtube_dl
import os

yaml = YAML()

with open("./config.yml",'r', encoding = 'utf-8') as file:
    config = yaml.load(file)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = config['YTDL Format Options']

ffmpeg_options = config['FFMPEG Options']

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


client = commands.Bot(command_prefix = config['Prefix'], 
        description = 'A generalized bot developed by Pradyumn', 
        case_insensitive = True)

token = "NzUzNTEzNTk4NDU3NzQxMzIy.X1nSOQ.XjHKC66qt0lrwTvGExbPH2GE4oM"   #bot token

log_channel_id = config['Log Channel ID']

client.embed_color = discord.Color.from_rgb(
        config['Embed Settings']['Color']['r'],
        config['Embed Settings']['Color']['g'],
        config['Embed Settings']['Color']['b']
        )

client.footer = config['Embed Settings']['Footer']['Text']
client.footer_image = config['Embed Settings']['Footer']['Icon URL']
client.prefix = config['Prefix']
client.playing_status = config['Playing Status'].format(prefix = client.prefix)

client.token = os.getenv('BotToken')

#events
@client.event
async def on_ready():
    """[summary]
    """
    print(f'{client.user} is ready!')
    
    game = discord.Game(name=client.playing_status)
    await client.change_presence(activity = game)
    
    embed= discord.Embed(
            title = f'{client.user.name} online!',
            color = client.embed_color,     #discord.Color.from_rgb(0,0,0),
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            )
    embed.set_footer(
            text = client.footer,
            icon_url = client.footer_image
            )
    client.log_channel = client.get_channel(log_channel_id)
    await client.log_channel.send(embed = embed)
    #await client.log_channel.add_reaction('\N{EYES}')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error!! ({error})')
    print("Error", error)

#when member joins
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    print('join')
    await channel.send(f'{member.mention} Joined the discord server')

#when member leaves
@client.event
async def on_member_leave(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    print('member left')
    await channel.send(f'{member.mention} Joined the discord server')
    await member.create_dm()
    await client.dm_channel.send(f'You will be missed!!')


#commands
@client.command(name="hi", aliases = ['hello'], help = "Returns a random welcome message")
async def hi(ctx):
    msg = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    print(choice(msg))
    await ctx.send(f"Hi! I am Anthem ")
    await ctx.send(choice(msg))


@client.command(name="ping", help="Returns the latency")
async def ping(ctx):
    print(f'**Pong!** Latency : {round(client.latency*1000)}ms')
    await ctx.send(f'**Pong!** Latency : {round(client.latency*1000)}ms')

@client.command(name="server", help="Returns the server details")
async def server(ctx):
    channel = ctx.message
    name = ctx.guild.name
    description = ctx.guild.description
    owner = ctx.guild.owner
    s_id = ctx.guild.id 
    region = ctx.guild.region
    member_count = ctx.guild.member_count   
    icon = ctx.guild.icon_url
    embed= discord.Embed(
            title = f'{client.user.name} is here to help',
            color = client.embed_color,     #discord.Color.from_rgb(0,0,0),  
            )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="owner", value=owner,inline = True)
    embed.add_field(name="server id", value=s_id,inline = True)
    embed.add_field(name="region", value=region,inline = True)
    embed.add_field(name="member count", value=member_count,inline = True)
    print("server")
    await ctx.channel.send(embed = embed)

@client.command(name="user", help="Returns user count")
async def user(ctx):
    await ctx.send(ctx.guild.member_count)
    print(ctx.guild.member_count)


@client.command(name="restart", aliases=['re'], help="Restarts the bot")
async def restart(ctx):
    embed= discord.Embed(
            title = f'{client.user.name} restarting!',
            color = client.embed_color, #discord.Color.from_rgb(0,0,0),
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            )
    embed.set_author(
            name = ctx.author.name,
            icon_url = ctx.author.avatar_url
            )
    embed.set_footer(
            text = client.footer ,
            icon_url = client.footer_image
            )

    await client.log_channel.send(embed = embed)
    await ctx.message.add_reaction('💯')
    await client.close()

@client.command(name="broklyn", aliases=['99'], help="Returns a random 99 quote")
async def broklyn(ctx):
    msg = ['cool cool cool cool', 'no doubt! no doubt! no doubt! no doubt!', 'name of your sex tape','Terry gonna destroy it', 'boyle brothers', 'G-hive','Go play Kwazy cup cakes', 'I would like you to be my mentor']
    #random_number = random.randint(0,8)
    #final_msg = msg[random_number]
    print(choice(msg))
    await ctx.send(choice(msg))

@client.command(name="f", help="returns a sad message")
async def f(ctx):
    msg = ['Go play Kwazy cup cakes', 'noob','better luck next time']
    #random_number = random.randint(0,2)
    #final_msg = msg[random_number]
    await ctx.send(choice(msg))
    print(choice(msg))

'''
@client.command()
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in ctx.logs(channel, limit=int(amount)):
        messages.append(message)
    await ctx.delete_message(messages)
    await ctx.send('Messages deleted!')
'''

@client.command(name="join", help="Joins the voice channel")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(name='leave', aliases=['l'], help="Leaves the voice channel")
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()


@client.command(name='play', aliases=['p'], help="It plays music")
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
    
    server = ctx.message.guild
    voice_channel = server.voice_client
    
    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after= lambda e:print("Player error : %s"%e)if e else None)
    print("Playing song")    
    await ctx.send(f'**Now Playing** {player.title}')

@client.command(name="stop", aliases=['s'], help="It stops the music and the makes the bot leave voice channel")
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    

@client.command(name='die', help="Returns a random last words")
async def die(ctx):
    msg=['why have you brought my short life to end','i could have done so much', 'i have a family, kill them instead']
    await ctx.send(choice(msg))
    
client.run(client.token,  reconnect=True)
