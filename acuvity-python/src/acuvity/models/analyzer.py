"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .analyzermodel import Analyzermodel, AnalyzermodelTypedDict
from .detector import Detector, DetectorTypedDict
from acuvity.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AnalyzerTypedDict(TypedDict):
    r"""Represents an analyzer."""

    id: NotRequired[str]
    r"""ID is the identifier of the object."""
    description: NotRequired[str]
    r"""The description of the analyzer."""
    detectors: NotRequired[List[DetectorTypedDict]]
    r"""The detectors the analyzer can use."""
    enabled: NotRequired[bool]
    r"""Tell if the analyzer is enabled by default."""
    group: NotRequired[str]
    r"""The group the analyzer belongs to."""
    models: NotRequired[List[AnalyzermodelTypedDict]]
    r"""The models used by the analyzer."""
    name: NotRequired[str]
    r"""The name of the analyzer."""
    namespace: NotRequired[str]
    r"""The namespace of the object."""
    triggers: NotRequired[List[str]]
    r"""A list of trigger or globl pattern that the analyzer will react on.
    A trigger is the detector Group and Name separated with a /.
    """


class Analyzer(BaseModel):
    r"""Represents an analyzer."""

    id: Annotated[Optional[str], pydantic.Field(alias="ID")] = None
    r"""ID is the identifier of the object."""

    description: Optional[str] = None
    r"""The description of the analyzer."""

    detectors: Optional[List[Detector]] = None
    r"""The detectors the analyzer can use."""

    enabled: Optional[bool] = None
    r"""Tell if the analyzer is enabled by default."""

    group: Optional[str] = None
    r"""The group the analyzer belongs to."""

    models: Optional[List[Analyzermodel]] = None
    r"""The models used by the analyzer."""

    name: Optional[str] = None
    r"""The name of the analyzer."""

    namespace: Optional[str] = None
    r"""The namespace of the object."""

    triggers: Optional[List[str]] = None
    r"""A list of trigger or globl pattern that the analyzer will react on.
    A trigger is the detector Group and Name separated with a /.
    """