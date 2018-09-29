import vk_api
from Lilly import Lilly
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, s):
    vk.method('messages.send', {'user_id': user_id, 'message': s})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token='63759c99295eb6ccfcbff8e9df2b87fa6522111610963781ffc158c21e37bb3b297cc9cbdd9e5011350f7')
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Словарь, где будут хранится разные объекты бота для разных пользователей
users_bot_class_dict = {}

print("Сервер запущен.")

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')

        if event.to_me:

            print('Для меня от: ', end='')

            print(event.user_id)

            user_id = event.user_id
            if user_id not in users_bot_class_dict:
                users_bot_class_dict[user_id] = Lilly()
            if users_bot_class_dict[user_id].WELCOME_MSG_SEND:
                write_msg(event.user_id, users_bot_class_dict[user_id].update_screen(event.text))
            else:
                write_msg(event.user_id, users_bot_class_dict[user_id].get_welcome_msg(event.user_id))

        print('Текст: ', event.text)
        print()



