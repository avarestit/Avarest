# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from bs4 import BeautifulSoup
from filer.models import File

from shuup.admin.forms.widgets import FileDnDUploaderWidget


def has_data_attribute(soup, attribute, val):
    return soup.select("[%s]" % attribute)[0][attribute] == val


def test_unbound_file_dnd_uploader_widget():
    soup = BeautifulSoup(FileDnDUploaderWidget().render(name="foo", value=""))
    assert soup.select("#dropzone-dropzone"), "widget has id"
    assert soup.select("input")[0]["name"] == "foo"
    assert not soup.select("input")[0].get("value")
    assert soup.select("[data-upload_path]")[0]["data-upload_path"] == "/"
    assert soup.select("[data-dropzone]")[0]["data-dropzone"] == "true"
    assert not soup.select("[data-kind]")
    assert not soup.select("[data-id]")
    assert not soup.select("[data-name]")
    assert not soup.select("[data-size]")
    assert not soup.select("[data-url]")
    assert not soup.select("[data-thumbnail]")
    assert not soup.select("[data-date]")


@pytest.mark.django_db
def test_bound_file_dnd_uploader_widget():
    f = File.objects.create(name="file")
    widget_html = FileDnDUploaderWidget(upload_path="/test", kind="foo").render(name="foo", value=f.pk)
    soup = BeautifulSoup(widget_html)
    assert soup.select("#dropzone-dropzone"), "widget has id"
    assert soup.select("input")[0]["name"] == "foo"
    assert soup.select("input")[0]["value"] == str(f.pk)
    assert soup.select("[data-upload_path]")[0]["data-upload_path"] == "/test"
    assert soup.select("[data-dropzone]")[0]["data-dropzone"] == "true"
    assert soup.select("[data-kind]")[0]["data-kind"] == "foo"
    assert soup.select("[data-id]")[0]["data-id"] == str(f.pk)
    assert soup.select("[data-name]")[0]["data-name"] == f.name
    assert not soup.select("[data-thumbnail]")
