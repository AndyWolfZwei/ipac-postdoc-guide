import os
import re
from file_reader import file_content, content_slice


def concat_text():
    IoS2 = "Instructions_on_stage_2"  # Instructions_on_stage_2
    os.system("pandoc {}/{}.md -s -o {}/{}.html".format("..", IoS2, "part/", IoS2))
    Instructions_on_stage_2 = file_content("part/Instructions_on_stage_2.html")
    Instructions2_path_rectified = re.sub(r'src="images/', 'src="../images/', Instructions_on_stage_2)
    writefile = "part/Instructions_on_stage_2.html"
    with open(writefile, 'w', encoding='UTF-8') as wf:
        wf.write(Instructions2_path_rectified)

    os.system("pandoc {} -s -o {}".format("part/Instructions_on_stage_2.html", "part/Instructions_on_stage_2.docx"))
    print("Save {0} to {0}.docx".format("Instructions_on_stage_2"))

    # Instructions_on_stage_4
    os.system("pandoc {} -s -o {}"
              .format("../Instructions_on_stage_4.md", "part/Instructions_on_stage_4.html"))
    Instructions_on_stage_4 = file_content("part/Instructions_on_stage_4.html")
    Instructions4_path_rectified = re.sub(r'src="images/', 'src="../images/', Instructions_on_stage_4)
    writefile2 = "part/Instructions_on_stage_4.html"
    with open(writefile2, 'w', encoding='UTF-8') as wf:
        wf.write(Instructions4_path_rectified)
    os.system("pandoc {} -s -o {}"
              .format("part/Instructions_on_stage_4.html", "part/Instructions_on_stage_4.docx"))
    print("Save {0} to {0}.docx".format("Instructions_on_stage_4"))


if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass

    if 'y' == input("--- Concat cover? ---\n(Y/y for yes; others for no) ").lower():
        print("== Slice mid part of cover ==")
        mid_part = content_slice(file_content("../README.md"))
        bf_part = file_content("part/add_before_cover.tex")
        af_part = file_content("part/add_after_cover.md")
        cover_md = "part/cover.md"
        cover_tex = cover_md.replace(".md", ".tex")
        cover_docx = cover_md.replace(".md", ".docx")
        with open(cover_md, 'w') as wf:
            wf.write(bf_part)
            wf.write(mid_part)
            wf.write(af_part)
        os.system("pandoc {} -s -o {}".format(cover_md, cover_tex))
        os.system("pandoc {} -s -o {}".format(cover_tex, cover_docx))
        print("Save cover to {}".format(cover_docx))

    if 'y' == input("--- Concat text? ---\n(Y/y for yes; others for no) ").lower():
        concat_text()
