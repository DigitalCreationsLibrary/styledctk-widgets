# SPDX-FileCopyrightText: 2025-present DigitalCreationsLibrary <aimosta.official@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from proj_test.__about__ import __version__
from proj_test.testlib import oneB


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="proj-test")
def proj_test():
    click.echo("Hello world!")


@proj_test.command("testb")
def testb():
    oneB()