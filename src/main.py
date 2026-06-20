from pipelines.oulad_pypeline import bulk_copy_runner
from util.custom_path import get_path_to_csv

if __name__ == "__main__":
    file  = get_path_to_csv("test.csv")
    print(file)
    bulk_copy_runner()

