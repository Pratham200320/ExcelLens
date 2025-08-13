# def onearg(x):
#     print(x)
#
# onearg('heloo')
#
#
# def name(x,y,z):
#     print('hello'+ x + y + z)
#
# name('hi','hello','world')



ratings= (4,5,6,5,5,3,2)
# goodratings = list(filter(lambda x: (x>3),ratings))
# print(goodratings)

newlist= list(map(lambda x: x*10,ratings))

mylist = [1,4,6,3,77,6]

sum_all= list(reduce(lambda x: x+10,ratings))