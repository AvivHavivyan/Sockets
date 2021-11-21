import re

m = re.search(r'([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})', '03:22:33:44:55:66')
print(m.group(0))
first = '03:22:33:44:55:66'.split(":", 1)

first = int(first[0])
print(first)
bit = first & 0b00000001
print(bit)
if bit == 0:
    print("multicast")
else:
    print("unicast")

