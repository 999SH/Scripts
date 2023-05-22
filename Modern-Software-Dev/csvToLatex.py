import pandas as pd

# Define the LaTeX table template
latex_table = """
\\begin{{table}}[ht]
\\centering
\\renewcommand{{\\arraystretch}}{{1.3}}
\\caption{{Opinions on Pair Programming}}
\\begin{{tabular}}{{|p{{0.8\\linewidth}}|l|}}
\\hline
\\textbf{{Question}} & \\textbf{{Response}} \\\\
\\hline
What group were you a member of? & {} \\\\
\\hline 
What level of programmer are you? & {}/10\\\\
\\hline 
How much did your team use pair programming? & {}/10\\\\
\\hline 
How much do you feel pair programming improved the team's efficiency? & {}/10\\\\
\\hline 
How sustainable was pair programming? & {}/10\\\\
\\hline 
How much do you feel that the quality of the code improved when pair programming? & {}/10\\\\
\\hline 
How much do you feel you learned from pair programming? & {}/10\\\\
\\hline 
Do you have anything more to add? & {}\\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""

# Load data
data = pd.read_csv('pair_programming.csv')

# Define the LaTeX document and preamble
latex_document = """
\\documentclass{article}
\\usepackage{array}
\\begin{document}
"""

# Add each data row to the document as a table
for _, row in data.iterrows():
    latex_document += latex_table.format(row['What group were you a member of?'],
                                         row['What level of programmer are you?'],
                                         row['How much did your team use pair programming?'],
                                         row['How much do you feel pair programming improved the team\'s efficiency?'],
                                         row['How sustainable was pair programming?'],
                                         row['How much do you feel that the quality of the code improved when pair programming?'],
                                         row['How much do you feel you learned from pair programming?'],
                                         row['Do you have anything more to add?'] if pd.notna(row['Do you have anything more to add?']) else 'No'
                                         )

# Close the document
latex_document += "\n\\end{document}"

# Write the LaTeX document to a .tex file
with open('pair_programming.tex', 'w') as f:
    f.write(latex_document)
