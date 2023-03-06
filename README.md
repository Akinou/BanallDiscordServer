# BanallDiscordServer
Ban all Discord Server
This script creates a Discord bot using the discord and discord.ext libraries in Python. When the command !remove_all_members is used in a Discord server, the bot will loop through all members in the server and attempt to ban them with the reason "Removing all members". If the bot encounters any errors, such as a member having higher permissions than the bot, it will simply pass over them and continue the loop. Once all members have been looped through, the bot will send a message in the server confirming that all members have been removed.
