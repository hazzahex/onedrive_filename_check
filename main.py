import os

destination = "/Users/Harry.Hextall/Projects/"
total = 0
illegal = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']


def walk_directory():
    global total
    for root, directories, filenames in os.walk(destination):
        for filename in filenames:
            total += 1
            abs_path = os.path.join(root, filename)
            if [e for e in illegal if e in filename]:
                print(abs_path)
        for directory in directories:
            total += 1
            abs_path = os.path.join(root, directory)
            if [e for e in illegal if e in directory]:
                print(abs_path)


walk_directory()
print(total)
