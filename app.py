import json
import requests
import csv


token = open('genes.txt','r')
linestoken=token.readlines()
tokens_column_number = 2
resulttoken=[]
for x in linestoken:
    resulttoken.append(x.split()[tokens_column_number])
token.close()
ids = resulttoken[1:]

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id={}&retmode=json"

for id in ids:
    conditions = []
    genes = []
    site = url.format(id)
    print(id)
    res = requests.get(site).content
    output = json.loads(res)
    for key in output["result"][id]:
        if "gene_sort" not in key:
            conditions.append("NA")
        else:
            genes.append(output["result"][id]["gene_sort"])
            for i in output["result"][id]["trait_set"]:
                conditions.append(i["trait_name"])
    print(genes)
    print(conditions)


