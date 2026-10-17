"""Explicit per-sample visibility for packed prompt and cartridge tokens."""

from __future__ import annotations

from typing import Iterable, Sequence


def build_visibility_mask(query_seq_ids: Sequence[int], memory_block_ids: Sequence[str], memory_block_lengths: Sequence[int], visible_blocks: Iterable[str]) -> list[list[bool]]:
    if len(memory_block_ids) != len(memory_block_lengths):
        raise ValueError("block ids and lengths must have equal length")
    if any(length < 0 for length in memory_block_lengths):
        raise ValueError("block lengths must be non-negative")
    visible = set(visible_blocks)
    kv_blocks: list[str | None] = []
    for block_id, length in zip(memory_block_ids, memory_block_lengths):
        kv_blocks.extend([block_id] * length)
    kv_blocks.extend([None] * len(query_seq_ids))
    memory_len = len(kv_blocks) - len(query_seq_ids)
    mask = []
    for q_idx, q_seq_id in enumerate(query_seq_ids):
        row = []
        for kv_idx, block_id in enumerate(kv_blocks):
            if kv_idx < memory_len:
                row.append(block_id in visible)
            else:
                request_idx = kv_idx - memory_len
                row.append(request_idx <= q_idx and query_seq_ids[request_idx] == q_seq_id)
        mask.append(row)
    return mask
