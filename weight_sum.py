import csv


def result_of_weighted_sum(NPM_score_list, ground_truth):
    # input:
    # NPM_score_list = list of (clusterid, NPM_score) for every clusterid
    # ground_truth = True cited paper's cluster_id

    citation = dict()
    with open('cluster_num__count_final') as f:
        reader = csv.reader(f)
        for cluster_id, cit in reader:
            citation[cluster_id] = int(cit)

    score_list = list()
    for cluster_id, NPM_score in NPM_score_list.items():

        score_list.append((cluster_id, float(NPM_score), citation[cluster_id]))

    ranking_list = list()
    for weight in range(10):

        paper_rank = list()
        for paper in score_list:
            # create weighted_ranking list for given weight
            weighted_score = paper[1] + (0.1 * weight) * paper[2]
            paper_rank.append((weighted_score, paper[0]))

        paper_rank.sort()
        paper_rank.reverse()
        rank = get_rank(str(ground_truth), paper_rank)
        ranking_list.append(rank)

    return ranking_list


def get_rank(ground_truth, paper_rank):
    i = 0
    for score, cluster_id in paper_rank:
        if ground_truth == cluster_id:
            return i
        else:
            i += 1