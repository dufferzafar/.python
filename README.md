
<div align="center">
 <img src="logo.png" width="211" height="64">
  <p>Little functions that live in my pythonpath.</p>
</div>


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

## Functions

<!--
* [Browser Related](#browser)
* [Pretty Printing](#pretty)

### <a name="browser"></a>Browser Related
-->

**`browser.view_html`**

View an HTML string in a browser. I mostly use this along with the [`requests`](http://docs.python-requests.org/en/latest/) library to quickly view the [`response.content`](http://docs.python-requests.org/en/latest/api/#requests.Response.content).

<!-- ### <a name="pretty"></a>Pretty Printing -->

**`pretty.json`**

Pretty Print a dictionary/json in color. The idea came from [jq](http://stedolan.github.io/jq/).

_TODO:_

* Handle list inside dicts
* Print numbers in different color?
* Only print first 10 keys (sort of like head)?
* Use colorama etc packages to print in color?
* Print inner level dicts in different color?
