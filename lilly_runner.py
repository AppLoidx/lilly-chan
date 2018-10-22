import vk_api
from lilly import Lilly
from vk_api.longpoll import VkLongPoll, VkEventType
import config


def write_msg(user_id, s):
    vk.method('messages.send', {'user_id': user_id, 'message': s})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=config.token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Словарь, где будут хранится разные объекты бота для разных пользователей
users_bot_class_dict = {}


def run():
    print("Server started")
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:

                print('New message:')
                print('For me by: ', end='')

                print(event.user_id)

                user_id = event.user_id
                if user_id not in users_bot_class_dict:
                    users_bot_class_dict[user_id] = Lilly()

                # Checking to welcome message send
                if users_bot_class_dict[user_id].WELCOME_MSG_SEND:
                    write_msg(event.user_id, users_bot_class_dict[user_id].update_screen(event.text))
                else:
                    write_msg(event.user_id, users_bot_class_dict[user_id].get_welcome_msg(event.user_id))

                print('Text: ', event.text)
                print()


print("Lilly_Test is ready")
