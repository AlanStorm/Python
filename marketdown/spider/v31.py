from lxml import etree

html = etree.parse("./v30.html")
rst = etree.tostring(html, pretty_print=True)
print(rst)
