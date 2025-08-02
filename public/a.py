import os

# Vercel'deki ana domain
base_url = "https://radio-music-storage.vercel.app/music"

# Script'in çalıştığı yerdeki "music" klasörünü kontrol eder
music_folder = "music"

print("🎧 MP3 Dosya Linkleri:\n")

for genre in os.listdir(music_folder):
    genre_path = os.path.join(music_folder, genre)
    if os.path.isdir(genre_path):
        print(f"🎵 {genre.upper()}:")
        for filename in os.listdir(genre_path):
            if filename.endswith(".mp3"):
                # URL için boşlukları %20 yap
                safe_filename = filename.replace(" ", "%20")
                full_url = f"{base_url}/{genre}/{safe_filename}"
                print(full_url)
        print()
