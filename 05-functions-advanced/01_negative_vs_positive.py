# #1
# sequence = input().split()
# total_sum_negatives = sum([int(x) if int(x) < 0 else 0 for x in sequence])
# total_sum_positives = sum([int(x) if int(x) > 0 else 0 for x in sequence])
# print(total_sum_negatives)
# print(total_sum_positives)
# if abs(total_sum_negatives) > total_sum_positives:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")


#2
def numbers(sequence):
    positives = sum(num for num in sequence if num > 0)
    negatives = sum(num for num in sequence if num < 0)
    print(negatives)
    print(positives)
    if abs(negatives) > positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


sequence = [int(x) for x in input().split()]
numbers(sequence)