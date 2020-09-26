#Def function for change element 

def hanoi(n, P1, P2, P3):
    global count
    # print('### move', count)
    """ Move n discs from pole P1 to pole P3. """
    if n == 0:
        # No more discs to move in this step
        # print(count-3)
        # count -= 1
        return
    # move n-1 discs from P1 to P2
    # print(count)
    hanoi(n-1, P1, P3, P2)

    if P1:
        # move disc from P1 to P3
        P3.append(P1.pop())
    print('---')
    print('### move', count)
    print('T1:', end='')
    print(*A)
    print('T2:', end='')
    print(*B)
    print('T3:', end='')
    print(*C)
    count += 1
    # move n-1 discs from P2 to P3
    hanoi(n-1, P2, P1, P3)

# Initialize the poles: all n discs are on pole A.
n = int(input())
A = list(range(n,0,-1))
C, B = [], []

Q = ['T1:', 'T2:', 'T3:']
print('### start')
print('T1:', end='')
print(*A)
print('T2:', end='')
print(*B)
print('T3:', end='')
print(*C)
count = 1
hanoi(n, A, B, C)
print(count)
