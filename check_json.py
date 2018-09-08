import json

json_path = './data/dblp.json'
json_path = './data/dblp_sample.json'

with open(json_path) as f:
    dblp = json.load(f)



x = [pub for pub in dblp if ('crossref' in pub and len(pub['crossref']) > 1)]
x
