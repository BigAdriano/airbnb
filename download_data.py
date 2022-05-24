#!/usr/bin/env python3

import os
import requests


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        # create folder if it does not exist
        os.makedirs(dest_folder)

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

def main():
    download("http://data.insideairbnb.com/united-kingdom/england/london/2021-12-07/visualisations/listings.csv", dest_folder="airbnb")
    download("https://raw.githubusercontent.com/BigAdriano/BigAdriano/bf6556b173020ca581bef45ac21adef0b73bf61e/london.png",dest_folder="airbnb")


if __name__ == '__main__':
    main()