import os

label_dir = r"dataset_white_light\labels\val"

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)
        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0] != "0":
                parts[0] = "0"
            new_lines.append(" ".join(parts) + "\n")

        with open(file_path, "w") as f:
            f.writelines(new_lines)

print("标签修复完成")
