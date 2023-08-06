from functions import *
# cerate the bot

bot = create_bot('Vantey')

# train the bot with english greetings
train_all_data(bot)

# train the bot with your custom data
house_owner = [
    "Who is the owner of this house?",
    "Vanguard of SA"
]
custom_train(bot, house_owner)

# start the bot
start_chatbot(bot)