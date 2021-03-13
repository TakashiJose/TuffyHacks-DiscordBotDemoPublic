# TuffyHacks-DiscordBotDemo By Jose Sanrindo
## Brief Description
- This is a simple discord bot demo, using python, 
for people to check out and get a gist of how one could 
normally be set up.

## Installation
- Too create your own discord bot you will need to install two things:
- Python Compiler(this will vary between Operating Systems)
>https://www.python.org/downloads/
- Discord.py library
>python3 -m pip install -U discord.py

## Set Up
- To make your own discord bot, you will need to create a application
> - Log in to your discord at https://discord.com/developers/applications
> - Click on the “New Application” button.
> - Give the application a name and click “Create”.
> - Create a Bot User by navigating to the “Bot” tab and clicking “Add Bot”.
- These instructions were pulled from https://discordpy.readthedocs.io/en/rewrite/discord.html

## Bot Invitation
- To invite your discord bot, you will need to find the bot's invite url
> - Log back in to your discord at https://discord.com/developers/applications
> - Enter the application you plan to invite
> - Go to the OAuth2, and mark the "bot" in the scopes list
> - Once that is done, the invite url is made below it
> - Enter the link into your browser, then specify which server you would like to add it to

## Events
- Events are triggers when a certain activity is detected by the bot.
- In the demo we use these event references:
> - on_ready(): when the client is done preparing data received from Discord
> - on_message(): when the client detects a message sent on a text channel
- More event references can be found on https://discordpy.readthedocs.io/en/rewrite/api.html#event-reference

## Commands Framework
- Commands: are triggers when users specify a requested action to the bot.
- Cogs: are a collection of commands, that is made in order to organize the commands once the bot's development increases.
- Extension: are able to allow bot functionality changes during run-time of the bot. 

## Uses in Demo
- "on_message": the bot will check messages sent, if a key word is user, the bot will send the message "nice"
- ".hello": the bot command will respond with "world"
- ".happy": the bot command will respond with the smiling emoji
- ".dice": the bot command will generate a random integer determined by what kind of dice you wish to roll
- ".reload": the bot command will update the use of the file world.py cog extension
- ".world": the bot command is from the cog extension and will do whichever task it is changed to.

## Now Lets Look at The Demo
- https://github.com/TakashiJose/TuffyHacks-DiscordBotDemoPublic

## Resources/Links
- Discord.py documentation
>https://discordpy.readthedocs.io/en/rewrite/index.html#
- "Python Create Discord Bot on Raspbery Pi" By Ginja
>https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi
- "Python: Making a Discord Bot (Rewrite / v1.x)" By Lucas, also has a "Learn Python" playlist
>https://www.youtube.com/playlist?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ