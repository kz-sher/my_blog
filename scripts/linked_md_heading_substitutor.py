import re
import glob 

def sub_md_heading_with_link(content: str, level: int):
    return re.sub('^' + '#' * level + ' (.*)', r'{% include linked_md_heading.html heading="\1" level=' + str(level) + r' %}', content, flags = re.M)

filenames = glob.glob('_posts/*md')
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
    wf = open(filename, 'w', encoding='utf8')
    wf.write(content)
    wf.close()