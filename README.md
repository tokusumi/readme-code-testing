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
    return "world"
```

See with [src/helloworld.py]() as:


* Synchronized code.
* Highlighting code in readme.
* Not affected code rendering.

And notice that nothing to do re-embedding new/modified code. This action overrides code if you change code in external file.


### Multiple use

You might add one file path (ex. [src/mul.py]()) for multiple code blocks:


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

