import os

import jinja2


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_PATH, "templates")
TEMPLATE_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True,
)


def render_template(template_name, output_path, context):
    template = TEMPLATE_ENV.get_template(template_name)
    with open(output_path, "w") as page_file:
        page_file.write(template.render(context))
