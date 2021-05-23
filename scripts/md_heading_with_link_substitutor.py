import re
import glob 
import os

def sub_md_heading_with_link(content: str, level: int):
    return re.sub('^' + '#' * level + ' (.*)', r'{% include md_heading_with_link.html heading="\1" level=' + str(level) + r' %}', content, flags = re.M)

filenames = glob.glob('_posts_bak/*md')
for filename in filenames:
    # read post md content
    rf = open(filename, 'r', encoding='utf8')

    # replace md heading with linked one 
    content = ''
    for line in rf:
        for i in range(1, 7): 
            line = sub_md_heading_with_link(line, i)
        content += line

    # write updated content back to post md
    wf = open('_posts/' + os.path.split(filename)[-1], 'w', encoding='utf8')
    wf.write(content)
    wf.close()