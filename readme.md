swag-evaluator
==============
The evaluator for the SWAG dataset in beaker.

This repository holds the code for creating the evaluator for the SWAG
dataset in beaker that powers the SWAG leaderboard.


Development
-----------
To create the evaluator blueprint:

    docker build --tag swag-evaluator .
    beaker blueprint create --name swag-evaluator swag-evaluator

To run an evaluation in an experiment: fill in `$SWAG_EVALUATOR` with
the name of the version of the SWAG evaluator you created as a
blueprint. Fill in `$SWAG_PREDICTIONS` with the predictions you
generated. Fill in `$SWAG_LABELS` with the labels for the SWAG split on
which you predicted.

    SWAG_EVALUATOR=$SWAG_EVALUATOR \
    SWAG_PREDICTIONS=$SWAG_PREDICTIONS \
    SWAG_LABELS=$SWAG_LABELS \
    beaker experiment create \
      --name='swag-evaluation' \
      --file=evaluate.yaml

To run the evaluation script locally, make sure you have the
dependencies installed from `requirements.txt` and then look at the
script's documentation using the `--help` option:

    $ python evaluate.py --help
    Usage: evaluate.py [OPTIONS] PREDICTIONS LABELS METRICS

      Write metrics for PREDICTIONS on LABELS to METRICS.

      Compute performance metrics for PREDICTIONS on LABELS and write the
      results to METRICS. PREDICTIONS should be the path to a file of
      predictions on SWAG data formatted as a CSV with a 'pred' column giving
      the prediction as an integer. LABELS should be the path to a file of
      labels on the SWAG data which should be in CSV format with a 'label'
      column giving the label as an integer. METRICS should be the path to which
      the metrics will be written.

    Options:
      --help  Show this message and exit.


Contact
-------
See [the GitHub repo][swag-evaluator-repo].


[swag-evaluator-repo]: https://github.com/allenai/swag-evaluator
