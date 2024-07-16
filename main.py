def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

        result = alice, bob

    return result
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)
print(result)