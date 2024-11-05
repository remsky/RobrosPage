import os

def rename_md_to_txt(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, file[:-3] + '.txt')
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    posts_directory = 'posts'
    rename_md_to_txt(posts_directory)
    print("Renaming complete.")
