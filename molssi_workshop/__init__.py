"""
molssi_workshop
A package developed in the MolSSI workshop to do... math
"""

# Add imports here
from .molssi_math import *
from .utils import title_case

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
