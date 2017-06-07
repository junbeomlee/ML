import operator
import sys
from weight_sum import result_of_weighted_sum

if __name__ == "__main__":

    file_name = sys.argv[1]

    vocaDict = {}

    with open("./w2v_sig.voc", encoding="ISO-8859-1") as f:
        lines = f.readlines()

        for line in lines:
            sentence = line.split()
            vocaDict[sentence[1]] = sentence[0]

    print(vocaDict)
    line_list = []

    with open("./w2v_sig_norm.index", encoding="ISO-8859-1") as f:
        lines = f.readlines()

        for line in lines:
            sentence = line.split()
            paper_score = {}
            paper_score["word"] = sentence[0]
            paper_score["paper"] = sentence[1]
            paper_score["score"] = sentence[2]
            line_list.append(paper_score)

    # print(list)
    word_list = []
    output = open('result_norm', 'w+');
    with open(file_name, encoding="ISO-8859-1") as f:
        lines = f.readlines()
        index = 0
        line_cnt = 0
        for line in lines:
            index += 1
            print(index)
            sentence = line.split()
            id = sentence[0]
            sentence.remove(sentence[0])
            for word in sentence:
                word_list.append(word)

            # print(word_list)
            score_dict = {}
            for word in word_list:
                if word in vocaDict.keys():
                    voca_num = vocaDict[word]

                    for paper in line_list:
                        if paper["word"] == voca_num:
                            if paper["paper"] in score_dict.keys():
                                score_dict[paper["paper"]] += float(paper["score"])
                                # print(voca_num+":"+paper["score"])
                            else:
                                score_dict[paper["paper"]] = float(paper["score"])
                                # print(voca_num + ":" + paper["score"])
                else:
                    continue

            # print(score_dict)
            sorted_x = list(sorted(score_dict.items(), key=operator.itemgetter(1)))
            sorted_x.reverse()
            sorted_x_idx = {}
            sorted_x_item = sorted_x

            for i in range(len(sorted_x)):
                item = sorted_x_item[i]
                sorted_x_idx[item[0]] = [item[1], i]
            if id in score_dict.keys():
                print("iter_cnt: {}, id: {}, rank: {}".format(line_cnt, id,
                                                              sorted_x_idx[id][1]) + " : " + str(result_of_weighted_sum(
                    score_dict, id)))
                print(id + " " + str(result_of_weighted_sum(score_dict, id)))
                output.write(id + " " + str(result_of_weighted_sum(score_dict, id)))
                output.write("\n")

        line_cnt += 1


