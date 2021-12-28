
from pathlib             import Path
from pyTooling.Packaging import DescribePythonPackageHostedOnGitHub

gitHubNamespace =        "edaa-org"
packageName =            "pyEDAA.Configure"
packageDirectory =       packageName
packageInformationFile = Path(f"{packageDirectory}/__init__.py")

DescribePythonPackageHostedOnGitHub(
	packageName=packageName,
	description="EDA tool detection, configuration and selection layer.",
	gitHubNamespace=gitHubNamespace,
	sourceFileWithVersion=packageInformationFile,
)
