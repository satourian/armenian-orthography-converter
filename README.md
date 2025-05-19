# Armenian Orthography Converter (Python)

This project converts text between the Soviet orthography and the classical Mashtots orthography of the Armenian language.  All previous JavaScript code has been removed in favour of a pure Python implementation.

## Requirements

- Python 3.8+

## Usage

### Library

```python
from py import converter

text = "Աղբյուրներ"
print(converter.soviet_to_mashtots(text))
```

### Command line

A simple command line interface is provided.  Use `--direction` to select the conversion direction.

```bash
python -m py.cli --direction to_mashtots INPUT.txt OUTPUT.txt
```

Options:
- `--direction` – either `to_mashtots` or `to_soviet`.
- `--show-path` – print each intermediate transformation.

## Running the tests

```bash
python -m unittest discover py/tests
```

## License

This project is distributed under the terms of the GNU GPL v3.
