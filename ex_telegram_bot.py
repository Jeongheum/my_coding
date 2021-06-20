import telegram

Jay_noti_bot_Token="1805573611:AAHw6pHuuJRlwQH_UbEIHtnM4pLtyDJcvSY"
botID=1805573611
myID=1259062846
bot = telegram.Bot(token = Jay_noti_bot_Token)
# for i in bot.getUpdates():
#     print(i.message)
#print(bot.get_me())
bot.sendMessage(chat_id = myID, text='안녕하세요 만나서 반가워요')
bot.send_photo(chat_id= myID, open('ss.png','rb'))
