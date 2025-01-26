import requests

def main():
    get_file("https://www.open-epg.com/files/dominican1.xml")

def get_file(link:str) -> None:
    """Extract the xml file from the link."""
    data = requests.get(link)
    guides = data.text
    guides = guides.replace("+0000", "-10000")
    with open("text.xml", 'w+') as fp:
        fp.writelines(guides)
        fp.close()

main()
