import os

import mlflow
from mlflow import log_metric, log_param,log_artifacts

if __name__ == "__main__":
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run():
        log_param("threshold", 3)
        log_param("verbosity", "DEBUG")

        log_metric("timestamps", 1000)
        log_metric("TTC", 33)

        log_artifacts(local_dir=os.getcwd(), artifact_path="data/census.csv")