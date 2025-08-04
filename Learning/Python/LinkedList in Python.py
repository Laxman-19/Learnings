class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None



    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node



    def insert_at_end(self, data):
        if self.head is None: # If linked list is blank
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        node = Node(data, None)
        itr.next = node



    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



    def get_length_of_ll(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    


    def remove_at(self, index):
        if index<0 or index>=self.get_length_of_ll():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head

        while index>1:
            itr = itr.next
            index -= 1
        itr.next = itr.next.next



    def insert_at(self, index, data):
        if index == 0:
            node = Node(data, self.head)
            self.head = node
            return

        itr = self.head
        while index>1:
            itr = itr.next
            index -= 1

        node = Node(data, itr.next)
        itr.next = node

        # count = 0
        # itr = self.head
        # while itr:
        #     if count == index - 1:
        #         node = Node(data, itr.next)
        #         itr.next = node
        #         break
        #     itr = itr.next
        #     count = count + 1
    


    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr.data != data_after:
            count += 1
            if count == 5:
                print('Value not in Linked List') 
                return
            itr = itr.next
        node = Node(data_to_insert, itr.next)
        itr.next = node

    # def insert_after_value(self, data_after, data_to_insert):
    #     count = 0
    #     itr = self.head
    #     while itr:
    #         if itr.data == data_after:
    #             node = Node(data_to_insert, itr.next)
    #             itr.next = node
    #             return 
    #         itr = itr.next
    #         count += 1
    #         if count == 5:
    #             print('Value not in Linked List')
    #             return  
    #     print('Value not in Linked List')  



    def remove_by_value(self, data):
        count = 0
        itr = self.head

        if itr.data == data:
            itr.next = self.head
            return

        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

            count += 1
            if count == self.get_length_of_ll() - 1:
                print('Value not in Linked List')
                return 



    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end="->")
            itr = itr.next
        print()



if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_values([1,2,3,4,5])
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.insert_at(0,25)
    ll.print()
    ll.insert_after_value(6,255)
    ll.print()
    ll.remove_by_value(3456)
    ll.print()
