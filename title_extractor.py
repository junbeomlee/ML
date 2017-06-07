paper_list = []

output = open('exist_paper', 'w+');

with open("./testDatacleanedJUNBEOM",encoding="ISO-8859-1") as f:
    lines = f.readlines()

    for line in lines:
        sentence = line.split()
        paper_dict = {}
        paper_dict[sentence[0]] =sentence
        paper_list.append(paper_dict)

# print(paper_list)

paper_dict = {}
with open("./result_norm", encoding="ISO-8859-1") as f:
    lines = f.readlines()

    for line in lines:
        sentence = line.split(" [")
        paper_dict[sentence[0]] = " "

# print(paper_dict)

exist_paper_list = []
for paper in paper_list:
    for key in paper:
        if key in paper_dict.keys():
            exist_paper_list.append(paper[key])


for paper in exist_paper_list:
    for word in paper:
        output.write(word+" ")
    output.write("\n")
