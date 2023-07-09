import os

def dfile(file: str, args: str = "", out: str = "./videos/"):
  with open(file, "r") as f:
    for line in f.read().splitlines():
      try:
        os.system(f"yt-dlp {args} {line}")
      except Exception as e:
        print(e)
def dyear(year: int, args: str = "", out: str = "./videos/"):
  y = str(year)
  file = f"./playlist/{year}.txt"
  dfile(file, args)
if __name__ == "__main__":
  dyear(2023, "-P ../videos/ -f 'best[height<=480][ext=mp4]/bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]'")
  print("makeSalvame Done")
