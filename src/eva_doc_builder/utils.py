import os
from pathlib import Path
from typing import List, Dict

import yaml

from eva_doc_builder.models import (
    Assembly,
    SubAssembly,
    Part,
    PartUsage,
)


def load_yaml(data_file_path: Path):
    with open(os.path.join(data_file_path), "r") as data_file:
        data = yaml.safe_load(data_file)
    return data


def load_parts(raw_parts: dict):
    for name, data in raw_parts.items():
        yield name, Part(name=name, **data)


def load_sub_assemblies(raw_sub_assemblies, parts: Dict[str, Part]):
    for name, data in raw_sub_assemblies.items():
        sub_assembly = SubAssembly(name, data.get("description"))
        for part_usage_data in data["parts"]:
            sub_assembly.add_part_usage(
                PartUsage(
                    parts[part_usage_data["part"]], part_usage_data["qty"]
                )
            )
        yield name, sub_assembly


def load_assemblies(raw_assemblies, sub_assemblies: Dict[str, SubAssembly]):
    for name, data in raw_assemblies.items():
        assembly = Assembly(
            name=name,
            display_name=data["display_name"],
            description=data.get("description"),
        )
        for sub_assembly_data in data["sub_assemblies"]:
            assembly.add_sub_assembly(sub_assemblies[sub_assembly_data])
        yield name, assembly


def load_models(raw_data):
    parts = dict(load_parts(raw_data["parts"]))
    sub_assemblies = dict(
        load_sub_assemblies(raw_data["sub_assemblies"], parts)
    )
    assemblies = dict(load_assemblies(raw_data["assemblies"], sub_assemblies))

    return {
        "parts": parts,
        "sub_assemblies": sub_assemblies,
        "assemblies": assemblies,
    }


def count_full_bom(assemblies, type_filter=None):
    parts_usage_set = {}
    for assembly in assemblies.values():
        for parts_usage in assembly.parts_usage.values():
            if (
                type_filter is not None
                and parts_usage.part.type != type_filter
            ):
                continue
            if parts_usage.part.name not in parts_usage_set:
                parts_usage_set[parts_usage.part.name] = parts_usage
            else:
                if (
                    parts_usage.qty
                    > parts_usage_set[parts_usage.part.name].qty
                ):
                    parts_usage_set[parts_usage.part.name] = parts_usage
    import pprint

    pprint.pprint(parts_usage_set)

