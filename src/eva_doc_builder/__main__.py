import os

import click

from eva_doc_builder.utils import load_yaml, load_models, count_full_bom
from eva_doc_builder.template_engine import render_template

GH_PATH = "https://github.com/pkucmus/EVA/tree/master/"


@click.group()
@click.pass_context
@click.argument("data_file_path", type=click.Path(exists=True))
def cli(ctx, data_file_path):
    ctx.obj = {"data_file_path": data_file_path}
    raw_data = load_yaml(data_file_path=ctx.obj["data_file_path"])
    click.echo(click.style("Loding models..."))
    ctx.obj["data"] = load_models(raw_data)
    click.echo(click.style("Done"))


@cli.command()
@click.pass_context
@click.argument("docs_dir", type=click.Path(exists=True))
def render_all(ctx, docs_dir):
    data = ctx.obj["data"]

    click.echo(click.style("Rendering printed_parts.md..."))
    render_template(
        "printed_parts.md.template",
        os.path.join(docs_dir, "printed_parts.md"),
        {"parts": data["parts"]},
    )
    click.echo(click.style("Done"))

    for name, sub_assembly in data["sub_assemblies"].items():
        click.echo(click.style(f"Rendering {sub_assembly.name}..."))
        render_template(
            "sub_assembly.md.template",
            os.path.join(docs_dir, "sub_assemblies", f"{sub_assembly.name}.md"),
            {"sub_assembly": sub_assembly},
        )
    click.echo(click.style("Done"))

    for name, assembly in data["assemblies"].items():
        click.echo(click.style(f"Rendering {assembly.name}..."))
        render_template(
            "assembly.md.template",
            os.path.join(docs_dir, "assemblies", f"{assembly.name}.md"),
            {"assembly": assembly},
        )
    click.echo(click.style("Done"))
    
    click.echo(click.style("All done!", fg="green", bold=True))


@cli.command()
@click.pass_context
@click.option("--type-filter", type=str)
def count_all_bom(ctx, type_filter=None):
    data = ctx.obj["data"]
    count_full_bom(data["assemblies"], type_filter=type_filter)
