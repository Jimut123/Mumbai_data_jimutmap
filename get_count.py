import glob
total_files = glob.glob('Mumbai_data/*')
total_folders = glob.glob('Mumbai_data/Mumbai*')
print(total_folders)
print(len(total_files))

