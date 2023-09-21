# fastapi_slowly/web.py

from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
from pathlib import Path


class Templates:
    static_folder = Path(__file__).parent.parent / "static"
    loader = FileSystemLoader(static_folder / "templates")
    env = Environment(loader=loader)

    def __init__(self, name="base.html"):
        self.template = self.env.get_template(name)

    def render(self, **kwargs):
        kwargs.setdefault("content", DEFAULTS.HTML_CONTENT)
        kwargs.setdefault("table_classes", DEFAULTS.HTML_TABLE_CLASSES)
        kwargs.setdefault("table_id", DEFAULTS.HTML_TABLE_ID)
        kwargs.setdefault("table_caption", DEFAULTS.HTML_TABLE_CAPTION)
        kwargs.setdefault("thead_classes", DEFAULTS.HTML_THEAD_CLASSES)
        kwargs.setdefault("version", DEFAULTS.HTML_FOOTER_VERSION)
        kwargs.setdefault("dt_order", DEFAULTS.JS_DT_ORDER)
        return self.template.render(**kwargs).lstrip("\n")


class DEFAULTS:
    HTML_CONTENT = Markup("sample content")
    HTML_FOOTER_VERSION = "Version Latest.Greatest"
    HTML_TABLE_CLASSES = "table table-striped caption-top"
    HTML_TABLE_ID = "myTable"
    HTML_TABLE_CAPTION = "Such Table. Much rows. Very Column."
    HTML_THEAD_CLASSES = None
    JS_DT_ORDER = "[]"  # unsorted


class URLS:
    ISS = "https://api.wheretheiss.at/v1/satellites/25544"
    PERIODIC_TABLE_CSV = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableCSV.csv"
