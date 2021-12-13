from jinja2 import Template


s = Template(open('kela.md', encoding='utf8').read()).render()
with open('readme.md', 'w', encoding='utf8') as f:
    f.write(s)
