# Template Render Project

This is a convenience module to help generate various templates throughout our projects.

## Getting Started

Make sure poetry and python are set up through asdf via the root README.

To configure poetry and set up deps run:

```shell
template_renderer$ poetry env use python
template_renderer$ poetry env use 3.8.13
template_renderer$ poetry install
```

To use the poetry environment, run:

```shell
template_renderer$ poetry shell
```

Inside this environment, your python installation will have access to all dependencies managed by poetry.

To stop using the poetry environment, run:

```shell
(template-renderer)template_renderer$ exit
```

## Ignore templates

We generate dockerignore files for cloud builds automatically via jinja templates.

After creating the `<PROJECT_NAME>/cloudbuild.yaml` and `<PROJECT_NAME>/Dockerfile.build` files for your cloud build, follow the steps below:

1. Create a `<PROJECT_NAME>/.ignore-excludes` file with at least the following lines:

   ```shell
   !<PROJECT_NAME>/Dockerfile.build
   !<PROJECT_NAME>/Dockerfile.build.dockerignore
   !<PROJECT_NAME>/Dockerfile.build.dockerignore.jinja2
   ```

   You will also need to include any resource files that will be copied over into the image
   (e.g. If your `Dockerfile.build` includes the line `COPY --chown=0:0 /conf/scripts /opt/docker/scripts` then the `.ignore_excludes` should include `!<PROJECT_NAME>/conf/scripts/**`).

2. Create a `<PROJECT_NAME>/Dockerfile.build.dockerignore.jinja2`:

   ```shell
   # See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

   # rendered via <root>/template_renderer/scripts/render_ignore_templates.py

   # Ignore everything
   *

   # inject dep exclusions here
   {{ ignore_excludes['<PROJECT_NAME>'] }}
   ```

3. Update the `template_paths` list object inside the `./template_render/scripts/render_ignore_templates.py` with the filepath from above.

4. Run `poetry shell` from within the `template_render` project and then run `python template_renderer/scripts/render_ignore_templates.py` from the repo root.
