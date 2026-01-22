def nums_sums(*args):
    n_sum = 0
    p_sum = 0
    for num in args:
        if num > 0:
            p_sum += num
        else:
            n_sum += num

    return n_sum, p_sum

numbers = map(int, input().split())
neg_sum, pos_sum = nums_sums(*numbers)

print(neg_sum)
print(pos_sum)
if pos_sum > abs(neg_sum):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")