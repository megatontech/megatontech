from jinja2 import Template


s = Template(open('README.md', encoding='utf8').read()).render()
with open('README.md', 'w', encoding='utf8') as f:
    f.write(s)
