import sys
import os

# Markdown folder path
project_path = sys.argv[1]
project_path = os.path.realpath(project_path)
markdown_file_list = []
for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith(".md"):
            markdown_file_list.append(os.path.join(root, file))

# Image folder path
assets_path = sys.argv[2]
assets_path = os.path.realpath(assets_path)

if __name__ == "__main__":

    # Check existence
    if not os.path.exists(project_path):
        print("Project path " + project_path + " not found.")
        sys.exit(1)
    if not os.path.exists(assets_path):
        print("Assets path " + assets_path + " not found.")
        sys.exit(1)

    print("Project path: " + project_path)
    print("All markdown files:" + str(markdown_file_list))

    # Get image list
    image_list = os.listdir(assets_path)
    for i, image in enumerate(image_list):
        image_list[i] = os.path.join(assets_path, image)

    # Get all markdown content
    markdown_content_list = []
    for markdown_file in markdown_file_list:
        with open(markdown_file, "r") as file:
            markdown_content_list.append(file.read())

    # Check if images are used
    unused_images = []
    for image in image_list:
        image_name = os.path.basename(image)
        used = False
        for markdown_content in markdown_content_list:
            if image_name in markdown_content:
                used = True
                break
            else:
                continue
        if not used:
            unused_images.append(image)

    # Decide to proceed or not
    if len(unused_images) == 0:
        print("All images are used.")
    else:
        print("Unused images:")
        for image in unused_images:
            print(image)
    proceed = ""
    proceed = input("Do you want to delete these images? (y/n): ")

    # Delete images
    if proceed == "y" or proceed == "Y":
        for image in unused_images:
            os.remove(image)
            print("Deleted: " + image)
    else:
        print("User chose not to delete images.")
