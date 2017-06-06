dict = {}
output = open('title', 'w');

with open('./contextcleaned_', encoding="ISO-8859-1") as f:
    lines = f.readlines()
    for line in lines:
        sentence = line.split("\t")
        dict[sentence[1]] = "a"
        print(sentence[1])


for k in dict:
    output.write(k+' '+dict[k]+'\n')

output.close()


