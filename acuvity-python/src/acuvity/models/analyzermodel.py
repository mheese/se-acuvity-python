"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from acuvity.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AnalyzermodelTypedDict(TypedDict):
    r"""Represent an analyzer model."""

    name: NotRequired[str]
    r"""The name of the model."""
    revision: NotRequired[str]
    r"""The revision of the model."""


class Analyzermodel(BaseModel):
    r"""Represent an analyzer model."""

    name: Optional[str] = None
    r"""The name of the model."""

    revision: Optional[str] = None
    r"""The revision of the model."""