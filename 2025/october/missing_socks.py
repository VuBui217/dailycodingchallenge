"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-18

                                                sMissing Socks
Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

Every 2 wash cycles, you lose a single sock.
Every 3 wash cycles, you find a single missing sock.
Every 5 wash cycles, a single sock is worn out and must be thrown away.
Every 10 wash cycles, you buy a pair of socks.
You can never have less than zero total socks.
Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
Return the number of complete pairs of socks.
"""

def sock_pairs(pairs, cycles):
    num_of_socks = 2*pairs
    for i in range(1,cycles+1):
        if i % 2 == 0:
            num_of_socks-=1
        if i % 3 == 0:
            num_of_socks+=1
        if i % 5 == 0:
            num_of_socks-=1
        if i % 10 == 0:
            num_of_socks+=2

        num_of_socks=max(num_of_socks,0)
    
    return num_of_socks//2
        #optimal way
        #lost = cycles // 2
        #found = cycles // 3
        #worn = cycles // 5
        #bought = (cycles // 10) * 2
        #socks = 2 * pairs - lost + found - worn + bought
        #return max(socks, 0) // 2

#print(sock_pairs(2, 5))   
"""
cycles =        0   1   2   3   4   5   6   7   8
num_of_socks =  2   2   1   2   1   0   1   1   0
"""

#print(sock_pairs(1, 8))

print(-3//2)