number = int(input())
prime = True
count = 0

for i in range(1, number + 1):

    if number % i == 0:
        count += 1
    if count > 2:
        prime = False
        break

print(prime)

