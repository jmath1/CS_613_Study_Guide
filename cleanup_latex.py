import os

root = os.getcwd()
this_script = os.path.abspath(__file__)

for dirpath, dirnames, filenames in os.walk(root, topdown=True):
    if '.git' in dirnames:
        dirnames.remove('.git')

    for fname in filenames:
        fpath = os.path.join(dirpath, fname)

        # never remove this script
        if os.path.abspath(fpath) == this_script:
            continue

        # keep important files
        if fname.endswith(('.tex', '.pdf', '.py', '.md')) or fname == '.gitignore':
            continue

        try:
            os.remove(fpath)
            print("Removed:", fpath)
        except Exception as e:
            print("Failed to remove:", fpath, "->", e)
