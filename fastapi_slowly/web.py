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
        """Render template with sensible default parameters."""

        # placeholder content
        kwargs.setdefault("content", DEFAULTS.HTML_CONTENT)

        # div class to wrap the content in (default: None, no wrapping)
        kwargs.setdefault("div_classes", DEFAULTS.HTML_DIV_CLASSES)

        # table classes
        kwargs.setdefault("table_classes", DEFAULTS.HTML_TABLE_CLASSES)

        # table id
        kwargs.setdefault("table_id", DEFAULTS.HTML_TABLE_ID)

        # table caption
        kwargs.setdefault("table_caption", DEFAULTS.HTML_TABLE_CAPTION)

        # table header classes
        kwargs.setdefault("thead_classes", DEFAULTS.HTML_THEAD_CLASSES)

        # table column order
        kwargs.setdefault("dt_order", DEFAULTS.JS_DT_ORDER)

        # version (goes in footer)
        kwargs.setdefault("version", DEFAULTS.HTML_FOOTER_VERSION)

        return self.template.render(**kwargs).lstrip("\n")


class DEFAULTS:
    HTML_CONTENT = Markup("sample content")
    HTML_DIV_CLASSES = None
    HTML_FOOTER_VERSION = "Version Latest.Greatest"
    HTML_TABLE_CLASSES = "table table-striped caption-bottom"
    HTML_TABLE_ID = "myTable"
    HTML_TABLE_CAPTION = "Such Table. Much rows. Very column."
    HTML_THEAD_CLASSES = None
    JS_DT_ORDER = "[]"  # unsorted


class URLS:
    ISS = "https://api.wheretheiss.at/v1/satellites/25544"
    PERIODIC_TABLE_CSV = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableCSV.csv"
