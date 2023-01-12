"""Les docstrings sont une façon de documenter son code (fonctions et modules en général). Il existe 3 formats de docstrings : Epytext, reST et le format 
Google.
"""

# format Epytext

"""Docstring de style Epytext

@param param1: un premier paramètre
@param param2: un deuxième paramètre
@returns: description de ce qui est retourné
"""

# format reST

"""Docstring de style reST

:param param1: un premier paramètre
:param param2: un deuxième paramètre
:returns: description de ce qui est retourné
"""

# format Google (le plus lisible)

"""Docstring de style Google

Args:
    param param1: un premier paramètre
    param param2: un deuxième paramètre

Returns:
    Description de ce qui est retourné
"""

import sys
from pprint import pprint

pprint(sys.path)