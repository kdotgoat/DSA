my_list = [10,20,30,40]
my_list.insert(1, 15)
print(my_list)
list1 = [50,60,70]
my_list.extend(list1)
print(my_list)
my_list.remove(70)
print(my_list)
def myfunc(n):
    abs(n - 50)
    my_list.sort(key=myfunc)
    print(my_list)
    index_of_30 = my_list.index(30)
    print(index_of_30)