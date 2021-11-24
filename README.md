# Readme code testing example

![Test code and embed into README](https://github.com/tokusumi/readme-code-testing/workflows/Test%20code%20and%20embed%20into%20README/badge.svg)

This repo demonstrates [Markdown Embed Code From File](https://github.com/marketplace/actions/markdown-embed-code-from-file) (GitHub Action).

This would helps testing for your code within readme (actually for markdown).

You could put code in external file and test them, as same as ordinary testing your code. You don't need copy & paste code and feel anxisous about compatibility anymore.

## Mark your code for embedding

This action could inspect your code, if you add a file path in code block as "\`\`\`lang:external/file/path.py\`\`\`".

The following code block has a file path `src/helloworld.py`:

```python:src/helloworld.py
def hello():
    return "v1.0.0 bbb world"
```

See [src/helloworld.py](./src/helloworld.py) as:

* Synchronized code.
* Highlighting code in readme.
* Not affected code rendering.

And notice that there are nothing to do re-embedding new/modified code. This action overrides code automatically if you change code in external file and commit it.

### Try it

Let's try demonstration in your repository as follows:

1. fork this repository.
1. edit [src/helloworld.py](./src/helloworld.py), create a new branch and start a pull request.
1. go to PR to check action result.
1. you can see auto updated readme at new branch you created above. (see if [above code block](#mark-your-code-for-embedding) is modified)
1. you can try again, if you edit it and commit again.

## More features
### Embedding specific lines

You might add specific lines from one file (ex. [src/mul.py](./src/mul.py)).

This action supports this with the syntax as "\`\`\`lang:external/file/path.py [start:end]\`\`\`" for it:

```py:src/mul.py [3-4]
def multiple(x):
    return pow(x, 2)
```

### Multiple use

You might add one file path (ex. [src/mul.py](./src/mul.py)) for multiple code blocks:

```py:src/mul.py
from math import pow

def multiple(x):
    return pow(x, 2)
```

It works!:

```py:src/mul.py
from math import pow

def multiple(x):
    return pow(x, 2)
```

However, the other is not available.

### Non-existent file

Notice that this action goes to "fail" if a file you add does not exist.

## Multilingual

This action could work for any programming "language".

Ideally you could write as "\`\`\`lang:external/file/path.py\`\`\`", but actually this action does not inspect "lang", just read path and copy&paste strings into target code block in markdown.

So, missing "lang" is available:

```:src/helloworld.sh
#!/bin/bash

echo "hello"
```

## Formatting

Notice that this action uses markdown parser/formatter, so, if you don't update any code, readme may be updated if formatter works.
