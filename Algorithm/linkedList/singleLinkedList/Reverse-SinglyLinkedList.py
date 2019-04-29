def reverse_iterative(head):
    # No need to reverse if head is null or there is 1 node
    if head == None or head.next == None:
        return head

    list_to_do = head.next
    reversed_list = head
    reversed_list.next = None

    while(list_to_do != None):
        temp = list_to_do
        list_to_do = list_to_do.next

        temp.next = reversed_list
        reversed_list = temp

    return reversed_list

list_head = [1,2,3,4,5,6,7,8,9]
list_head = reverse_iterative(list_head)
print(list_head)