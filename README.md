<p align="center">
  <a title="edaa-org.github.io/pyEDAA.ToolSetup" href="https://edaa-org.github.io/pyEDAA.ToolSetup"><img height="80px" src="doc/_static/logo.svg"/></a>
</p>

[![Sourcecode License](https://img.shields.io/pypi/l/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=Apache&label=code)](LICENSE.md)
[![Documentation License](https://img.shields.io/badge/doc-CC--BY%204.0-green?longCache=true&style=flat-square&logo=CreativeCommons&logoColor=fff)](LICENSE.md)

[![PyPI](https://img.shields.io/pypi/v/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyEDAA.ToolSetup/)
![PyPI - Status](https://img.shields.io/pypi/status/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)

[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=Libraries.io&logoColor=fff)](https://libraries.io/github/edaa-org/pyEDAA.ToolSetup)
[![Codacy - Quality](https://img.shields.io/codacy/grade/2245747238a94667b25f75970b86a333?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pyEDAA.ToolSetup)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/2245747238a94667b25f75970b86a333?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pyEDAA.ToolSetup)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/edaa-org/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=Codecov)](https://codecov.io/gh/edaa-org/pyEDAA.ToolSetup)

[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyEDAA.ToolSetup?longCache=true&style=flat-square&logo=GitHub)](https://GitHub.com/edaa-org/pyEDAA.ToolSetup/network/dependents)
[![Requires.io](https://img.shields.io/requires/github/edaa-org/pyEDAA.ToolSetup?longCache=true&style=flat-square)](https://requires.io/github/EDAA-ORG/pyEDAA.ToolSetup/requirements/?branch=main)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyEDAA.ToolSetup?longCache=true&style=flat-square)](https://libraries.io/github/edaa-org/pyEDAA.ToolSetup/sourcerank)

<p align="center">
  <a title="edaa-org.github.io/pyEDAA.ToolSetup" href="https://edaa-org.github.io/pyEDAA.ToolSetup"><img height="275px" src="doc/_static/work-in-progress.png"/></a>
</p>


# Main Goals

* Provide abstract information of where a tool is installed and configured on the local machine.
* Find local EDA tool installations and gather all necessary information in a configuration file.
* Support multiple versions and variants of the same tool.
* In case of multiple tool versions/variants select one default installation.
* Allow switching the default version/variant.
* Allow reading and writing such a configuration file via API.
* Allow reading and writing such a configuration file via CLI.


# Features

* Find tool installations:
  * at default installation locations (based on operating system).
  * in `PATH`.
  * via environment variables.
* Support multiple versions of the same tool.  
  E.g. Vivado 2018.3, 2021.2
* Support multiple variants of the same tool.  
  E.g. ModelSim Altera Edition vs. ModelSim SE vs. QuestaSim
* Configuring a default version/variant per tool.


# Condensed View on `ToolInformation` Class

```python
from pathlib import Path
from pyTooling.Decorators import export

@export
class ToolInformation:
  def __init__(self, installationDirectory: Path, binaryDirectory: Path, version: str = None, edition: str = None): ...

  @property
  def InstallationDirectory(self) -> Path:
    return self._installationDirectory

  @property
  def BinaryDirectory(self) -> Path:
    return self._binaryDirectory

  @property
  def Version(self) -> str:
    return self._version

  @property
  def Edition(self) -> str:
    return self._edition
```


# Examples

```python
from pathlib import Path
from pyEDAA.ToolSetup import Installations

yamlFile = Path("configuration.yml")

installation = Installations(yamlFile)
activeHDL = installation.Aldec.ActiveHDL
activeHDLVersion = activeHDL["10.3"]
print(activeHDLVersion.BinaryDirectory)
```


# References

* [Paebbels/pyIPCMI: pyIPCMI/Simulator/GHDLSimulator.py](https://github.com/Paebbels/pyIPCMI/blob/0f91e26f989ca025c9380ff808d1e532614b9593/pyIPCMI/ToolChain/GHDL.py#L70)

# Contributors

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)
* [Martin Zabel](https://github.com/mzabeltud)
* [Unai Martinez-Corral](https://github.com/umarcor)
* [and more...](https://github.com/edaa-org/pyEDAA.ToolSetup/graphs/contributors)


# License

This Python package (source code) is licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).

---
SPDX-License-Identifier: Apache-2.0
