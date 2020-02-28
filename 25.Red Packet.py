"""
Plans:
1. get the total red packet and get the total value
2. ensure each red packet has at least $0.01 -- creating a list with each red packet has at least $0.01
3. random change red packet value one by one
4. print out a list with all red packet value
"""

import random

def sum_remain(l,n):
    sum_before = 0
    sum_after = 0
    for i in l[:n]:
        sum_before +=i
    for i in l[n+1:]:
        sum_after += i
    return sum_before + sum_after
"""
testlist = [1,2,3,4,5]
print(sum_remain(testlist,0))
"""

while True:
    try: # ensure that buyer entered string can be converted to int
        packet_count = int(input("Please enter count of packet in integer: "))
        while True:
            try: # ensure that buyer entered string can be converted to float
                value = round(float(input(f"Please enter the value of the red packet at least ${0.01*packet_count} (format: 0.00): ")), 2)
                if value >= packet_count*0.01: # ensure everyone at least have $0.01 in red packet
                    break
                else:
                    print("you have entered lower value than minimum, please re-enter:")
                    pass
            except:
                print("Please enter correct format of packet value!")
        break
    except:
        print("Please enter correct format of packet count!")
        pass

print(value, packet_count)

packet = [] # given a default amount for everyone as 0.01
for i in range(packet_count):
    packet.append(0.01)
print(packet)

for i in range(0, packet_count): # random granted red packet
    packet[i] = round(random.uniform(0.01, value - sum_remain(packet, i)), 2)

print(packet)

