"""Stream type classes for tap-estr."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_estr.client import TapEstrStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class EstrLatest(TapEstrStream):
    """To fetch the latest €STR"""

    name = "latest"
    path = "/latest"
    primary_keys: t.ClassVar[list[str]] = ["date"]
    schema = th.PropertiesList(
        th.Property("date", th.StringType),
        th.Property("value", th.NumberType),
    ).to_dict()
