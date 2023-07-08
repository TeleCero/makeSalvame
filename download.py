import os

def dfile: str, args: str = ""):
  with open(file, "r") as f:
    for line in f.read().splitlines():
      try:
        os.system(f"yt-dlp {args} {line}")
      except Exception as e:
        print(e)
def dyear(year: int, args: str = ""):
  y = str(year)
  file = f"./playlist/{year}.txt"
  dfile(file, args)
if __name__ == "__main__":
  dyear(2023)
  print("makeSalvame Done")
