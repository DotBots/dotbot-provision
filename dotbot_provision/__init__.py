"""DotBot provisioning CLI package — DEPRECATED.

Folded into the unified `dotbot` package (2026-05). Migrate with:

    pip install dotbot[provision]
    dotbot testbed provision --help

This standalone package will be archived after a 6-month grace period.
See https://github.com/DotBots/PyDotBot for the consolidated tooling.
"""

import sys
import warnings

__version__ = "0.1.6"

_DEPRECATION_MESSAGE = (
    "dotbot-provision is deprecated; use `pip install dotbot[provision]` "
    "and `dotbot testbed provision ...` instead. "
    "This standalone package will be archived after 2026-11."
)

warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
# Print to stderr too — DeprecationWarning is silenced by default for end
# users running the CLI, and we want them to actually see this.
print(f"[DEPRECATION] {_DEPRECATION_MESSAGE}", file=sys.stderr)
