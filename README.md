# .python
Little functions that lie in my pythonpath.

## Installation

```bash
git clone http://github.com/dufferzafar/.python ~/.python
export PYTHONPATH=$PYTHONPATH:$HOME/.python
```

Test that it works:

```
$ python
>>> import pretty
>>> pretty.json(dict(this="should", be="in", cool="colors"))
```

To set the environment when you load your shell:

```
echo "export PYTHONPATH=$PYTHONPATH:$HOME/.python" > .bashrc
echo "export PYTHONPATH=$PYTHONPATH:$HOME/.python" > .zshrc
```

Learn more about [`PYTHONPATH`](https://docs.python.org/2/using/cmdline.html#environment-variables).
