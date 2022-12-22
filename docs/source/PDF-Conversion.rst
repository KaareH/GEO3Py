PDF to Jupyter-notebook steps
===============================

There are a few options if you are provided with a ``.pdf`` and want its contents inline in a Jupyter-notebook.
This is often the case for exams and homework.

*These instructions are only tested on specific system configurations, and may not work with every system. Each option has advantages and disadvantages.*


MS Word and pandoc
----------------------
1. Open PDF in word and save as ``.docx``
2. Run ``pandoc -f docx -t ipynb -o DGexam_E21.ipynb --extract-media=. DGexam_E21.docx``
3. Open notebook in VSCode
4. Find and replace ``attachment:./`` with nothing
5. Find and replace ``<img src="`` with ``![](``
6. Find and replace ``.png"`` with ``.png)``
7. Find and replace ``.jpg"`` with ``.jpg)``
8. Starting from the bottom of the markdown-cell, split the cells between each section and subsection. Shortcut in VSCode ``Shift + ctrl + -``

OCR to LaTeX conversion
-------------------------
`Mathpix <https://mathpix.com/>`_ is tool for converting screenshot-snippets to Markdown/LaTeX.
It works well for text and equations that can be directly pasted from clipboard into notebook-cells, but does not include graphical figures.

Internet connectivity is required for conversion.


IDE-extensions for quickly pasting images
----------------------------------------------
At least for VSCode, there are extensions available that makes it easy to paste images from clipboard into Jupyter-notebooks.
It's possible to either store image-data as separate files or embeded into the notebook as Base64.

See `Paste Image <https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image>`_ for VSCode.

Convert Jupyter-notebook to PDF
==================================
Run ``jupyter nbconvert --to pdf DGexam_E21.ipynb`` in the same directory as the notebook and media folder
