from beet import Context
from bolt import Runtime

def beet_default(ctx: Context):
    ctx.require(Runtime)

    # The bolt files in src/data/rb/functions will be auto-discovered
