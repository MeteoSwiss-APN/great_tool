#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for package `great_tool`."""
import pytest
from click.testing import CliRunner

from great_tool import cli


# dummy lines to avoid flake8 error F401 (imported but unused); remove!
pytest


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "test_cli_project.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output
    dry_run_result = runner.invoke(cli.main, ["-n"])
    assert dry_run_result.exit_code == 0
    assert "Is dry run" in dry_run_result.output
    version_result = runner.invoke(cli.main, ["-V"])
    assert version_result.exit_code == 0
    assert cli.__version__ in version_result.output
