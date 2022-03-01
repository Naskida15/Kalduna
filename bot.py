import random
import string
import discord
from discord.ext import commands
from fuzzywuzzy import fuzz

import config

# Initialization
bot = commands.Bot(command_prefix='.', Intents=discord.Intents.all())


def format_word(word):
    word = word.lower()
    word = word.translate(str.maketrans('', '', string.punctuation))
    return word.strip()


@bot.event
async def on_message(message):
    if not message.author.id == config.kalduna_id:
        message_words = message.content.split(' ')

        # "Ra" response
        if len(message_words) < 2:
            for word in message_words:
                if format_word(word) in config.xuina_words:
                    mention = message.author.mention
                    await message.reply(f'{mention} ხუინა')
                    break

        if len(message_words) < 4:
            for word in config.bad_words:
                if fuzz.ratio(message.content, format_word(word)) > 85:
                    mention = message.author.mention
                    await message.reply(f'{mention} {random.choice(config.my_mention_response)}')
                    break

        # My call
        # for i in message_words:
        #     if fuzz.ratio(i, config.owner_calls[0]) > 75 or fuzz.ratio(i, config.owner_calls[1]) > 75:
        #         await message.reply(f'{config.phrases[4]}')
        if str(config.my_id) in message.content:
            await message.reply(f'{config.phrases[4]}')

        # Bot call
        if len(message_words) < 5:
            if fuzz.ratio(message.content, 'kaldun') > 75 or fuzz.ratio(message.content, 'კალდუნ') > 75 or \
                    fuzz.ratio(message_words[0], 'კალდუნ') > 75 or fuzz.ratio(message_words[0], 'kaldun') > 75:
                await message.reply(f'{random.choice(config.phrases)}')
            if bot.user.mentioned_in(message):
                await message.reply(f'{random.choice(config.phrases)}')


# Run
if __name__ == '__main__':
    bot.run(config.TOKEN)
