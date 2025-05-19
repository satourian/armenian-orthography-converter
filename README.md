# Armenian orthography converter

[![Bower](https://img.shields.io/bower/v/armenian-orthography-converter.svg?style=flat-square)](https://github.com/instigatetcf/armenian-orthography-converter/)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square)](https://github.com/instigatetcf/armenian-orthography-converter/blob/master/LICENSE)

## Set up

Use following command to load node packajes

    npm install

## Install

    bower install armenian-orthography-converter

## Python usage

This repository now includes a Python implementation.

```python
from py import converter

modern = "Աղբյուրներ"
traditional = converter.soviet_to_mashtots(modern)
```

## Run Python tests

Run the unit tests with:

```bash
python -m unittest discover py/tests
```

## Grunt tasks

Use following command to check code quality

    grunt tslit

Use following command to build project (it will create dest/mashtots.min.js file)

    grunt build
