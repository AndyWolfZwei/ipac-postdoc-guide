# Export to Off-line Guide

Concatenate several files to comprise 2 parts of the off-line guide:

1. Cover
    - Mainly from README.md at the master branch;
    - Author info in *part/add_before_cover.tex* would be added in the beginning;
    - URL of online guide in *part/add_after_cover.md* would be added at the end.
2. Text
    - From all Details

## Prerequisite

- Python 3+
- [pandoc](https://pandoc.org/installing.html)

## TODO

- python main.py to output *.docx* file:
    1. Add the **date** when the guide is updated;
    2. Add page header in each page **except** the 1st page;
    3. Optimize linespread (1.5x);
    4. Customize font size of headings;
    5. Optimize pagination.
- save the *.docx* file to *.pdf* file
    1. Correct bookmarks;
    2. Add **page number**;
    3. Rectify all **hyper-links**.