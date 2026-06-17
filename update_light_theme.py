import os

# 1. Update PALETTE in plots.py
plots_path = "src/visualization/plots.py"
with open(plots_path, "r") as f:
    content = f.read()

content = content.replace('("#ff6b7a")', '("#a82b35")') # This is wrong, it's a tuple.
content = content.replace('1: ("#e63946", "#ff6b7a")', '1: ("#e63946", "#a82b35")')
content = content.replace('2: ("#2a9d8f", "#52d9cb")', '2: ("#2a9d8f", "#1b635a")')
content = content.replace('3: ("#e9c46a", "#f4d792")', '3: ("#e9c46a", "#b5974e")')

content = content.replace('fill="#16213e"', 'fill="#f9f9f9"')

# Fix heatmap logic
old_diag_r = 'r_ = int(42 * (1 - intensity) + 42)'
old_diag_g = 'g_ = int(157 * intensity + 50 * (1 - intensity))'
old_diag_b = 'b_ = int(143 * intensity + 62 * (1 - intensity))'

new_diag_r = 'r_ = int(42 * intensity + 250 * (1 - intensity))'
new_diag_g = 'g_ = int(157 * intensity + 250 * (1 - intensity))'
new_diag_b = 'b_ = int(143 * intensity + 250 * (1 - intensity))'

content = content.replace(old_diag_r, new_diag_r)
content = content.replace(old_diag_g, new_diag_g)
content = content.replace(old_diag_b, new_diag_b)

old_off_r = 'r_ = int(230 * intensity + 26 * (1 - intensity))'
old_off_g = 'g_ = int(57 * intensity + 26 * (1 - intensity))'
old_off_b = 'b_ = int(70 * intensity + 46 * (1 - intensity))'

new_off_r = 'r_ = int(230 * intensity + 250 * (1 - intensity))'
new_off_g = 'g_ = int(57 * intensity + 250 * (1 - intensity))'
new_off_b = 'b_ = int(70 * intensity + 250 * (1 - intensity))'

content = content.replace(old_off_r, new_off_r)
content = content.replace(old_off_g, new_off_g)
content = content.replace(old_off_b, new_off_b)

# Fix text color in heatmap
content = content.replace('txt_fill = "#fff" if intensity > 0.4 else "#ccc"', 'txt_fill = "#fff" if intensity > 0.4 else "#333333"')

with open(plots_path, "w") as f:
    f.write(content)

# 2. Update advanced_plots.py
adv_path = "src/visualization/advanced_plots.py"
with open(adv_path, "r") as f:
    content = f.read()

content = content.replace('colors = ["#ff6b7a", "#52d9cb", "#f4d792"]', 'colors = ["#e63946", "#2a9d8f", "#e9c46a"]')

with open(adv_path, "w") as f:
    f.write(content)

# 3. Update algorithm_comparison.py
algo_path = "src/evaluation/algorithm_comparison.py"
with open(algo_path, "r") as f:
    content = f.read()

content = content.replace('colors = ["#f4a261", "#e76f51", "#8ab17d", "#2a9d8f"]', 'colors = ["#e76f51", "#2a9d8f", "#e9c46a", "#264653"]')
content = content.replace('1: "#ff6b7a"', '1: "#e63946"')
content = content.replace('2: "#52d9cb"', '2: "#2a9d8f"')
content = content.replace('3: "#f4d792"', '3: "#e9c46a"')

with open(algo_path, "w") as f:
    f.write(content)

print("Updated colors for light theme!")
