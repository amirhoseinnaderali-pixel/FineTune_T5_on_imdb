import json
from pathlib import Path


def test_historical_results_are_parseable():
    path = Path('results/historical/t5_imdb_historical.json')
    rows = json.loads(path.read_text())
    assert len(rows) == 10
    assert all(0.0 < row[2] < 1.0 for row in rows)
    assert {row[0] for row in rows} == {'full_finetuning','soft_prompt','adapter','adapterhub','lora'}