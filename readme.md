# VSPacker

Packer is a utility library for packaging c# projects into a distributable zip file. It is designed to be used in a Post Build event in Visual Studio.

![](https://img.shields.io/pypi/v/vspacker)
![](https://img.shields.io/pypi/pyversions/vspacker
)


## Installation
```bash
pip install vspacker
```

## Usage

See the example below for a simple implementation. For more detail see [examples](./example/).

### Python Implementation

```python
import os
import vspacker.package_builder as builder


def main():
    args = parse_args()
    project_file = args.project_file
    solution_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    example_file = os.path.join(solution_root, "Example/grasshopper", "portal-example.gh")

    proj = builder.AssemblyBuilder(project_file)
    proj.build_zip(
        input_dir=os.path.join(proj.project_dir, "bin", "release", "net48"),
        zip_filename=f"{proj.project_name}-{proj.version}.zip",
        exclude_patterns=["*.xml", "*.pdb"],
        include_files=[
            (os.path.join(solution_root, "LICENSE"), "resources/LICENSE.txt"),
            os.path.join(solution_root, "README.md"),
        ],
        internal_folder=proj.project_name,
    )
    proj.copy_file(
        example_file,
        proj.output_folder,
        rename=f"{proj.project_name}-example-{proj.version}.gh",
    )


if __name__ == "__main__":
    main()
```
