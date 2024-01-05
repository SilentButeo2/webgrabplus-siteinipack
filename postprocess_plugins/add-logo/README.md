# Add logo post process

Add or change channel logos in xmltv files

Content of the logos file
-------------------------

The syntax for the logo ini file is `channel name, logo link`. Each channel on its own line

- The `channel name` must be the same as the `channel_id` value in the channel section of the input file
- Lines starting with `*` are considered a comment text

**Example logos file content:**

```xml
TV Camara , https://www.net.com.br/imagens/logo/tv_camara-1680_95x39.png
TV Brasil , https://www.net.com.br/imagens/logo/tv_brasil-1683_95x39.png
PREMIERE HD 3 , https://www.net.com.br/imagens/logo/premiere_hd_3_-1175_95x39.png
```

## .NET version (add_logo.exe)

Version 1.0.0 Jan van Straaten , November 2020

How to use
----------

**Specify the following command line arguments following the syntax `/name=value` or `/name:value`:**

- `/in=xmltv`: input file name. E.g. /in=guide.xml
- `/out=xmltv`: output file name. This is an optional and default value is 'guide_logos.xml'.
      Cannot be the same as `/in`. E.g. /out=epg_logos.xml
- `/logos=name`: Name of the file with the new logos. E.g. /logos=my_logos.ini
- `/h` or `/?`: Print this help. Optional and takes no argument

**Example of a valid command line:**

```cmd
add_logo.exe /in=guide.xml /out=epg_logos.xml /logos=logos.ini
```

**Example as webgrab+plus postprocess plugin:**

```xml
<postprocess run=\"y\" grab=\"n\">add_logo.exe /in=guide+2.xml /logos=logos.txt</postprocess>
```    

# Python version (add_logo.py)

Version 1.0.0 Thiago Crepaldi, December 2023

The python version internally works the ame way as the .NET version. The only difference is how the script is invoked by the user.

## Requirements

* Python 3

How to use
----------

*add_logo.py [-h] --xmltv_in XMLTV_IN --logos LOGOS [--xmltv_out XMLTV_OUT] [--version VERSION] [--usage]*

Options
-------
  - `-h` or `--help`: Show this help message and exit
  - `--xmltv_in XMLTV_IN`: Path to XMLTV Guide file
  - `--logos LOGOS`: Path to Logos file
  - `--xmltv_out XMLTV_OUT`: Path to updated XMLTV Guide file that will be created
  - `--version VERSION`: Set script version

**Example of a valid command line:**

```sh
/usr/bin/python3 add_logo.py --xmltv_in=guide.xml --logos=my_logos.ini --xmltv_out guide_with_logo.xml
```

**Example as webgrab+plus postprocess plugin:**

```xml
<postprocess run=\"y\" grab=\"n\">python3 add_logo.py --xmltv_in=guide.xml --logos=my_logos.ini --xmltv_out guide_with_logo.xml</postprocess>
```
