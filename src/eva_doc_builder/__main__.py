import os

import click

from eva_doc_builder.utils import load_yaml, load_models
from eva_doc_builder.template_engine import render_template

GH_PATH = "https://github.com/pkucmus/EVA/tree/master/"


@click.group()
@click.pass_context
@click.argument("data_file_path", type=click.Path(exists=True))
def cli(ctx, data_file_path):
    ctx.obj = {"data_file_path": data_file_path}
    raw_data = load_yaml(data_file_path=ctx.obj["data_file_path"])
    ctx.obj["data"] = load_models(raw_data)


@cli.command()
@click.pass_context
@click.argument("docs_dir", type=click.Path(exists=True))
def render_all(ctx, docs_dir):
    data = ctx.obj["data"]

    render_template(
        "printed_parts.md.template",
        os.path.join(docs_dir, "printed_parts.md"),
        {"parts": data["parts"]},
    )

    for name, sub_assembly in data["sub_assemblies"].items():
        render_template(
            "sub_assembly.md.template",
            os.path.join(docs_dir, "sub_assemblies", f"{sub_assembly.name}.md"),
            {"sub_assembly": sub_assembly},
        )

    for name, assembly in data["assemblies"].items():
        render_template(
            "assembly.md.template",
            os.path.join(docs_dir, "assemblies", f"{assembly.name}.md"),
            {"assembly": assembly},
        )
