# T5 Efficient Adaptation on IMDB

This repository studies how much task performance can be retained when adapting a T5 model with different parameter-efficient mechanisms.

## Research question

> How much sentiment-classification performance can be retained while reducing the number of trainable parameters and adaptation cost?

## Methods

The original project contains:

- Full fine-tuning
- Soft Prompt
- Adapter
- AdapterHub
- LoRA

Base model: `t5-small`

Dataset: IMDB

Stored dataset sizes:
- Train: 25,000
- Test: 25,000

## Historical evidence

The notebooks contain saved runs. The strongest stored validation-accuracy values are:

| Method | Best stored validation accuracy |
|---|---:|
| Full fine-tuning | 90.0% |
| Soft Prompt | 87.1% |
| Adapter | 90.6% |
| AdapterHub | 90.4% |
| LoRA | 89.5% |

Several methods have multiple stored variants; see `results/historical/t5_imdb_historical.json`.

These numbers are **historical notebook evidence**, not controlled reproductions.

## What the historical experiment does and does not show

The notebooks demonstrate successful implementation and execution of multiple adaptation mechanisms.

However, the comparison is not fully controlled. Learning rates differ substantially across methods, multiple variants exist, random-seed control is not established, and training-time / peak-memory measurements are incomplete.

Therefore this repository does not claim a universal ranking of adaptation methods.

## Research framing

The useful object of study is the trade-off:

`task performance ↔ trainable parameters ↔ adaptation cost`

Future controlled experiments should report:

- accuracy
- macro F1
- trainable parameters
- total parameters
- trainable percentage
- training time
- peak GPU memory
- optimization steps
- environment metadata

## Reproducibility

See:

- `RESEARCH_AUDIT.md`
- `RESULTS.md`
- `REPRODUCIBILITY.md`
- `configs/research.yaml`

The original notebooks remain unchanged as historical evidence.

## Analysis

To inspect the preserved historical measurements:

```bash
python scripts/analyze_historical.py
```

The test suite includes a structural check for the preserved historical results.

## Current status

| Stage | Status |
|---|---|
| Original implementations | complete |
| Historical execution | documented |
| Scientific audit | complete |
| Historical results preserved | complete |
| Controlled reproduction | pending |
| Multi-seed evaluation | pending |
| Resource-efficiency measurement | pending |

## Next research question

> If parameter-efficient adaptation retains task performance with a small trainable parameter budget, can the same efficiency principle be extended to preference optimization and reasoning-oriented adaptation?
