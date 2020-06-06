# EVA MGN Carriage Platform


![](https://github.com/pkucmus/EVA/blob/master/docs/assets/images/lineup.png)

I present to you the EVA carriage platform - easy to mount, remix and use MGN carriages for different Hotend assemblies.

They work great with the [Rat Rig V-core Pro](https://www.ratrig.com/3d-printing-cnc/3d-printer-kits/complete-kits/rat-rig-v-core-pro-linear-rail-701.html) "Easy mod" I created: https://github.com/pkucmus/Easy-Mod

A rather poor attempt to talk about those: https://www.youtube.com/playlist?list=PLR8LTCniA766Mg1a88iF8xhOlvZR-Rc3A

## Instructions

Visit the [project page](https://pkucmus.github.io/EVA/) for instructions and more information.

## Contribution

If you want to help with testing - please grab a carriage and report your findings as an [issue](https://github.com/pkucmus/EVA/issues) - please include pictures, videos and your opinion.

If you see anything missing from the Instructions - please file an [issue](https://github.com/pkucmus/EVA/issues).

### Generating the documentation

Python3.8 required with Poetry.

```bash
poetry install
```

To generate gifs:

```python
from generate import genearate_gifs_from_directory

genearate_gifs_from_directory("assets/images/gifs/source", {"id": "v6_titan"})
```

To serve the gh-page locally:

```bash
mkdocs serve
```

To deploy gh page:

```bash
mkdocs gh-deploy
```
