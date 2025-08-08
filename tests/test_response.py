from contextlib import nullcontext as does_not_raise
import pytest
import scripts.response as response
from utilities.long_responses import R_PLUTO
import re
import os


Expectation = pytest.RaisesExc | does_not_raise