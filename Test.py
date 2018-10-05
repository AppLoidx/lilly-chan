import vk_api
import time

vk = vk_api.VkApi(token='63759c99295eb6ccfcbff8e9df2b87fa6522111610963781ffc158c21e37bb3b297cc9cbdd9e5011350f7')

values = {'out':0, "count":100, 'time_offset':60}


def write_msg(user_id, s ):
    vk.method('messages.send', {'user_id':user_id, "message":s})

while True:
    response = vk.method('messages.get', values)

    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        write_msg(item['user_id'], "hey")
    time.sleep(1)