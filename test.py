import os

import mlflow
from mlflow import log_metric, log_param,log_artifacts

if __name__ == "__main__":
    mlflow.set_tracking_uri('http://localhost:5000')
    mlflow.end_run()
    with mlflow.start_run(run_name='test'):
        log_param("threshold", 3)
        log_param("verbosity", "DEBUG")

        log_metric("timestamps", 1000)
        log_metric("TTC", 33)

        log_artifacts("data")