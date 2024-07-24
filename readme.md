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
import vspacker.package_builder as builder

def main():
    project_file = "path/to/project/project.csproj"
    bd = builder.AssemblyBuilder(project_file)
    bd.build_zip(
        zip_filename=f"{bd.project_name}_v{bd.version}.zip",
        exclude_patterns=["RhinoCommon.dll", "Grasshopper.dll", "*.lic"],
        include_files=["LICENSE", "README.md"],
    )
    bd.package_example("example.gh")

if __name__ == "__main__":
    main()
```
