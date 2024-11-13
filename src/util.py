import glob

def get_files_from_dir(dir_path: str) -> list:
    return glob.glob(f"{dir_path}/*.pcap*")

def hex_to_bin(hex_str: str) -> str:
    pass

def save_file(file_path: str, data: dict):
    pass