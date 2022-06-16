# Audubon Field Guide Scraper

This script scrapes the common name, scientific name, photo, and sound (if available) from the [Audubon Field Guide](https://www.audubon.org/bird-guide?field_bird_family_tid=All&field_bird_region_tid=All) into a text file for import into Anki or similar flashcard software. It also downloads the photo and sound files.

This was whipped up very quickly, so the code is likely not optimal.

## Instructions for use

Python should already be installed on your system.

1. Install the packages in `requirements.txt`.

2. Open the [Audubon Field Guide](https://www.audubon.org/bird-guide?field_bird_family_tid=All&field_bird_region_tid=All).

3. Scroll down until all species are loaded.

4. Open your browser's developer tools (try <kbd>F12</kbd>).

5. Copy and paste all of the HTML into a file named `audubon.html`.

6. Move `audubon.html` and `audubon-scrape.py` into the same folder.

7. Run `audubon-scrape.py`.

## Todo

- [ ] Automatically organize into folders
- [ ] Scrape descriptions as well from species page
