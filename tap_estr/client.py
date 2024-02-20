"""REST client handling, including TapEstrStream base class."""

from __future__ import annotations

import sys
from typing import Any, Callable, Iterable

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class TapEstrStream(RESTStream):
    """TapEstr stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root"""
        return "https://api.estr.dev"

    records_jsonpath = "$[*]"
