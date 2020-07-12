[![Maintainability](https://api.codeclimate.com/v1/badges/950e956456b688c0886e/maintainability)](https://codeclimate.com/github/kushalkolar/MESmerize/maintainability) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Gitter](https://badges.gitter.im/mesmerize_discussion/community.svg)](https://gitter.im/mesmerize_discussion/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Mesmerize is a platform for the annotation and analysis of neuronal calcium imaging data. It encompasses the entire process of calcium imaging analysis from raw data to semi-final publication figures that are interactive, and aids in the creation of FAIR-functionally linked datasets. It is applicable for a broad range of experiments and is intended to be used by users with and without a programming background.

## News & upcoming

**July 2020**

Changes:
- Mesmerize can be installed via pip.
- Much easier to import imaging meta data from other sources.
- Create stimulus tuning curve plots.
- ΔF/F must now be extracted at the Viewer stage for caiman data, or set through other methods. Spikes and ΔF/F can be visualized in the Viewer.

**June 2020**

Version 0.2 released.

Changes:

- Windows is now supported!
- The Viewer can handle 3D data and 3D ROIs.
- For development, classes are provided for creating Volumetic ROI types, and a Volumetic ROI manager.
- Caiman 3D CNMF is supported.
- Updated CNMF(E) and motion correction modules to use the latest release of CaImAn. Parameter entry GUIs are much more flexible now.
- CNMF(E) data can be imported directly from hdf5 files from Caiman. Therefore you can use your own scripts/notebooks and existing CNMF hdf5 files for downstream analysis in Mesmerize.
- More customizable support for use of caiman modules within the Mesmerize viewer's script editor.
- Suite2p importer added, allowing you to perform downstream analysis of Suite2p output data in Mesmerize.
- Some cleanup with the batch manager
- bug fixes

*Please note that batches from v0.1 and v0.2 are not inter-compatible. Use the v0.1 branch if you need v0.1*

**Nov 2019:**

See our recent biorxiv manuscript where we use Mesmerize to analyze a calcium imaging dataset from *Ciona intestinalis* as well as other model organisms!

https://doi.org/10.1101/840488

<a href="https://doi.org/10.1101/840488">
<img src="https://www.biorxiv.org/sites/default/files/site_logo/bioRxiv_logo_homepage.png" alt="manuscript on biorxiv" width="160"/>
</a>

## Questions/Discussions

Feel free to ask questions or discuss things on gitter. For larger bugs/issues please use the issue tracker.

[![Gitter](https://badges.gitter.im/mesmerize_discussion/community.svg)](https://gitter.im/mesmerize_discussion/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


## Documentation
Documentation is available here: [http://www.mesmerizelab.org/](http://www.mesmerizelab.org/)

## Installation

If you're familiar with virtual environments and have necessary build tools, installation is as simple as:

```
pip install tslearn~=0.2.2
pip install mesmerize
```

After installation simply call ``mesmerize`` from inside the virtual environment to launch it.

If you're unfamiliar with virtual environments, see the docs for more detailed instructions on all operating systems:

http://mesmerizelab.org/user_guides/installation.html
