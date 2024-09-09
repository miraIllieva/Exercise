n = int(input())
positivies = []
negtivies = []

for i in range(n):
    current_numner = int(input())
    if current_numner > 0:
        positivies.append(current_numner)
    else:
        negtivies.append(current_numner)

print(positivies)
print(negtivies)
print(f"Count positivies: {len(positivies)}. Sum of negatives: {sum(negtivies)}")
