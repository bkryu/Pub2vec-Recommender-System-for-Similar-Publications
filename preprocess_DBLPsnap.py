import snap
import json
# This file edgelists from the DBLP citation dataset

num_lines = 10
all_lines = 4107340
one_percent = int(0.01*all_lines)


#Initialize empty arrays and dictionaries
Graph = snap.PNGraph.New()
id_map = dict()
inv_id_map = dict()
id_count = 0

# Read file line by line. File is too big so cannot read all the file at once.
print("Reading nodes...")
# json_file = open('dblp_cleaned.txt','r')
json_file = open('dblp_papers_v11.txt','r')
counter = 0
for line in json_file:
	d = json.loads(line)
	if (counter % one_percent == 0):
		print("Completed %d percent of processing...\r" %int(counter/one_percent))

	id_count += 1
	id_map[int(d["id"])] = id_count

	inv_id_map[id_count] = int(d["id"])
	# if ("authors" in d.keys() and "year" in d.keys()) and "n_citation" in d.keys():
	# 	inv_id_to_authors[id_count] = len(d["authors"])
	# 	inv_id_to_year[id_count] = int(d["year"])
	# 	inv_id_to_citations[id_count] = int(d["n_citation"])
	Graph.AddNode(id_count)
	
	counter += 1

json_file.close()


print("Reading edges...")
# json_file = open('dblp_cleaned.txt','r')
json_file = open('dblp_papers_v11.txt','r')
counter = 0
for line in json_file:
	d = json.loads(line)
	if (counter % one_percent == 0):
		print("Completed %d percent of processing...\r" %int(counter/one_percent))

	curr_id = int(d["id"])
	curr_map_id = id_map[curr_id]
	if "references" in d:
		refs = d["references"]
		for item in refs:
			target_idx = int(item)
			target_map_idx = id_map[target_idx]
			Graph.AddEdge(curr_map_id, target_map_idx)
	
	counter += 1

print("Saving snap graph file...")
snap.SaveEdgeList(Graph, 'dblp_snapgraph.txt')

# Create mapping from DBLP ID to SNAP graph ID and vice versa
json_file = json.dumps(id_map)
f = open("id_map.json","w")
f.write(json_file)
f.close()

json_file = json.dumps(inv_id_map)
f = open("inv_id_map.json","w")
f.write(json_file)
f.close()

