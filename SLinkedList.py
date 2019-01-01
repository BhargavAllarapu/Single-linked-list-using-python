class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def printList(self):
        currnode = self.headval
        while currnode is not None:
            print(currnode.dataval)
            currnode = currnode.nextval
        return ("--- End of list ---")

    def insert(self, newdata):
        currnode = Node(newdata)
        if self.headval is None:
            self.headval = currnode
        else:
            temp = self.headval
            self.headval = currnode
            currnode.nextval = temp

    def lenghtOfNode(self):
        counter = 0
        currnode = self.headval
        while currnode is not None:
            counter += 1
            currnode = currnode.nextval
        return counter

    def deleteNode(self, position, length):
        if position == 1:
            currnode = self.headval
            self.headval = currnode.nextval
            currnode.nextval = None
            del(currnode)
        elif position == length:
            currnode = self.headval
            for i in range(length-2):
                currnode = currnode.nextval
            temp = currnode.nextval
            currnode.nextval = None
            del(temp)
        elif 1<position<length:
            prevnode = self.headval
            for i in range(position-2):
                prevnode = prevnode.nextval
            currnode = prevnode.nextval
            prevnode.nextval = currnode.nextval
            currnode.nextval = None
            del(currnode)
        else:
            print("Enter a between 1 and "+str(length))

li = SLinkedList()
print("Welcome to single linked list")
a = input("Enter : ")
b = input("Enter : ")
c = input("Enter : ")
d = input("Enter : ")
e = input("Enter : ")
f = input("Enter : ")
li.insert(a)
print(li.printList())
li.insert(b)
print(li.printList())
li.insert(c)
print(li.printList())
li.insert(d)
li.insert(e)
li.insert(f)
print(li.printList())
length = li.lenghtOfNode()
pos=int(input("Enter position to delete: "))
li.deleteNode(pos, length)
print(li.printList())
