import zipfile
import shutil

# Paths inside the ZIP archive
input_image = "processed_dataset_zip/processed_dataset/image_gan_in_final/99.png"
output_image = "processed_dataset_zip/processed_dataset/image_gan_out_final/99.png"

# Output destination paths
input_image_path = "/mnt/c/Users/VARUN/Downloads/archive/processed_dataset_zip/processed_dataset/input.png"
output_image_path = "/mnt/c/Users/VARUN/Downloads/archive/processed_dataset_zip/processed_dataset/output.png"

# Path to the ZIP archive
zip_path = "/mnt/c/Users/VARUN/Downloads/archive.zip"

# Extract just the required files
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Extract input image to memory and save
    with zip_ref.open(input_image) as src_file, open(input_image_path, 'wb') as dest_file:
        shutil.copyfileobj(src_file, dest_file)
        print(f"✅ Saved: {input_image_path}")
    
    # Extract output image to memory and save
    with zip_ref.open(output_image) as src_file, open(output_image_path, 'wb') as dest_file:
        shutil.copyfileobj(src_file, dest_file)
        print(f"✅ Saved: {output_image_path}")
