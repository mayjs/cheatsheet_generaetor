from string import Template
import json

section_template = Template("""
    <h3>$title</h3>        
""")

content_templates = {"text": Template("""
    <p>$text</p>
    """),
    "shortcut": Template("""
    <code>$shortcut</code>
    <p>$desc</p>
    """),
}

def generate_content(content):
    print(content_templates[content["type"]].substitute(**content))


def generate_section(section):
    print("<div>")
    print(section_template.substitute(title=section["title"]))
    for content in section["content"]:
        generate_content(content)
    print("</div>")


with open("example.json") as f:
    descr = json.load(f)

if "sections" in descr:
    for section in descr["sections"]:
        generate_section(section)


