from pathlib import Path
from xml.etree.ElementTree import Element, ParseError

from django.test import TestCase, Client

from xml_converter.xml_parser import parse_xml_fromstring, parse_xml_to_dict

TEST_DIR = Path(__file__).parent / Path('test_files')


class XMLConversionTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_connected_convert_empty_document(self) -> None:
        with (TEST_DIR / Path('empty.xml')).open() as fp:
            response = self.client.post('/connected/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Root": "",
            })

    def test_api_convert_empty_document(self) -> None:
        with (TEST_DIR / Path('empty.xml')).open() as fp:
            response = self.client.post('/api/converter/convert/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Root": "",
            })

    def test_connected_convert_addresses(self) -> None:
        with (TEST_DIR / Path('addresses.xml')).open() as fp:
            response = self.client.post('/connected/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Root": [
                    {
                        "Address": [
                            {"StreetLine1": "123 Main St."},
                            {"StreetLine2": "Suite 400"},
                            {"City": "San Francisco"},
                            {"State": "CA"},
                            {"PostCode": "94103"},
                        ]
                    },
                    {
                        "Address": [
                            {"StreetLine1": "400 Market St."},
                            {"City": "San Francisco"},
                            {"State": "CA"},
                            {"PostCode": "94108"},
                        ]
                    },
                ],
            })

    def test_parse_xml_fromstring(self) -> None:
        root = """
        <?xml version="1.0"?>
        <Root>
            <Address>
                <StreetLine1>123 Main St.</StreetLine1>
                <StreetLine2>Suite 400</StreetLine2>
                <City>San Francisco</City>
                <State>CA</State>
                <PostCode>94103</PostCode>
            </Address>
        </Root>
        """
        result = parse_xml_fromstring(xml_fromstring=root)
        self.assertEqual('Root', result.tag)
        self.assertIsInstance(result, Element)

    def test_parse_xml_fromstring_empty(self) -> None:
        with self.assertRaises(ParseError):
            parse_xml_fromstring(xml_fromstring='')

    def test_parse_xml_to_dict(self) -> None:
        root = """
        <Foo>
            <Bar>Baz</Bar>
        </Foo>
        """
        tree = parse_xml_fromstring(xml_fromstring=root)
        xml_parsed = parse_xml_to_dict(el=tree)
        self.assertIsInstance(xml_parsed.get('Foo'), list)
        self.assertEqual(xml_parsed.get('Foo')[0].get('Bar'), 'Baz')

    def test_parse_xml_to_dict_empty(self) -> None:
        root = """
        <?xml version="1.0"?>
        <Root></Root>
        """
        tree = parse_xml_fromstring(xml_fromstring=root)
        xml_parsed = parse_xml_to_dict(el=tree)
        self.assertEqual(xml_parsed.get('Root'), '')
