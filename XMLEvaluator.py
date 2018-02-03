from lxml import etree as XMLVAL
import xml.etree.ElementTree as ET


PATH_VPRASANJA = "Vprasanja.xml"
PATH_SHEMA = "ShemaVprasanj.xsd"


def validate_XML_doc(schema_path, xml_doc_path):
  xml_schema_doc = XMLVAL.parse(schema_path)
  xml_schema = XMLVAL.XMLSchema(xml_schema_doc)

  xml_doc = XMLVAL.parse(xml_doc_path)
  return xml_schema.validate(xml_doc)

def print_all_questions(xml_doc):
  tree = ET.parse(PATH_VPRASANJA)
  root = tree.getroot()
  for child in root.iter("vprasanje"):
    print (child.tag, child.attrib, child.text, child.find("vsebina").text, child.find("odgovor").text)


if __name__ == '__main__':

  print_all_questions(PATH_VPRASANJA)

  if (validate_XML_doc(PATH_SHEMA, PATH_VPRASANJA)):
    print("XML valid")
  else:
    print("XML not valid. Plese check file:" + PATH_VPRASANJA)
