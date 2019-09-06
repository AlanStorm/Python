from lxml import etree

html = etree.parse("./v30.html")

print(html)

rst = html.xpath('//book')

print(rst)

rst = html.xpath('//book[@category="sport"]')

print(rst)

rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(rst)
