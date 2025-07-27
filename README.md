# builder-ric

`builder-ric` is a lightweight Python CLI tool for generating structured project scaffolding. It helps you quickly create Python project folders and files through a single command-line interface.

## Features
- Generate a project root with a single command
- Create nested folders and files using intuitive syntax
- Specify where the project should be built with `--path`
- Automatically adds `__init__.py` in directories containing Python files
- Clean and minimal structure for starting new projects

## Installation
### Option 1: Install via Test PyPI (Recommended for early testing)
```bash
  pip install -i https://test.pypi.org/simple/ builder-ric
```
Make sure your Python environment uses `pip` from Python 3.10+.
> **Note:** This package is currently hosted on Test PyPI and is intended for testing purposes only. Once stable, it will be released to the main PyPI index.

### Option 2: Install locally (For development)
```bash
    git clone https://github.com/captaineywick/builder_ric.git
    cd builder_ric
    pip install -e .
```
This uses pip's editable mode so any changes to the code are reflected immediately.

## Usage
The main CLI command is `ric`.

```bash
  ric <project_name> [items...] [--path <directory>]
```
* `project_name`: Name of the root folder to generate (use `.` to use the current directory)
* `items`: Folder and file definitions using a custom syntax
* `--path (optional)`: Target base directory where the project should be created. Defaults to the current directory `"."` if not provided.

### Syntax
* Create a folder: `folder_name/`
* Create nested folders: `folder1/subfolder1`
* Create files in a folder: `folder:filename1.py,filename2.py`
* Create folder, sub folder and files creation inside subfolder: `folder/subfolder:script1.py,script2.py`

### Example
```bash
  ric sample_project folder1/subfolder_1:sample_1.py,sample_2.py utils:helpers.py --path /your/target/location
```

This will generate:
```
/your/target/location/
└── sample_project/
    ├── folder1/
    │   └── subfolder_1/
    │       ├── sample_1.py
    │       ├── sample_2.py
    │       └── __init__.py
    ├── utils/
    │   ├── helpers.py
    │   └── __init__.py
    └── ...
```
> Any directory containing .py files will automatically receive an __init__.py.

## Development
To contribute:
1. Clone the repository
2. Install development dependencies:
    ```bash
      pip install -r requirements-dev.txt
    ```
3. Make changes.
4. Run tests before submitting a PR:
    ```bash
      pytest --cov-report=html
    ```

## License
MIT License. See the [LICENSE](LICENSE) file for details.

## TODO
Add tests for:
  - `app`
  - `adapters`
  - `presentation`