from pathlib import Path

p = Path.home()
p = p / "PathLib" / "readme.txt"
p.write_text("Bonjour")