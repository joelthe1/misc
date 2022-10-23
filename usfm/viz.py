from pprint import pprint

is_in_block = True
block = {}
markers = {}
with open("usfm.sty") as sty_file:
    for idx, line in enumerate(sty_file):
        line = line.strip()
        # print(line)
        if line.startswith("#"):
            continue

        if len(line) == 0 and is_in_block:
            is_in_block = False
            if len(block) > 0:
                block["index_number"] = idx
                markers[block["Marker"]] = block
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
    nodes_file.write("id,marker,styleType,rank\n")
    relations_file.write("startId,endId\n")
    for marker, props in markers.items():
        rank = ""
        if "Rank" in props:
            rank = props["Rank"]
        nodes_file.write(
            f"{props['index_number']},{props['Marker']},{props['StyleType']},{rank}\n"
        )
        if "OccursUnder" in props:
            for m in props["OccursUnder"].split():
                relations_file.write(
                    f"{markers[m]['index_number']},{props['index_number']}\n"
                )

# with open("output.mermaid", "w") as mermaid_file:
#     for marker in markers:
#         if "OccursUnder" not in marker:
#             mermaid_file.write(f"{marker['Marker']}\n")
#         else:
#             for m in marker["OccursUnder"].split():
#                 mermaid_file.write(f"{m} --> {marker['Marker']}\n")
