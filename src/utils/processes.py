import asyncio

from exceptions import *
from config import *


async def process_exec(script: str):
    process = await asyncio.create_subprocess_shell(
        script,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    await process.wait()
    return process

async def gclone_copy(source: str, destination: str = None) -> None:
    if destination == None:
        destination = DEFAULT_DESTINATION
    d = "{" + destination + "}"
    s = "{" + source + "}"
    proc = await process_exec(f'gclone copy gclone:{s} gclone:{d} --transfers 50 -vP --stats-one-line --stats=15s --ignore-existing --drive-server-side-across-configs --drive-chunk-size 128M --drive-acknowledge-abuse --drive-keep-revision-forever')
    output = await proc.stdout.read()
    if proc.returncode != 1:
        return(output)
    raise GcloneError(f"{(await proc.stderr.read()).decode('utf-8').splitlines()[0]}.")

async def rclone_remotes() -> None:
    proc = await process_exec('rclone listremotes')
    remotes = [str(f'📁 {r}') for r in (await proc.stdout.read()).decode('utf-8').splitlines() if r != 'gclone:']
    strip_remotes = str("\n".join([f"{s[:32]}" for s in remotes]))
    return(remotes, strip_remotes)