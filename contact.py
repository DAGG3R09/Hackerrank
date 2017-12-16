class contacts:
    def __init__(self):
        self.count = 0
        self.alphabets = [None for i in range(26)]

    def add_contacts(self, string):
        x = self
        x.count += 1

        for s in string:
            hash = ord(s)-ord('a')
            if x.alphabets[hash] == None:
                x.alphabets[hash] = contacts()
                x.alphabets[hash].count = 1
            else:
                x.alphabets[hash].count += 1
            x = x.alphabets[hash]


        # print(">", self.count)

    def find_partial(self, string):
        for s in string:
            hash = ord(s)-ord('a')
            if self.alphabets[hash] == None:
                return 0

            self = self.alphabets[hash]
        return self.count

q = int(input())
contact_book = contacts()
for a0 in range(q):
    command, string = input().split()

    if command == "add":
        contact_book.add_contacts(string)
    else:
        print(contact_book.find_partial(string))
