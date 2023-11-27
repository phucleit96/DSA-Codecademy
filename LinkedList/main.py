from LinkedList import LinkedList

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
#
#
# # print(my_linked_list.pop().value)
# # print(my_linked_list.pop().value)
# # print(my_linked_list.pop().value)
#
# # my_linked_list.set_value(2, "Hello Con Cac")
# my_linked_list.insert(2, "Hello Worlddddd")
# my_linked_list.insert(1, "Hello Worlddddd11")
# my_linked_list.append(4)
# my_linked_list.print_list()
# # my_linked_list.reverse()
# # my_linked_list.print_list()
# print(my_linked_list.find_middle_node())

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()