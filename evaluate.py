"""Evaluate a submission for the SWAG dataset."""

import json
import logging

import click
import pandas as pd


logger = logging.getLogger(__name__)


@click.command()
@click.argument(
    'predictions_path', metavar='PREDICTIONS',
    type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument(
    'labels_path', metavar='LABELS',
    type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument(
    'metrics_path', metavar='METRICS',
    type=click.Path(exists=False, file_okay=True, dir_okay=False))
def evaluate(predictions_path, labels_path, metrics_path):
    """Write metrics for PREDICTIONS on LABELS to METRICS.

    Compute performance metrics for PREDICTIONS on LABELS and write
    the results to METRICS. PREDICTIONS should be the path to a file
    of predictions on SWAG data formatted as a CSV with a 'pred'
    column giving the prediction as an integer. LABELS should be the
    path to a file of labels on the SWAG data formatted as a CSV with
    a 'label' column giving the label as an integer. METRICS should be
    the path to which the metrics will be written.
    """
    with click.open_file(predictions_path, 'r') as predictions_file:
        predictions = pd.read_csv(predictions_file)['pred']

    with click.open_file(labels_path, 'r') as labels_file:
        labels = pd.read_csv(labels_file)['label']

    # compute number of correct predictions
    correct = predictions == labels
    successes = correct.sum()
    n = len(correct)
    p = successes / n

    # compute an Agresti-Coull confidence interval for the accuracy
    z = 1.96
    n_hat = n + z ** 2
    p_hat = (successes + z ** 2 / 2) / n_hat
    err = z * ((p_hat * (1 - p_hat) / n_hat) ** 0.5)
    hi = p_hat + err
    lo = p_hat - err

    # write the metrics to disk
    metrics = {
        'accuracy': p,
        'accuracy_hi_95': hi,
        'accuracy_lo_95': lo
    }
    with click.open_file(metrics_path, 'w') as metrics_file:
        json.dump(metrics, metrics_file)


if __name__ == '__main__':
    evaluate()
