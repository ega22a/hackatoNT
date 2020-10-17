import vk_api
import random
import json
import requests
import time

token = '68ff37dd1941ee9d0cc50a6adf61009a33bc31937cee05297110d6d29310ac20490275f4ede0fb919c306'

vk = vk_api.VkApi(token=token)

vk._auth_token()

keyboardSEX = {
    "one_time": True,
    "buttons": [
    [[get_button(label='М', color="primary"),
    get_button(label='Ж', color="negative")],
    get_button(label='Не имеет значения', color="secondary")]
    ]
}
keyboardSEX = json.dumps(keyboardSEX, ensure_ascii=False).encode('utf-8')
keyboardSEX = str(keyboardSEX.decode('utf-8'))

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 1, "filter": "unanswered"})
        #print(messages)
        if messages["count"] >= 1:
            #print(messages)
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.title() = "Начать ":
    except:
        time.sleep(1)
