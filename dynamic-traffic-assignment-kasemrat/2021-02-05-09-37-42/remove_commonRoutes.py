from lxml import etree
from xml.etree import ElementTree
import xml.etree.cElementTree as eleTree

# parsing directly.
tree = etree.parse('routes.rou.xml')
root = tree.getroot()
root_new = etree.Element('routes')
# Use a `set` to keep track of "visited" elements with good lookup time.
visited = set()

result = len(root.getchildren())
print('Before :', result)

# The iter method does a recursive traversal
for el in root.iter('route'):
    # Since the id is what defines a duplicate for you
    if 'edges' in el.attrib:
        current = el.get('edges')
        # In visited already means it's a duplicate, remove it
        if current in visited:
            el.getparent().remove(el)
            # print('duplicated....')
        # Otherwise mark this ID as "visited"
        else:
            visited.add(current)
            subelement = etree.Element('route')
            subelement.set('edges', str(current))
            root_new.append(subelement)

print('After :',len(visited))
tree=etree.ElementTree(root_new)
filename = "removeCommonRoutes.rou.xml"
tree.write(filename, xml_declaration=True,pretty_print=True)