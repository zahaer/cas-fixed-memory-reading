"""Small diagnostics for fixed-memory CAS experiments."""

from .interventions import apply_block_bias
from .visibility import build_visibility_mask

__all__ = ["apply_block_bias", "build_visibility_mask"]
