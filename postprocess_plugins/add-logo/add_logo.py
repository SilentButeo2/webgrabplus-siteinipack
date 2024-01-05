import argparse
import csv
import os
import re
import sys
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--xmltv_in", help="Path to XMLTV Guide file", required=True)
    parser.add_argument("--logos", help="Path to Logos file", required=True)
    parser.add_argument(
        "--xmltv_out",
        help="Path to updated XMLTV Guide file that will be created",
        required=False,
    )
    parser.add_argument(
        "--version", help="Set script version", required=False, default="0.1"
    )

    args = parser.parse_args()

    # Check if the user has provided valid arguments
    check_usage(args)

    print("Add or change channel logos in xmltv files")
    print(f"Version {args.version} Thiago Crepaldi, December 2023\n")

    # Internal variables
    path = os.path.dirname(os.path.abspath(__file__))
    args.xmltv_in_path = os.path.dirname(os.path.abspath(args.xmltv_in))
    args.xmltv_out_path = os.path.dirname(os.path.abspath(args.xmltv_out))
    args.logos_path = os.path.dirname(os.path.abspath(args.logos))

    # Read the XMLTV file
    print(f"Reading XMLTV file {args.xmltv_in}...")
    xmltv_channels = {}
    document = parse(args.xmltv_in)
    for channel in document.getElementsByTagName("channel"):
        xmltv_id = channel.getAttribute("id").strip()
        icon = ""
        icon_element = channel.getElementsByTagName("icon")
        if len(icon_element) > 0:
            assert len(icon_element) == 1
            icon = icon_element[0].getAttribute("src").strip()
        xmltv_channels[xmltv_id] = icon

    # Read the logos file
    print(f"Reading logos file {args.logos}...")
    with open(args.logos, encoding="utf-8") as logos_file:
        content_reader = csv.reader(logos_file, delimiter=",")
        logos_changed = 0

        for xmltv_id_ini, new_icon in content_reader:
            xmltv_id_ini, new_icon = xmltv_id_ini.strip(), new_icon.strip()
            if xmltv_id_ini in xmltv_channels:
                if new_icon.lower() != xmltv_channels[xmltv_id_ini].lower():
                    logos_changed += 1
                    was_empty = xmltv_channels[xmltv_id_ini] == ""
                    xmltv_channels[xmltv_id_ini] = new_icon

                    if not was_empty:
                        print(
                            f"Logo replaced by '{new_icon}' for channel '{xmltv_id_ini}'"
                        )
                    else:
                        print(
                            f"Missing logo added '{new_icon}' for channel '{xmltv_id_ini}'"
                        )

        if logos_changed == 0:
            print("No logos added or changed .. ")

    # Update the XMLTV file with the new logos
    for channel in document.getElementsByTagName("channel"):
        xmltv_id = channel.getAttribute("id").strip()
        icon = ""
        new_icon = xmltv_channels[xmltv_id]
        icon_element = channel.getElementsByTagName("icon")
        if len(icon_element) > 0:
            assert len(icon_element) == 1
            icon = icon_element[0].getAttribute("src").strip()

        if (len(icon) == 0 and len(new_icon) > 0) or icon != new_icon:
            if not icon_element:
                icon_element = document.createElement("icon")
                channel.appendChild(icon_element)

            icon_element.setAttribute("src", new_icon)

    # Write the XMLTV file
    with open(args.xmltv_out, "w") as f:
        document.writexml(f, encoding="utf-8")


def check_usage(args):
    fail = False
    if not args.xmltv_in or not os.path.exists(args.xmltv_in):
        message = "invalid --xmltv_in argument, try -h for help"
        fail = True
    if not args.logos or not os.path.exists(args.logos):
        message = "invalid --logos arguments, try -h for help"
        fail = True

    if not args.xmltv_out:
        args.xmltv_out = args.xmltv_in.replace(".xml", "_logos.xml")

    if fail:
        raise RuntimeError(message)


if __name__ == "__main__":
    main()

