from pathlib import Path


class Part:
    def __init__(
        self,
        name: str,
        type: str,
        path: Path = None,
        url: str = None,
        print_settings: dict = None,
    ):
        self.name = name
        self.path = path
        self.type = type
        self.url = url
        self.print_settings = print_settings

    def __repr__(self):
        return f"Part: {self.name}"


class PartUsage:
    def __init__(self, part: Part, qty: int, required: bool = True):
        self.part = part
        self.qty = qty
        self.required = required

    def __repr__(self):
        return f"PartUsage: {self.part}, qty: {self.qty}"


class SubAssembly:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        self.parts_usage = []

    def add_part_usage(self, part_usage: PartUsage):
        self.parts_usage.append(part_usage)

    def __repr__(self):
        return f"SubAssembly: {self.name}"


class Assembly:
    def __init__(self, name: str, display_name: str, description: str = None):
        self.name = name
        self.display_name = display_name
        self.description = description
        self.sub_assemblies = []
        self.parts_usage = {}

    def add_part_usage_from_sub_assembly(self, parts_usage):
        for sub_assembly_part_usage in parts_usage:
            if sub_assembly_part_usage.part.name in self.parts_usage:
                self.parts_usage[
                    sub_assembly_part_usage.part.name
                ].qty += sub_assembly_part_usage.qty
            else:
                self.parts_usage[
                    sub_assembly_part_usage.part.name
                ] = PartUsage(sub_assembly_part_usage.part, sub_assembly_part_usage.qty)

    def add_sub_assembly(self, sub_assembly: SubAssembly):
        self.sub_assemblies.append(sub_assembly)
        self.add_part_usage_from_sub_assembly(
            sub_assembly.parts_usage
        )

    def __repr__(self):
        return f"Assembly: {self.name}"
