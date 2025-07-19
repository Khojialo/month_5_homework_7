# import random
#                       Question 1
# nums = [1,2,3,4,5,6,7,8,9,10]
#
# class NumIterator:
#     def __init__(self,nums:list):
#         self.nums = nums
#         self.index = 0
#
#
#     def __iter__(self):
#         return self
#
#
#     def __next__(self):
#         if self.index >=len(self.nums):
#             raise StopIteration("Element not found")
#         num = self.nums[self.index]
#         self.index += 1
#         return num
#
#
# my_nums = NumIterator(nums)
# print(my_nums.__next__())
# print(my_nums.__next__())
# print(my_nums.__next__())

#                                  QUESTION 2

# names = ["Alan","Rose","Bull"]
#
# my_list = iter(names)
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))

#                                   QUESTION 3
# matn = "Salom Python"
# def harf(text:str):
#     for i in text:
#         yield i
# print(list(harf(matn)))

#                                   QUESTION 4

# def simple_gen():
#     for i in range(1,6):
#         yield i
#
# for j in simple_gen():
#     print(j)

#                                   QUESTION 5

# matn = "Salom Python"
#
# def my_gen(text:str):
#     for i in text.split():
#         yield len(i)
# print(list(my_gen(matn)))


#                                   QUESTION 6

# def toq_gen():
#     for i in range(1,11):
#         if i % 2 !=0:
#             yield i
#
# print(list(toq_gen()))

#                                   QUESTION 7

# def juft_gen():
#     for i in range(1,11):
#         if i % 2 ==0:
#             yield i
#
# print(list(juft_gen()))

#                                   QUESTION 8

# def square_gen():
#     for i in range(1,11):
#             yield i**2
#
# print(list(square_gen()))

#                                   QUESTION 9

# nums = [-1,2,-5,6,-10,12]
# def musbat_gen():
#    for i in nums:
#        if i > 0:
#            yield i
#
# print(list(musbat_gen()))

#                                   QUESTION 10

# matn = "Salom Python"
#
# def teskari_gen(text:str):
#     yield text[::-1]
#
# print(list(teskari_gen(matn)))

#                                   QUESTION 11

# son = int(input("Sonni kiriting: "))
#
# def n_gen(n):
#     count = 1
#     for i in range(1,n+1):
#         count *= i
#     yield count
# print(list(n_gen(son)))


#                                   QUESTION 12


# nums = [1,2,3,4,5,7,3,4,5,1]
#
# def takroriy_gen(n:list[int]):
#     n_l = []
#     for i in n:
#         if not i in n_l:
#             n_l.append(i)
#             yield i
# print(list(takroriy_gen(nums)))


#                                   QUESTION 13

# son = int(input("Sonni kiriting:"))
# sonlar = [2,3,4,5,6,8]
#
# def kopaytma(nums:list,n:int):
#     for i in nums:
#         yield i * n
#
#
# print(list(kopaytma(sonlar,son)))


#                                   QUESTION 14

# son = [2,4,5,67,8,7]
#
# def min_max_gen(nums:list):
#         yield min(nums)
#         yield max(nums)
# print(list(min_max_gen(son)))

#                                   QUESTION 15

# lugat = {"name":"Khoji","last_name":"Erkinjonov"}
#
# def lugat_gen(n:dict):
#     md = {}
#     for key,value in n.items():
#         md[value] = key
#     yield md
#
# print(list(lugat_gen(lugat)))

#                                   QUESTION 16

# d1 = {"name":"Khoji"}
# d2 = {"lastname":"Erkinjonov"}
#
# def one(*n:dict):
#     n_d = {}
#     for i in n:
#         n_d.update(i)
#     yield n_d
#
# print(list(one(d1,d2)))



#                                   QUESTION 17


# dict_son= {1: 2, 3: 2, 4: 2, 6: 7}
#
# def k_gen(n:dict):
#     values  = list(n.values())
#     yield max(set(values),key=values.count)
#
# print(list(k_gen(dict_son)))

#                                   QUESTION 18

# def num_gens():
#     for i in range(1,5):
#         yield random.randint(1,10)
#
# print(list(num_gens()))

#                                   QUESTION 19

# num = 5
#
#
# def tub_gen(n:int):
#     son = 2
#     count = 0
#     while count < n:
#         for i in range(2,int(son**0.5)+1):
#             if son%i == 0:
#                 break
#         else:
#             yield son
#             count +=1
#         son+=1
#
# print(list(tub_gen(num)))
#

