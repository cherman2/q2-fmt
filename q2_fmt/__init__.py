# ----------------------------------------------------------------------------
# Copyright (c) 2022-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._version import get_versions
from ._engraftment import engraftment, group_timepoints

__version__ = get_versions()['version']
del get_versions

__all__ = ['engraftment', 'group_timepoints']
