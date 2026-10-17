"""CPU smoke test for visibility isolation and zero-bias identity."""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cas_ext.interventions import apply_block_bias
from cas_ext.visibility import build_visibility_mask


def softmax(values):
    scale = max(values)
    exps = [math.exp(value - scale) for value in values]
    total = sum(exps)
    return [value / total for value in exps]


def main():
    mask = build_visibility_mask([0, 0, 1], ["gold", "distractor"], [2, 2], ["gold"])
    assert mask == [[True, True, False, False, True, False, False], [True, True, False, False, True, True, False], [True, True, False, False, False, False, True]], mask
    logits = [1.0, 2.0, 0.5, -1.0]
    blocks = ["gold", "gold", "distractor", None]
    assert apply_block_bias(logits, blocks, {}) == logits
    unbiased = softmax(logits)
    biased = softmax(apply_block_bias(logits, blocks, {"gold": 1.0}))
    assert biased[0] / biased[1] == unbiased[0] / unbiased[1]
    assert sum(biased[:2]) > sum(unbiased[:2])
    print("PASS visibility isolation")
    print("PASS zero-bias identity and block-share algebra")


if __name__ == "__main__":
    main()
