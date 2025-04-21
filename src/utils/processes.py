#! /usr/bin/env python3

from typing import Tuple

import asyncio

from config import GCLONE_COPY, RCLONE_LISTREMOTES
from exceptions import *


async def process_exec(command: str) -> Tuple[str, str, int]:
    """
    Process function which creates a subprocess shell with a
    specified command and returns its output.

    :param command: The command to execute.

    :return: (Tuple[str, str, int]) -
        A tuple representing the output contents of the subprocess shell.
          - stdout (String): The standard output from the command.
          - stderr (String): The standard error output from the command.
          - returncode (Integer): The exit status of the subprocess.
    """

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8'), process.returncode


async def process_exec_stream(command: str):
    """
    Process function that executes a shell command as a subprocess and
    yields each line of standard output (stdout) in real time.

    :param command: The shell command to execute.

    :yield: Lines of standard output from the subprocess.
    """
    
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        yield line.decode("utf-8").strip()

    await process.wait()


async def gclone_copy(source: str, destination: str = None) -> str:
    """
    Process function which performs an asynchronous copy operation using
    gclone from a {source} to a {destination}.

    :param source: The source path or remote to copy from.
    :param destination: The destination path or remote to copy to. 
                        Defaults to the value of DEFAULT_DESTINATION if not provided.
    
    :return: The standard output (stdout).
    """

    if destination == None:
        destination = DEFAULT_DESTINATION
    command = GCLONE_COPY.format(source=source, destination=destination)

    stdout, stderr, return_code = await process_exec(
        command=command
    )

    if return_code != 1:
        return stdout
    raise GcloneError(stderr.strip().splitlines()[0] if stderr else None)


async def gclone_copy_stream(source: str, destination: str = None):
    """
    Process function which performs a streamed copy operation using
    gclone from a {source} to a {destination}, yielding real-time output lines.

    :param source: The source path or remote to copy from.
    :param destination: The destination path or remote to copy to. 
                        Defaults to the value of DEFAULT_DESTINATION if not provided.

    :yield: Individual lines of real-time standard output (stdout).
    """

    if destination is None:
        destination = DEFAULT_DESTINATION

    command = GCLONE_COPY.format(source=source, destination=destination)
    async for line in process_exec_stream(command):
        yield line
        

async def rclone_remotes() -> str:
    """
    Process function which fetches a list of configured rclone remotes.

    :return: A string of remote names.
    """

    stdout, stderr, return_code = await process_exec(
        command=RCLONE_LISTREMOTES
    )

    if return_code != 1:
        return stdout.strip()
    raise GcloneError(stderr.strip().splitlines()[0] if stderr else None)
