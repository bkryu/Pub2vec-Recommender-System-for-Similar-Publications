import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections

all_lines = 4107340
# all_lines = 2000
one_percent = int(0.01*all_lines)
# print("Total number of lines: %d" % all_lines)

author_citation_pairs = []
n_citations = collections.defaultdict(int)
n_authors = collections.defaultdict(int)
reference_citation_pairs = []

# nodes = set()




fos_map = dict() # Maps from Graph Node ID to FOS
fos_set = set()

name_map = dict() # Maps from Graph Node ID to Publication Name
citation_map = dict() # Maps from Graph Node ID to Citation Count

json_file = open('inv_id_map.json','r')
for line in json_file:
    inv_id_map = json.loads(line)

json_file = open('id_map.json','r')    
for line in json_file:
    id_map = json.loads(line)

print("Reading nodes...")
json_file = open('dblp_papers_v11.txt','r')
counter = 0

for line in json_file:
    d = json.loads(line)
    if (counter % one_percent == 0):
        print("Completed %d percent of processing...\r" %int(counter/one_percent))

    if "fos" in d.keys():
        if "title" in d.keys():
#             print(d['title'])
            name_map[id_map[str(d['id'])]] = d['title']
        if 'n_citation' in d.keys():
#             print(d['n_citation'])
            citation_map[id_map[str(d['id'])]] = int(d['n_citation'])

        fos_map[id_map[str(d['id'])]] = dict()
        
        fos_total = 0.0
        
        for field_d in d['fos']:
#             print(field_d['name'])
#             print(field_d['w'])
            fos_set.add(field_d['name'])
            
            fos_map[id_map[str(d['id'])]][field_d['name']] = field_d['w']
            
            fos_total += (field_d['w'])**2
            
#         print(fos_total)
        
    

    counter += 1
#     if counter > 20:
#         break
json_file.close()    


json_file = json.dumps(fos_map)
f = open("fos_map.json","w")
f.write(json_file)
f.close()

json_file = json.dumps(name_map)
f = open("name_map.json","w")
f.write(json_file)
f.close()

json_file = json.dumps(citation_map)
f = open("citation_map.json","w")
f.write(json_file)
f.close()
