# Research Audit — T5 Efficient Adaptation on IMDB

## Scope
This audit uses the five stored notebooks and their saved outputs. No new training run is claimed.

## Research question
> How much sentiment-classification performance can be retained while reducing the number of trainable parameters and adaptation cost?

## Historical evidence
| Method | Best stored accuracy | Metric | Total parameters shown | LR |
|---|---:|---|---:|---:|
| Full fine-tuning | 90.0% | valid_acc | 60,506,624 | 1e-5 |
| Soft Prompt variant 1 | 87.1% | valid_acc | 60,511,744 | 0.1 |
| Soft Prompt variant 2 | 84.8% | valid_acc | 60,511,744 | 0.1 |
| Soft Prompt variant 3 | 86.6% | valid_acc | 60,511,744 | 0.1 |
| Adapter | 90.6% | valid_acc | 60,611,168 | 1e-3 |
| AdapterHub variant 1 | 90.4% | valid_acc | not captured | 1e-4 |
| AdapterHub variant 2 | 89.3% | valid_acc | not captured | 1e-4 |
| LoRA variant 1 | 89.5% | valid_acc | 60,801,536 | 1e-4 |
| LoRA variant 2 | 88.8% | valid_acc | 60,543,488 | 1e-4 |
| LoRA variant 3 | 88.9% | valid_acc | 60,801,536 | 1e-4 |

## Methodological findings
- The learning rate differs substantially across methods, so the historical comparison is not a clean isolation of the adaptation mechanism.
- Several methods contain multiple stored variants and must remain explicitly labelled.
- The headline outputs are labelled valid_acc; do not relabel them as test accuracy without tracing the exact output path.
- A common seed protocol is not established, so variance is unknown.
- Training time and peak GPU memory are not measured consistently.
- The project mixes custom PyTorch, OpenDelta, AdapterHub and PEFT implementations.
- Environment versions are not consistently pinned; the LoRA notebook changes PyTorch versions and records dependency conflicts.

## What this evidence establishes
The project demonstrates successful implementation and execution of several T5 adaptation approaches on IMDB with nontrivial stored validation-accuracy results.
It does not establish a universally optimal PEFT method or a clean causal comparison.

## Redesign
Future controlled runs should fix model, dataset split, preprocessing, seed, batch/effective batch, sequence length, optimization budget and evaluation protocol, then vary the adaptation mechanism.

## Next research question
> If parameter-efficient adaptation can retain task performance with a small trainable parameter budget, can the same efficiency principle be extended to preference optimization and reasoning-oriented adaptation?