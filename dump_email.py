from pathlib import Path
lines = Path('index.html').read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines,1):
    if 'emailLocal' in line:
        for j in range(max(1,i-2), min(len(lines), i+15)+1):
            print(f"{j}: {lines[j-1]}")
        break
