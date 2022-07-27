from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError


def parse_xml_fromstring(xml_fromstring: str) -> ET.Element:
    try:
        return ET.fromstring(xml_fromstring.strip())
    except ParseError as e:
        raise e


def parse_xml_to_dict(el: ET.Element) -> dict[str, list | str]:
    dict_xml = {el.tag: [] if el.attrib else ''}
    el_children = list(el)

    if el_children:
        children_list = []

        for children_dict in map(parse_xml_to_dict, el_children):
            children_list.append(children_dict)

        dict_xml = {el.tag: children_list}

    if el.text:
        text = el.text.strip()

        if not el_children:
            dict_xml[el.tag] = text

    return dict_xml
