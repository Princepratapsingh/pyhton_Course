marks=[13,45,48,32,56,93]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("hello")
#     index+=1
for index, mark in enumerate(marks):
    print(index,mark)
    if(index==3):
        print("hello")