.. include:: shields.inc

.. image:: _static/logo.svg
   :height: 90 px
   :align: center
   :target: https://GitHub.com/edaa-org/pyEDAA.ToolSetup

|br|

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:ToolSetup-github| |SHIELD:svg:ToolSetup-src-license| |SHIELD:svg:ToolSetup-ghp-doc| |SHIELD:svg:ToolSetup-doc-license| |SHIELD:svg:ToolSetup-gitter|
   |  |SHIELD:svg:ToolSetup-pypi-tag| |SHIELD:svg:ToolSetup-pypi-status| |SHIELD:svg:ToolSetup-pypi-python|
   |  |SHIELD:svg:ToolSetup-gha-test| |SHIELD:svg:ToolSetup-lib-status| |SHIELD:svg:ToolSetup-codacy-quality| |SHIELD:svg:ToolSetup-codacy-coverage| |SHIELD:svg:ToolSetup-codecov-coverage|

.. Disabled shields: |SHIELD:svg:ToolSetup-lib-dep| |SHIELD:svg:ToolSetup-req-status| |SHIELD:svg:ToolSetup-lib-rank|

.. only:: latex

   |SHIELD:png:ToolSetup-github| |SHIELD:png:ToolSetup-src-license| |SHIELD:png:ToolSetup-ghp-doc| |SHIELD:png:ToolSetup-doc-license| |SHIELD:svg:ToolSetup-gitter|
   |SHIELD:png:ToolSetup-pypi-tag| |SHIELD:png:ToolSetup-pypi-status| |SHIELD:png:ToolSetup-pypi-python|
   |SHIELD:png:ToolSetup-gha-test| |SHIELD:png:ToolSetup-lib-status| |SHIELD:png:ToolSetup-codacy-quality| |SHIELD:png:ToolSetup-codacy-coverage| |SHIELD:png:ToolSetup-codecov-coverage|

.. Disabled shields: |SHIELD:png:ToolSetup-lib-dep| |SHIELD:png:ToolSetup-req-status| |SHIELD:png:ToolSetup-lib-rank|


The pyEDAA.ToolSetup Documentation
##################################

EDA tool detection, configuration and selection layer.

.. image:: _static/work-in-progress.png
   :height: 275 px
   :align: center
   :target: https://GitHub.com/edaa-org/pyEDAA.ToolSetup

|br|


.. _goals:

Main Goals
**********

* Provide abstract information of where a tool is installed and configured on the local machine.
* Find local EDA tool installations and gather all necessary information in a configuration file.
* Support multiple versions and variants of the same tool.
* In case of multiple tool versions/variants select one default installation.
* Allow switching the default version/variant.
* Allow reading and writing such a configuration file via API.
* Allow reading and writing such a configuration file via CLI.


.. _features:

Features
********

* Find tool installations:

  * at default installation locations (based on operating system).

  * in ``PATH``.

  * via environment variables.

* Support multiple versions of the same tool.
  E.g. Vivado 2018.3, 2021.2

* Support multiple variants of the same tool.
  E.g. ModelSim Altera Edition vs. ModelSim SE vs. QuestaSim

* Configuring a default version/variant per tool.


.. _CONTRIBUTORS:

Contributors
************

* `Patrick Lehmann <https://GitHub.com/Paebbels>`__ (Maintainer)
* `Martin Zabel <https://GitHub.com/https://github.com/mzabeltud>`__
* `Unai Martinez-Corral <https://GitHub.com/umarcor>`__
* `and more... <https://GitHub.com/edaa-org/pyEDAA.ToolSetup/graphs/contributors>`__


.. _LICENSE:

License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


.. toctree::
   :hidden:

   Used as a layer of EDA² ➚ <https://edaa-org.github.io/>

.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency

.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Main Documentation
   :hidden:

   DataModel
   YAML

.. raw:: latex

   \part{References}

.. toctree::
   :caption: References
   :hidden:

   pyEDAA.ToolSetup/index

.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   Coverage Report ➚ <coverage/index>
   Static Type Check Report ➚ <typing/index>
   License
   Doc-License
   Glossary
   genindex
.. #
   py-modindex
