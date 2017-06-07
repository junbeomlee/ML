import sklearn.preprocessing

# min = 999999999
# max = 0
#
# with open("./cluster_num__count_final", encoding="ISO-8859-1") as f:
#     lines = f.readlines()
#
#     for line in lines:
#         sentence = line.split(",")
#
#         if int(sentence[1]) < min:
#             min = int(sentence[1])
#
#         if int(sentence[1]) > max:
#             max = int(sentence[1])

value_list = []
with open("./cluster_num__count_final", encoding="ISO-8859-1") as f:
    lines = f.readlines()

    for line in lines:
        sentence = line.split(",")
        value_list.append(float(sentence[1]))

scaled = sklearn.preprocessing.normalize(value_list)
print(scaled)
# normalized = (scaled - min(scaled)) / (max(scaled) - min(scaled))
#
# print(normalized)
# #
# # print (min)
# # print (max)
# #
output = open('cluster_num__count_final_norm', 'w+')

with open("./cluster_num__count_final", encoding="ISO-8859-1") as f:
    lines = f.readlines()
    index = 0
    for line in lines:
        sentence = line.split(",")
        output.write(sentence[0] + ",")
        output.write(str(scaled[0][index]))
        output.write("\n")
        index += 1

output.close()
