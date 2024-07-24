# Visual Studio Post Build Event

This is an example to be used in a Visual Studio Post Build event. This example assume project structure:
```
project/
    scripts/
        pack.bat
        package.py
        requirements.txt
            -> vspacker
    project/
        project.csproj
    project.sln
```


### Pack in Debug and Release configurations
```bash
call $(SolutionDir)scripts/pack.bat $(ProjectDir) $(ProjectPath)
```

### Only pack in Release configuration
```bash
if $(ConfigurationName) == Release call $(SolutionDir)scripts/pack.bat $(ProjectDir) $(ProjectPath)
```
