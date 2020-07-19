import yaml
import pprint

with open("docs/data.yml") as yaml_file:
    data = yaml.safe_load(yaml_file)

subs = {}

for assembly in data["assemblies"]:
    subs[assembly] = {}
    for sub in data["assemblies"][assembly]["sub_assemblies"]: 
        for part in data["sub_assemblies"][sub]["parts"]: 
            if data["parts"][part["part"]]["type"] != "printed":
                if part["part"] in subs[assembly]: 
                    subs[assembly][part["part"]] += part["qty"] 
                elif part["part"] not in subs[assembly]: 
                    subs[assembly][part["part"]] = part["qty"]




superset = {}

for sub_parts in subs.values():
    for part, qty in sub_parts.items():
        if (part in superset and qty > superset[part]) or part not in superset:
            superset[part] = qty

pprint.pprint(superset)
