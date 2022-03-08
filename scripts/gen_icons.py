# from argparse import ArgumentParser
from sys import argv
from csv import DictReader

HTML_TEMPLATE = """<a href="{link}" target="_blank" rel="noopener">
  <img src="{icon}" alt="{name}" width="{size}" height="{size}" style="margin:4px;">
</a>"""

def generate_icon_link(icon: dict[str, str], size: int):
    return HTML_TEMPLATE.format(
        link=icon["website"],
        icon=icon["icon"],
        name=icon["name"],
        size=size
    )



def generate_icons_html(csv_file_name: str, icon_size: int):
    links = []

    with open(csv_file_name) as csv_file:
        reader = DictReader(csv_file)

        return "\n".join([generate_icon_link(icon, icon_size) for icon in reader])


if __name__ == "__main__":
    # TODO change to use ArgumentParser
    # parser = ArgumentParser(description="Generate html links displayed as icons")
    if len(argv) < 3:
        print("usage: gen_icons.py <source-file> <icon-size>")
        exit()

    print(generate_icons_html(argv[1], int(argv[2])))
