"""Utilities to manage monkeytale file storage."""
import shutil
from pathlib import Path

from eliot import current_action
from eliot import log_call
from eliot import to_file
from eliot.json import EliotJSONEncoder

SOURCE_PATH = Path(".")
LOG_FILE = "monkeytale.log"
BUILD_DIRECTORY = "build"

LOG_PATH = SOURCE_PATH / LOG_FILE
BUILD_PATH = SOURCE_PATH / BUILD_DIRECTORY


class MonkeytaleJSONEncoder(EliotJSONEncoder):
    def default(self, o):
        try:
            return EliotJSONEncoder.default(self, o)
        except TypeError:
            return "REPR: " + f"{o=}"[4:]


@log_call  # noqa: NotCalledLocally
def start_log() -> Path:
    # Always overwrite the log for each run
    to_file(LOG_PATH.open(mode="w"), encoder=MonkeytaleJSONEncoder)
    return LOG_PATH


@log_call  # noqa: NotCalledLocally
def initialize_build_directory() -> Path:
    # Build from scratch every time
    if BUILD_PATH.is_dir():
        current_action().log(
            message_type=f"Deleting previous build directory: '{BUILD_DIRECTORY}'",
            path=str(BUILD_PATH.resolve()),
        )
        shutil.rmtree(BUILD_PATH)
    BUILD_PATH.mkdir(exist_ok=False, parents=True)
    return BUILD_PATH
