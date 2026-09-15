from pathlib import Path


def read_txt_file(file_path):
    path = Path(file_path)
    return path.read_text(encoding="utf-8")
