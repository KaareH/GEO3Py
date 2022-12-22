PDF to Jupyter-notebook steps
=============================


(For exam and assignment use when given a `.pdf`)

1. Open PDF in word and save as `.docx`
2. Run `pandoc -f docx -t ipynb -o DGexam_E21.ipynb --extract-media=. DGexam_E21.docx`
3. Open notebook in VSCode
4. Find and replace `attachment:./` with nothing
5. Find and replace `<img src="` with `![](`
6. Find and replace `.png"` with `.png)`
7. Find and replace `.jpg"` with `.jpg)`
8. Starting from the bottom of the markdown-cell, split the cells between each section and subsection. Shortcut in VSCode `Shift + ctrl + -`


# Convert Jupyter-notebook to PDF
Run `jupyter nbconvert --to pdf DGexam_E21.ipynb` in the same directory as the notebook and media folder
