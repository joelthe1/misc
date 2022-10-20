from pprint import pprint

is_in_block = True
block = {}
markers = []
with open("usfm.sty") as sty_file:
    for line in sty_file:
        line = line.strip()
        # print(line)
        if line.startswith("#"):
            continue

        if len(line) == 0 and is_in_block:
            is_in_block = False
            if len(block) > 0:
                markers.append(block)
                block = {}

        if line.startswith("\\"):
            # print(line)
            is_in_block = True
            splits = line.split(" ", maxsplit=1)
            if len(splits) == 2:
                key, value = splits
                block[key[1:]] = value

pprint(len(markers))

with open("nodes.csv", "w") as nodes_file, open("relations.csv", "w") as relations_file:
    # Write headers
    nodes_file.write("Id,styleType,rank\n")
    relations_file.write("startId,endId\n")
    for marker in markers:
        rank = ""
        if "Rank" in marker:
            rank = marker["Rank"]
        nodes_file.write(f"{marker['Marker']},{marker['StyleType']},{rank}\n")
        if "OccursUnder" in marker:
            for m in marker["OccursUnder"].split():
                relations_file.write(f"{m},{marker['Marker']}\n")

# with open("output.mermaid", "w") as mermaid_file:
#     for marker in markers:
#         if "OccursUnder" not in marker:
#             mermaid_file.write(f"{marker['Marker']}\n")
#         else:
#             for m in marker["OccursUnder"].split():
#                 mermaid_file.write(f"{m} --> {marker['Marker']}\n")
