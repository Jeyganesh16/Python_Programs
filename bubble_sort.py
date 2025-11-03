def bubble_sort_asc(asc):
    for i in range(len(asc)):
        for j in range(len(asc)- 1 - i):
            if asc[j] > asc[j+1]:
                asc[j],asc[j+1] = asc[j+1],asc[j]

def bubble_sort_desc(desc):
    for i in range(len(desc)):
        for j in range(len(desc)- 1 - i):
            if desc[j] < desc[j+1]:
                desc[j],desc[j+1] = desc[j+1],desc[j]                

numbers =[5,3,8,4,2]
asc_num = numbers.copy()
bubble_sort_asc(asc_num)

desc_num = numbers.copy()
bubble_sort_desc(desc_num)


print("Original List:",numbers)
print("Ascending Order of List:",asc_num)
print("Decending Order of List:",desc_num)
