import json
from pathlib import Path

import pandas as pd


def main():
    path = Path('results/historical/t5_imdb_historical.json')
    rows = json.loads(path.read_text())
    frame = pd.DataFrame(rows, columns=['method','variant','accuracy','total_parameters','learning_rate'])
    print(frame.to_string(index=False))
    summary = frame.groupby('method', as_index=False).agg(best_accuracy=('accuracy','max'), runs=('accuracy','count'))
    print('\nDescriptive historical summary:')
    print(summary.sort_values('best_accuracy', ascending=False).to_string(index=False))


if __name__ == '__main__':
    main()