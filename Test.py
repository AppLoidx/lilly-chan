from Parse.Schedule import Schedule

#sch = Schedule("P3112")
#print(sch.test())


class A:

    array = []
    num = 2

a1 = A()
a2 = A()

a1.array.append([2, 3, 4])
a2.array.append([3, 4, 5])

a1.num = 34
a2.num = 22

print(a1.array, a2.array, A.array)
print(a1.num, a2.num, A.num)
