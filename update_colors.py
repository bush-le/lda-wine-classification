import os

files = [
    "src/visualization/plots.py",
    "src/visualization/advanced_plots.py",
    "src/evaluation/algorithm_comparison.py"
]

replacements = {
    "#ffffff": "#000000",
    "#1a1a2e": "#ffffff",
    "#a0a0b0": "#555555",
    "#2a2a40": "#f0f0f0",
    "Dark background": "Light background",
    "light text": "dark text",
}

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, "w") as f:
        f.write(content)

print("Replaced colors successfully.")
