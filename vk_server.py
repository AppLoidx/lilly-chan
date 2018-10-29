from lilly import Lilly
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotMessageEvent
from vk_api.bot_longpoll import VkBotEventType
from config import vk_api_token


# TODO: Add to editor package as class
def clean(text):
    result = ""
    not_append = False

    for i in list(text):
        if i == "[":
            not_append = True
        if not_append:
            pass
        else:
            result += i
        if i == "]":
            not_append = False

    return result


token = vk_api_token    # access_token
vk = vk_api.VkApi(token=token)
vk_s = vk.get_api()

lilly = Lilly()     # Ядро бота

longpoll = VkBotLongPoll(vk, 171857362)  # VkApi, group_id

# Слушаем сервер
for event in longpoll.listen():

    # Новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Новое сообщение:')

        if event.group_id:
            print(event.object.from_id, 'пишет: ')

            vk_s.messages.send(peer_id=event.object.peer_id,
                               message=lilly.update_screen(clean(event.object.text)[1::]))

        print('Текст: ', event.object.text, end="\n")

