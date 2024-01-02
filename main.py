# sample_list = [14, 3, 6, 7, 178]
# def multiply_elements(lst):
#     result = 1
#     for element in lst:
#         result *= element
#     return result
#
# def find_minimum(lst):
#     if not lst:
#         return None
#     minimum = lst[0]
#     for element in lst:
#         if element < minimum:
#             minimum = element
#     return minimum
#
# def count_primes(lst):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     count = 0
#     for element in lst:
#         if is_prime(element):
#             count += 1
#     return count
#
#
# def remove_number(lst, target):
#     count_removed = lst.count(target)
#     lst = [element for element in lst if element != target]
#     return count_removed
#
#
# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list
#
#
# def power_elements(lst, power):
#     powered_list = [element ** power for element in lst]
#     return powered_list
#
# print("Task 1:", multiply_elements(sample_list))
# print("Task 2:", find_minimum(sample_list))
# print("Task 3:", count_primes(sample_list))
# print("Task 4:", remove_number(sample_list, 5))
# print("Task 5:", merge_lists(sample_list, [13, 17, 19]))
# print("Task 6:", power_elements(sample_list, 2))
