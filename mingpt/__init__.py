"""
Credit to karpathy for mingpt: https://github.com/karpathy/minGPT
"""
__all__ = (
    'set_seed', 'top_k_logits', 'sample', 'CausalSelfAttention', 'Block',
    'GPT', 'Trainer', 'GPTConfig', 'GPT1Config', 'TrainerConfig',
)

from mingpt.model import *
from mingpt.trainer import *
from mingpt.utils import *
