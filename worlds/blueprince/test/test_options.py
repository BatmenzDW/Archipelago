

from . import BluePrinceTestBase
from ..options import GoalType

# This class is here for testing errors that are found during fuzzer testing
class TestOptions(BluePrinceTestBase):
    options = {
        # "goal_type": GoalType.option_tunnel
    }