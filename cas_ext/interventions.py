"""Closed-form, optional block-level interventions for diagnostics."""

from __future__ import annotations

from typing import Mapping, Sequence


def apply_block_bias(logits: Sequence[float], block_ids: Sequence[str | None], bias_by_block: Mapping[str, float]) -> list[float]:
    if len(logits) != len(block_ids):
        raise ValueError("logits and block_ids must have equal length")
    return [value + float(bias_by_block.get(block_id, 0.0)) if block_id is not None else value for value, block_id in zip(logits, block_ids)]
