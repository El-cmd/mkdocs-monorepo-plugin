#!/usr/bin/env python

from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch

from mkdocs_monorepo_plugin.edit_uri import EditUrl


class TestEditUri(TestCase):
    def test_is_root_uses_realpath_for_page_source_path(self):
        config = {"config_file_path": "/var/folders/work/mkdocs.yml"}
        page = SimpleNamespace(
            file=SimpleNamespace(abs_src_path="/var/folders/work/docs/index.md")
        )
        plugin = SimpleNamespace(originalDocsDir="/var/folders/work/docs")

        edit_url = EditUrl(config, page, plugin)

        def fake_realpath(value):
            if value.startswith("/var/folders/work"):
                return value.replace(
                    "/var/folders/work", "/private/var/folders/work", 1
                )
            return value

        with patch(
            "mkdocs_monorepo_plugin.edit_uri.path.realpath", side_effect=fake_realpath
        ):
            self.assertTrue(edit_url._EditUrl__is_root())
