import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
        filename='login_xml_test.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
def find_timingexbytes_incoming(number):
    tree = ET.parse('groups.xml')
    root = tree.getroot()
    check_number = number

    for number_value in root.findall(f".//group[number='{check_number}']"):
        incoming_value = number_value.find('timingExbytes/incoming')
        if incoming_value is None:
            print("NONE")
            logging.info("Value timingExbytes/incoming not found")
            continue
        logging.info(f"Value timingExbytes/incoming: {incoming_value.text}")
        print(incoming_value.text)

find_timingexbytes_incoming(1)