from . import config

def get(html_url):
    url = config.template_dir + "/" + html_url
    fi = open(url, "r")
    return fi.read()
