import argparse
import os

from vspacker import package_builder as builder


def parse_args():
    parser = argparse.ArgumentParser(description="Package files to zip")
    parser.add_argument("project_file", help="project file")
    return parser.parse_args()


def main():
    args = parse_args()
    project_file = args.project_file
    solution_root = os.path.dirname(os.path.dirname(project_file))
    example_file = os.path.join(solution_root, "Example/grasshopper", "portal-example.gh")

    proj = builder.AssemblyBuilder(project_file)
    proj.build_zip(
        input_dir = os.path.join(proj.project_dir, "bin", "release", "net48"),
        zip_filename=f"{proj.project_name}-{proj.version}.zip",
        exclude_patterns=["RhinoCommon.dll", "Grasshopper.dll", "*.xml", "*.pdb"],
        include_files=["LICENSE", "README.md"],
    )
    proj.build_folder(
        dir_paths=[os.path.join(solution_root, "Example")],
        folder_name="examples",
        exclude_patterns=["*.gh", "*.3dm"],
        include_files=["LICENSE", "README.md", "icon.png", "manifest.json"],
    )

    proj.copy_file(
        example_file,
        os.path.join(proj.output_folder, "examples"),
        rename=f"{proj.project_name}-example-{proj.version}.gh" # optional
    )


if __name__ == "__main__":
    main()
