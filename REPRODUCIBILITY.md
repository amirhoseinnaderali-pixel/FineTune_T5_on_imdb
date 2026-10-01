# Reproducibility

## Historical environment

The notebooks install dependencies interactively and do not provide one complete locked environment. The LoRA notebook changes the PyTorch version and records dependency conflicts.

Treat the historical environment as approximate.

## Data

Dataset: IMDB

Stored sizes:
- train: 25,000
- test: 25,000

Future controlled experiments must use one deterministic split/evaluation protocol across all methods.

## Required metadata for new runs

Record Python, PyTorch, Transformers, PEFT, AdapterHub/Adapter-Transformers, OpenDelta, Datasets, CUDA, GPU model, git SHA and random seed.

New measurements must remain separate from historical evidence.
