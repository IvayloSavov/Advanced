import os

path = input()
path_sep = path.count(os.path.sep)
result_dict = {}

for root, directories, files in os.walk(path):
    if path_sep - root.count(os.path.sep) > 1:
        continue
    for file in files:
        file_extension = file.split(".")
        extension = "." + file_extension[1]
        if extension not in result_dict.keys():
            result_dict[extension] = []
        result_dict[extension].append(f"- - - {file}")

path_to_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + os.path.sep + "report_1.txt"
with open(path_to_desktop, "w") as file:
    for extension, files in sorted(result_dict.items()):
        file.write(extension + "\n")
        for file_1 in sorted(files):
            file.write(file_1 + "\n")
    # for extension, files in sorted(result_dict.items()):
    #     print(extension, file=file)
    #     for file_1 in sorted(files):
    #         print(file_1, file=file)
