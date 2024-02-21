from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_estr import streams


class TapEstr(Tap):
    """TapEstr tap class."""

    name = "tap-estr"

    def discover_streams(self) -> list[streams.TapEstrStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.EstrLatest(self),
            streams.EstrHistorical(self),
        ]


if __name__ == "__main__":
    TapEstr.cli()
