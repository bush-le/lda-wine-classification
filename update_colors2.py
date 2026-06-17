import os

files = [
    "src/visualization/plots.py",
    "src/visualization/advanced_plots.py",
    "src/evaluation/algorithm_comparison.py"
]

replacements = {
    "#e0e0e0": "#000000",
    "#aaa": "#444444",
    "#ccc": "#333333",
}

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()
        
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        # Fix the specific txt_fill line in plots.py
        if filepath.endswith("plots.py"):
            content = content.replace('txt_fill = "#fff" if intensity > 0.4 else "#333333"', 
                                      'txt_fill = "#fff" if intensity > 0.4 else "#ccc"')
            
        with open(filepath, "w") as f:
            f.write(content)

print("Replaced e0e0e0, aaa, ccc colors successfully.")
