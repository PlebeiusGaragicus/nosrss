# Credit: Jack Sweeney

import sys
import requests
import mimetypes
from requests.exceptions import HTTPError

import logging
logger = logging.getLogger("nospy")


def nostr_build_upload(file_name):
    """ Uploads an image/video to nostr build and returns the URL of it.
    """
    logger.debug(f"Uploading '{file_name}' to nostr.build...")

    url = 'https://nostr.build/api/upload/ios.php'

    with open(file_name, 'rb') as f:
        files = {'fileToUpload': f}
        data = {'submit': 'Upload'}
        response = requests.post(url, files=files, data=data)
    response.raise_for_status()
    if response.status_code == 200:
        return response.text.replace("\\", "").strip("\"")


def void_cat_upload(file_name):
    """ Uploads an image/video to void.cat and returns the URL of it.
    """
    logger.debug(f"Uploading '{file_name}' to void.cat...")

    mime_type, _ = mimetypes.guess_type(file_name)

    with open(file_name, "rb") as f:
        data = f.read()
    headers = {
        "V-Content-Type": mime_type,
        "V-Filename": file_name,
    }

    url = "https://void.cat/upload?cli=true"
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text


def upload_on_any(file_name):
    """Uploads an image/video to nostr build or void cat, depending on if the first fails."""
    try:
        url = nostr_build_upload(file_name)

    except HTTPError:
        logger.debug("Failed to upload image to nostr.build")
        pass # we will try another attempt using void.cat below

    except FileNotFoundError as e:
        logger.error(f"File '{file_name}' not found.")
        sys.exit(1)
    else:
        logger.debug("Successfully uploaded image to nostr.build")
        return url
    try:
        url = void_cat_upload(file_name)
    except HTTPError:
        logger.error("Failed to upload image")
        sys.exit(1)
    else:
        logger.debug("Successfully uploaded image to void.cat")
        return url


def upload(args):
    file_name = args.get("<file>", None)

    image_link = upload_on_any(file_name)

    # print(image_link)
    print(f"link: {image_link}")
