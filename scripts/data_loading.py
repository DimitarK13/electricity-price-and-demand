import kagglehub # type: ignore

path = kagglehub.dataset_download(
    "aramacus/electricity-demand-in-victoria-australia", output_dir='./data/raw'
)

print("Dataset downloaded to:", path)
