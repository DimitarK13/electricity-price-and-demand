import kagglehub # type: ignore
import pandas as pd
import os

path = kagglehub.dataset_download(
    "aramacus/electricity-demand-in-victoria-australia", output_dir='./data/raw'
)

print("Dataset downloaded to:", path)

df = pd.read_csv(os.path.join(path, "complete_dataset.csv"))

print(df.head())