# import lilly

# lilly = Lilly.Lilly()

# print(lilly.get_schedule())

from group_queue import queue
queue = queue.Queue()

queue.new_queue()

array = queue.get_queue()
for i in range(len(array)):
    print(f"{i+1}. {array[i].get_name()} ({array[i].get_id()})")

queue.delete_person("13")
print("\nqueue.delete_position('13')")

print("=================================================")
array = queue.get_queue()
for i in range(len(array)):
    print(f"{i+1}. {array[i].get_name()} ({array[i].get_id()})")

queue.add_person("13", 4)
print("\nqueue.add_person('13', 4)")

print("=================================================")
array = queue.get_queue()
for i in range(len(array)):
    print(f"{i+1}. {array[i].get_name()} ({array[i].get_id()})")

queue.swap('5', '7')
print("\nqueue.swap('5', '7')")

print("=================================================")
array = queue.get_queue()
for i in range(len(array)):
    print(f"{i+1}. {array[i].get_name()} ({array[i].get_id()})")

queue.swap('12','5')
print("\nqueue.swap('12','5')")

print("=================================================")
array = queue.get_queue()
for i in range(len(array)):
    print(f"{i+1}. {array[i].get_name()} ({array[i].get_id()})")

print("\n=====HISTORY=====\n")
for i in queue.history.get_history():
    print(i)
