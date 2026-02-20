import os
import urllib.parse

# Configurations
EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")
README_FILE = "README.md"
# Set width to "100%" for full width or a pixel value like "800"
IMAGE_WIDTH = "900"


def generate_readme():
    # 1. Get all image files in the current directory
    files = [f for f in os.listdir(".") if f.lower().endswith(EXTENSIONS)]

    # 2. Sort files by modification time (Newest First)
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("# Wallpaper Gallery\n")
        f.write(
            f"*Total Wallpapers: {len(files)} | Sorted by: Latest First*\n\n---\n\n"
        )

        for filename in files:
            # URL encode the filename (changes spaces to %20 so GitHub can read them)
            encoded_name = urllib.parse.quote(filename)

            # Write the image and the filename as a label
            f.write(f"### `{filename}`\n")
            f.write(
                f'<img src="./{encoded_name}" width="{IMAGE_WIDTH}" alt="{filename}">\n\n'
            )
            f.write("---\n\n")

    print(f"Successfully generated {README_FILE} with {len(files)} images.")


if __name__ == "__main__":
    generate_readme()
