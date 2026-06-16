# onedrive_filename_check

A tiny script to find files and folders whose names contain characters that **OneDrive (and Windows) won't allow**, so you can rename them before syncing.

OneDrive rejects names containing any of: `\ / : * ? " < > |`. This walks a directory tree and prints the full path of anything — file or folder — whose name includes one of those characters, then prints the total number of items scanned.

## Usage

```bash
python main.py
```

Set the `destination` variable at the top of `main.py` to the folder you want to scan (it's currently hardcoded to a local path). Any offending paths are printed to stdout, followed by the total count of items walked.

> A quick personal utility — the target directory is hardcoded rather than passed as an argument.
