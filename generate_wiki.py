import os
import subprocess
import shlex
import shutil

import jinja2
import yaml
import markdown_table


TEMPLATE_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))


def generate_gif(gif_path, path):
    dir_list = os.listdir(path)
    dir_list.sort()
    command = f"convert -dispose previous -delay 100 -loop 0 '{path}/*.png' -coalesce -layers OptimizeTransparency '{gif_path}'"
    subprocess.call(shlex.split(command))


def resize(path, size):
    filename, ext = os.path.splitext(path)
    new_path, filename = os.path.split(filename)
    filename = os.path.join(new_path, "resized", filename)
    subprocess.call(shlex.split(f"convert '{path}' -resize {size} '{filename}{ext}'"))


def resize_all_in_directory(path, size):
    dir_list = os.listdir(path)
    try:
        os.mkdir(os.path.join(path, "resized"))
    except FileExistsError:
        pass
    for source in dir_list:
        if os.path.splitext(source)[1] == ".png":
            resize(os.path.join(path, source), size)


def genearate_gifs_from_directory(path, carriage):
    resize_all_in_directory(os.path.join(path, carriage["id"]), "512x512")
    generate_gif(
        f"images/gifs/{carriage['id']}.gif",
        f"images/gifs/source/{carriage['id']}/resized",
    )
    shutil.rmtree(f"images/gifs/source/{carriage['id']}/resized")


def make_bom(bom_data):
    return markdown_table.render(
        ["Name", "Type", "Qty", "Notes"], [map(str, item.values()) for item in bom_data]
    )


if __name__ == "__main__":
    with open("data.yaml", "r") as data_file:
        data = yaml.safe_load(data_file)

    home_table_data = []

    for carriage in data["carriages"].values():
        # genearate_gifs_from_directory("images/gifs/source", carriage)
        template = TEMPLATE_ENV.get_template("wiki/templates/carriage.md.template")

        bom_string = make_bom(carriage["bom"])

        with open(os.path.join("wiki", f"{carriage['id']}.md"), "w") as page_file:
            page_file.write(
                template.render(
                    {
                        "base_url": data["base_url"],
                        "carriage": carriage,
                        "bom": bom_string,
                    }
                )
            )

    template = TEMPLATE_ENV.get_template("wiki/templates/home.md.template")
    with open(os.path.join("wiki", "home.md"), "w") as home_file:
        home_file.write(
            template.render(
                {"data": data}
            )
        )
