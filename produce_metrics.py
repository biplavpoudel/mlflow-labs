from mlflow import log_metric
from random import choice

if __name__ == "__main__":
    metric_names = ["cpu"]
    percentages = [i for i in range(0, 100)]

    for i in range(400):
        log_metric("cpu", choice(percentages))