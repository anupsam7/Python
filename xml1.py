import xml.etree.ElementTree as ET
data = '''<person>
<name>Anup</name>
<phone type="intl"> +1 734 303 4456</phone>
<email hide="anupsam7@hotmail.com"/>
</person>'''

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Number:',tree.find('phone').text)
print('Number type:',tree.find('phone').get('type'))
print('Email:',tree.find('email').get('hide'))
