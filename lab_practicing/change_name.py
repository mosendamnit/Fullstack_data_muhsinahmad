from pathlib import Path
from shutil import copytree , rmtree


unclean_data_path = Path(__file__).parent / "unclean_data"
clean_data_path = Path(__file__).parent / "clean_data"


if clean_data_path.is_dir():
    rmtree(clean_data_path)


clean_data_path.mkdir(parents=True , exist_ok=True)

for folder in unclean_data_path.iterdir():
    new_name = folder.name.split()[0]
    copytree(folder , clean_data_path / new_name)