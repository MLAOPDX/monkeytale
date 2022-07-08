import re

import pytest
from devtools import debug
from monkeytale import __version__
from pytest_bdd import given, parsers, scenarios, then, when
from sh import Command, ErrorReturnCode, grep, monkeytale, pdm, wc

# Cannot import directly as @ is not a valid Python identifier
a_tail = Command("@")

scenarios("../features/cli.feature")


@given("Monkeytale is installed")
def monkeytale_installed():
    assert int(wc(grep(pdm("list"), "monkeytale"), "-l"))


@when(
    parsers.parse("Monkeytale is executed using {command} with {option}"),
    target_fixture="monkeytale_output",
)
def monkeytale_executed(command, option):
    error_return_code = None
    try:
        if command == "monkeytale":
            result = monkeytale(option) if option else monkeytale()
        elif command == "@":
            result = a_tail(option) if option else a_tail()
        else:
            raise NotImplementedError(f"Command '{command}' not supported.")
    except ErrorReturnCode as e:
        result = ""
        error_return_code = e

    return (command, str(result), error_return_code)


@then("Monkeytale will complete successfully")
def monkeytale_version(monkeytale_output):
    _, _, error_return_code = monkeytale_output
    assert not error_return_code


@then("Monkeytale will echo back its current version")
def monkeytale_version(monkeytale_output):
    command, output, _ = monkeytale_output
    assert re.match(rf".*{command}, version \d+\.\d+\.\d+.*", output)
