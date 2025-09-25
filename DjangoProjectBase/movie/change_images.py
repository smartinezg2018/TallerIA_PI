import os

def rename_images_with_underscores(folder_path: str):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            new_filename = filename.replace(" ", "_").lower()
            if new_filename != filename:
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
rename_images_with_underscores('../media/movie/images')