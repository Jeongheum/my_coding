import telegram
import json
with open('personal.json','r') as f:
  json_data = json.load(f)
  
Jay_noti_bot_Token=json_data["telegram"]["token"]
myID=json_data["telegram"]["id"]
bot = telegram.Bot(token = Jay_noti_bot_Token)
# for i in bot.getUpdates():
#     print(i.message)
#print(bot.get_me())

# send text message
txt='안녕하세요 만나서 반가워요'
bot.sendMessage(chat_id = myID, text=txt)

# send photo
img_url= url
bot.send_photo(chat_id= myID, photo=img_url)
