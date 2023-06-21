import re
import html

def remove_html_tags(text):
    img_tags = re.findall('<img.*?src="(.*?)".*?/?>', text)  # Find all image src attributes
    text_without_tags = re.sub('<.*?>', '', text)  # Remove all HTML tags
    text_without_tags = html.unescape(text_without_tags)  # Convert HTML entities to their actual characters

    # Add the image urls back to the text
    for img_tag in img_tags:
        text_without_tags += '\n' + img_tag

    return text_without_tags

text = """<p>The joystick is like a tiny dagger in my thumb…</p>
<img src="https://nitter.net/pic/ext_tw_video_thumb%2F1627801536884781057%2Fpu%2Fimg%2FIR-R9XtlyuuV8Wa2.jpg" />"""

clean_text = remove_html_tags(text)

print(clean_text)
