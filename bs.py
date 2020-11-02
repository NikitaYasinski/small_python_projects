from bs4 import BeautifulSoup

def parse(path_to_file):
    img_count = 0
    h_count = 0
    with open(path_to_file, 'r', encoding='utf-8') as wiki:
        contents = wiki.read()
        soup = BeautifulSoup(contents, 'lxml')
        img_tags = soup.find("div", id="bodyContent").find_all("img")
        for img_tag in img_tags:
            if "width" in img_tag.attrs:
                if int(img_tag["width"]) >= 200:
                    img_count += 1

        h_tags = soup.find("div", id="bodyContent").find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        for h_tag in h_tags:
            if h_tag.text[0] == "E" or h_tag.text[0] == "T" or h_tag.text[0] == "C":
                print(h_tag)
                h_count += 1

        max_tags = 0
        a_tags = soup.find("div", id="bodyContent").find_all("a")
        for a_tag in a_tags:
            current_count = 1
            siblings = a_tag.find_next_siblings()
            for sibling in siblings:
                if sibling.name == 'a':
                    current_count += 1
                    max_tags = max(current_count, max_tags)
                else:
                    current_count = 0

        count_list = 0
        lists = soup.find("div", id="bodyContent").find_all(['ul', 'ol'])
        for tag in lists:
            if not tag.find_parents(['ul', 'ol']):
                count_list += 1

    return [img_count, h_count, max_tags, count_list]
