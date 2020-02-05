import discord
import asyncio
import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Discord')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("-> $help <-")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello! I am PlacekBot, the creation of Placek#3618. Hope you enjoy me :smile: ")

    if message.content.startswith('$invite'):
        await message.channel.send("Invite me to your server with this link: link here")

    if message.content.startswith('$help'):
        await message.channel.send("Prefix is $. Commands are: hello, invite, help, reddit, srs. More coming soon!")

    if message.content.lower().startswith('$reddit '):
        subToCheck = message.content.split(' ')[1].lower()
        if len(subToCheck) > 20: #  Subreddit names are a max 20 characters in length, so no point searching for one with a longer name.
            await message.channel.send("That name is too long for a subreddit. Please try a shorter name.")
            return
        try:
            post = reddit.subreddit(subToCheck).random() #  Gets a random post from the sub mentioned.
            await message.channel.send(post.url)
        except Exception as e: #  If the sub doesn't exist tell the user.
            await message.channel.send('Error! Possibly the sub doesnt exist, or something else went wrong.')
			
    if message.content.startswith('$srs'):
        post = reddit.subreddit('subredditsimulator').random()
        await message.channel.send(post.title)
        

client.run('')
