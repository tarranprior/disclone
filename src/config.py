#! /usr/bin/env python3

from utils.helpers import configuration

DEFAULT_REMOTE = "gclone:"
DEFAULT_DESTINATION = configuration()["configuration"]["default_destination"]

GCLONE_COPY = (
    "gclone copy {source} {destination} "
    "--transfers 50 -vP --stats-one-line --stats=15s "
    "--ignore-existing --drive-server-side-across-configs "
    "--drive-chunk-size 128M --drive-acknowledge-abuse "
    "--drive-keep-revision-forever"
)

GCLONE_MOVE = (
    "gclone move {source} {destination} "
    "--transfers 50 --tpslimit-burst 50 --checkers 10 -vP "
    "--stats-one-line --stats=15s --ignore-existing "
    "--drive-server-side-across-configs --drive-chunk-size "
    "128M --drive-acknowledge-abuse "
    "--drive-keep-revision-forever --fast-list "
)

GCLONE_SYNC = (
    "gclone sync {source} {destination} "
    "--transfers 50 --tpslimit-burst 50 --checkers 10 "
    "-vP --stats-one-line --stats=15s "
    "--drive-server-side-across-configs --drive-chunk-size "
    "128M --drive-acknowledge-abuse "
    "--drive-keep-revision-forever --fast-list"
)

GCLONE_CHECK = (
    "gclone check {source} {destination} -P "
    "--drive-server-side-across-configs --fast-list"
)

GCLONE_SIZE = (
    "gclone size {source} --disable ListR"
)
GCLONE_LSJSON = (
    "gclone lsjson {source}"
)
GCLONE_TREE = (
    "gclone tree {source}"
)

GCLONE_DELETE = (
    "gclone delete {source} -vP --stats-one-line "
    "--stats=15s --fast-list"
)
GCLONE_DELETE_FILE = (
    "gclone deletefile {source} -vP --stats-one-line "
    "--stats=15s --fast-list"
)
GCLONE_PURGE = (
    "gclone purge {source} -vP --stats-one-line "
    "--stats=15s --fast-list"
)

RCLONE_LISTREMOTES = (
    "rclone listremotes"
)
