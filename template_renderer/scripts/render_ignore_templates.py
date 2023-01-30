import jinja2

from glob import glob
from pprint import pprint


template_paths = [
    ".gcloudignore.jinja2",
    "python/Dockerfile.build.dockerignore.jinja2",
]


def render_templates(ensure_no_diff=False):
    ignore_excludes_file_name = ".ignore-excludes"
    ignore_excludes_paths = glob(f"**/{ignore_excludes_file_name}", recursive=True)

    ignore_excludes = dict()
    for path in ignore_excludes_paths:
        with open(path, "r") as f:
            content = f.read()
            key = path[: -len(ignore_excludes_file_name)]
            if key.endswith("/"):
                key = key[:-1]

            ignore_excludes[key] = content

    print("ignore_excludes:")
    pprint(ignore_excludes.keys())

    extension = ".jinja2"
    for path in template_paths:
        if not path.endswith(extension):
            raise Exception(f"Expected path {path} to be a jinja2 file")

        with open(path, "r") as f:
            template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)
            out = template.render(ignore_excludes=ignore_excludes)
            rendered_path = path[: -len(extension)]
            print("Rendering path", path, "as", rendered_path)
            if ensure_no_diff:
                with open(rendered_path, "r") as f2:
                    expected_out = f2.read()
                    if expected_out != out:
                        raise Exception(
                            """Expected no diff for {path}. Run `poetry shell` from within
            the `./template_render` project and then run `python ./template_renderer/scripts/render_ignore_templates.py`
            from the `./monorepo` project root` and commit changes."""
                        )
            else:
                with open(rendered_path, "w") as f2:
                    f2.write(out)


if __name__ == "__main__":
    render_templates()
