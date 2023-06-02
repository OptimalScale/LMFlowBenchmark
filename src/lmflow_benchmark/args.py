#!/usr/bin/env python
# coding=utf-8
"""This script defines common arguments.
"""

from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class BenchmarkingArguments:
    dataset_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "benchmark dataset name provided by lmflow"
        },
    )
    lm_evaluation_metric: Optional[str] = field(
        default="accuracy",
        metadata={
            "help": "the metric the model will be evaluated on",
            "choices": ["acc", "acc_norm", "bleu", "chrf", "em", "f1", "ppl", \
                "ter", "r@1", "r@2", "mrr", "mc1", "mc2", "word_perplexity", \
                    "byte_perplexity", "bits_per_byte"],
        },
    )
