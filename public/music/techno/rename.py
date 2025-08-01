import os

folder = "./"  # MP3 dosyalarının bulunduğu klasör
for filename in os.listdir(folder):
    if filename.endswith(".mp3"):
        new_name = filename.replace(" ", "-").lower()
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
