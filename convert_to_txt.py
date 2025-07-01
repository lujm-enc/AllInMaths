import os
import shutil

# Define source and destination directories
SRC_DIR = os.path.abspath('.')
DST_DIR = os.path.join(os.path.dirname(SRC_DIR), os.path.basename(SRC_DIR) + '_txt')

# File extensions and names to ignore
IGNORE_EXTENSIONS = {'.aux', '.log', '.out', '.pdf', '.bcf', '.run.xml', '.synctex.gz', '.toc', '.synctex', '.synctex(busy)'}
IGNORE_NAMES = {'main.aux', 'main.log', 'main.out', 'main.pdf', 'main.bcf', 'main.run.xml', 'main.synctex.gz', 'main.synctex', 'main.synctex(busy)', 'main.toc'}


def should_ignore(file_name):
    ext = os.path.splitext(file_name)[1]
    return ext in IGNORE_EXTENSIONS or file_name in IGNORE_NAMES


def convert_and_copy(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s_item = os.path.join(src, item)
        d_item = os.path.join(dst, item)
        if os.path.isdir(s_item):
            convert_and_copy(s_item, d_item)
        else:
            if should_ignore(item):
                continue
            if item.endswith('.tex'):
                # Convert .tex to .txt
                d_item = d_item[:-4] + '.txt'
                with open(s_item, 'r', encoding='utf-8') as f_in, open(d_item, 'w', encoding='utf-8') as f_out:
                    f_out.write(f_in.read())
            else:
                shutil.copy2(s_item, d_item)


def main():
    if os.path.exists(DST_DIR):
        print(f"Destination folder {DST_DIR} already exists. Remove it or choose another name.")
        return
    convert_and_copy(SRC_DIR, DST_DIR)
    print(f"Project copied and .tex files converted to .txt in {DST_DIR}")


if __name__ == '__main__':
    main()
