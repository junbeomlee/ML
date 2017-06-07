import sklearn.preprocessing

value_list = []
with open("./w2v_sig.index", encoding="ISO-8859-1") as f:
    lines = f.readlines()

    for line in lines:
        sentence = line.split(" ")
        value_list.append(float(sentence[2]))

scaled = sklearn.preprocessing.normalize(value_list)

output = open('w2v_sig_norm.index', 'w+')

with open("./w2v_sig.index", encoding="ISO-8859-1") as f:
    lines = f.readlines()
    index = 0
    for line in lines:
        sentence = line.split(" ")
        output.write(sentence[0] + " ")
        output.write(sentence[1] + " ")
        output.write(str(scaled[0][index]))
        output.write("\n")
        index += 1

output.close()