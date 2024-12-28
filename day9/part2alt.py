class Region:
    def __init__(self, file_id, length):
        self.file_id = file_id
        self.length = length
        self.prev = None
        self.next = None

    def is_blank(self):
        return self.file_id < 0


with open('input.txt') as f:
    disk_map = [int(c) for c in f.read()]

head = Region(-1, 0)
cur = head

file_id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        next = Region(file_id, disk_map[i])
        file_id += 1
        cur.next = next
        next.prev = cur
        cur = next
    elif disk_map[i] > 0:
        next = Region(-1, disk_map[i])
        cur.next = next
        next.prev = cur
        cur = next

    

print("----")

print(cur.file_id)
print(cur)
print(cur.prev)
print(cur.prev.prev)
tail = Region(-1, 0)
cur.next = tail
tail.prev = cur
right = tail.prev

print(tail.file_id)
print(tail.prev.file_id)
print(tail.prev.prev.file_id)
print(tail.prev.prev.prev.prev.file_id)
print(tail.prev.prev.prev.prev.prev.file_id)
print(tail.prev.prev.prev.prev.prev.prev.file_id)

first_blank = head
while not first_blank.is_blank() and not first_blank == right:
    first_blank = first_blank.next

if first_blank != right:
    while right is not None and right != first_blank:
        print("right", right.file_id, right.length)
        prev = right.prev
        if not right.is_blank():
            left = first_blank
            while not (left.is_blank() and left.length >= right.length) and left != right:
                left = left.next
            
            if left != right:
                prev.next = right.next
                right.next.prev = prev
                
                left.file_id = right.file_id
                print("file_id", right.file_id)

                if left.length > right.length:
                    print("merging")
                    remainder = left.length - right.length
                    left.length = right.length
                    new_region = Region(-1, remainder)
                    new_region.prev = left
                    new_region.next = left.next
                    left.next.prev = new_region
                    left.next = new_region
            # else:
            #     print("no blank space found")
            #     print(prev.prev.prev.file_id)

                
        right = prev

checksum = 0
offset = 0
cur = head.next
while cur is not None:
    length = cur.length
    if not cur.is_blank():
        for i in range(offset, offset + length):
            checksum += i * cur.file_id

    offset += length
    cur = cur.next

print(checksum)