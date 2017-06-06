dict = {}
output = open('paper_freq_10000', 'w');

with open("./contextcleaned_", encoding="ISO-8859-1") as f:
    lines = f.readlines()

    for line in lines:

        sentence = line.split("\t")
        if sentence[1] in dict:
            count = dict.get(sentence[1])
            count += 1
            dict[sentence[1]] = count
        else:
            dict[sentence[1]] = 1

for k in dict:
    output.write(k + ' ' + str(dict[k]) + '\n')

output.close()
