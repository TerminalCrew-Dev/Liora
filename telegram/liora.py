import telebot
import re
import json
from dotenv import dotenv_values

config = {**dotenv_values(".env")}

from app import check_token_data



# Define your regex pattern
pumpfun_pattern = r"^[a-zA-Z0-9]{40}pump$"


html_response = """
# todo come up with good response
"""



bot = telebot.TeleBot(token=config["bot_token"])

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, """Hi there, I'm Liora. I'll be your personal navigator through the Sol Terminal.""")

# Handler for messages matching the regex
@bot.message_handler(func=lambda message: re.match(pumpfun_pattern, message.text))
def handle_regex_match(message):

    token = check_token_data(message.text)
    token_data = json.dumps(token.get("token_info", "Couldn't get data..."))
    bot.reply_to(message, token_data)


bot.infinity_polling()