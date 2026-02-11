from pathlib import Path
path = Path('index.html')
data = path.read_text(encoding='utf-8')
data = data.replace('"Marianne Rethore": "ma.rethore"', '"Emilie Roussel": "e.roussel"')
path.write_text(data, encoding='utf-8')
