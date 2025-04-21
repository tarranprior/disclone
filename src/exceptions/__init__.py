#! /usr/bin/env python3

class GcloneError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
