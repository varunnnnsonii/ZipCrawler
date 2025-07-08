import zipfile
from pathlib import PurePath

def list_folders_only(zip_path):
    folders = set()
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for entry in zip_ref.namelist():
            path = PurePath(entry)
            parts = path.parts

            # Skip if it's a file at the root
            if len(parts) <= 1:
                continue

            # Add folder paths (exclude files)
            for i in range(1, len(parts)):
                folder_path = "/".join(parts[:i])
                if not parts[i-1].lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                    folders.add(folder_path)

    # Print in a nice tree-like format
    for folder in sorted(folders):
        indent_level = folder.count('/')
        print("    " * indent_level + "└── " + folder.split('/')[-1])

# Your zip file path
zip_path = "your_zip_file.zip"
list_folders_only(zip_path)
