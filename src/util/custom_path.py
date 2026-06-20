import os

def get_path_to_csv(csv_file: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    oudlad_dir = os.path.join(current_dir, '..', '..', 'OULAD-DATA', csv_file)
    return oudlad_dir
