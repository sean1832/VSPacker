# VSPacker

Packer is a tool for packaging c# projects into a distributable zip file. It is designed to be used in a Post Build event in Visual Studio.

## Usage

```python
import vspacker.package_builder as builder

def main():
    project_directory = "path/to/project/dir"
    project_file = "path/to/project.csproj"
    bd = builder.AssemblyBuilder(project_directory, project_file)
    bd.build_zip(
        zip_filename=f"{bd.project_name}_v{bd.version}.zip",
        exclude_patterns=["RhinoCommon.dll", "Grasshopper.dll", "*.lic"],
        include_files=["LICENSE", "README.md"],
    )
    bd.package_example("example.gh")

if __name__ == "__main__":
    main()
```

