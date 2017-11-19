import requests


def leet():
    r = requests.get('https://leetcode.com/api/problems/all/')
    json = r.json()
    statlist = json['stat_status_pairs']
    stats = [x['stat'] for x in statlist]

    problemset = [(x['question_id'], x['question__title']) for x in stats]
    sort = sorted(problemset)

    problems = ["LeetCode {}. {}".format(p[0], p[1]) for p in sort]

    return problems
