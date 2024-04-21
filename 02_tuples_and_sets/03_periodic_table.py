# n = int(input())
# unique_compounds = set()
# for _ in range(n):
#     chemical_compounds = input().split()
#     for compound in chemical_compounds:
#         unique_compounds.add(compound)
# for element in unique_compounds:
#     print(element)

n = int(input())
unique_components = {compound for _ in range(n) for compound in input().split()}
for el in unique_components:
    print(el)