import sys
import os

# Markdown file path
project_path = sys.argv[1]
project_path = os.path.realpath(project_path)

# Image folder path
assets_path = sys.argv[2]
assets_path = os.path.realpath(assets_path)

if __name__ == "__main__":

    if not os.path.exists(project_path):
        print("Project path " + project_path + " not found.")
        sys.exit(1)
    if not os.path.exists(assets_path):
        print("Assets path " + assets_path + " not found.")
        sys.exit(1)

    image_list = os.listdir(assets_path)

    for i, image in enumerate(image_list):
        image_list[i] = os.path.join(assets_path, image)

    markdown_content = ""
    with open(project_path, "r") as file:
        markdown_content = file.read()

    unused_images = []

    for image in image_list:
        image_name = os.path.basename(image)
        if image_name not in markdown_content:
            unused_images.append(image)

    if len(unused_images) == 0:
        print("All images are used.")
    else:
        print("Unused images:")
        for image in unused_images:
            print(image)

    proceed = ""
    proceed = input("Do you want to delete these images? (y/n): ")

    if proceed == "y" or proceed == "Y":
        for image in unused_images:
            os.remove(image)
            print("Deleted: " + image)
    else:
        print("User chose not to delete images.")
