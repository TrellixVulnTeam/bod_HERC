
from bs4 import BeautifulSoup ,Comment ,NavigableString
import re
prefix = "og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#"

for m in re.finditer(r"([A-z]*): (https?:\/\/[\/a-zA-Z0-9@:%&._\+~?#=&]*)", prefix):
        print((m.group(1)))
        print((m.group(2)))