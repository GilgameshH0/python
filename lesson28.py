# ДЗ 
names = ["John", "Elena", "Ivan", "Sergey"]

# print(len(names[0]))
# def get_names(nms):
#     for i in nms:
#         if len(i) == 4:
#             print(i)
# get_names(names)

def get_true(names):
    return [i for i in names if len(i) == 4]

print(get_true(names))