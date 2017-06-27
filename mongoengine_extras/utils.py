import re
import unicodedata

STRIP_REGEXP = re.compile(r'[^\w\s-]')
HYPHENATE_REGEXP = re.compile(r'[-\s]+')


def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8')
    value = str(STRIP_REGEXP.sub('', value).strip().lower())
    return HYPHENATE_REGEXP.sub('-', value)
