import os

for filename in os.listdir():
    if not filename.endswith('.tex') and not filename.endswith('.pdf') and not filename.endswith('.py') and not filename.endswith('.md') and not filename == 'cleanup_latex.py' and not filename == ".git" and filename != ".gitignore":
        os.remove(filename)
