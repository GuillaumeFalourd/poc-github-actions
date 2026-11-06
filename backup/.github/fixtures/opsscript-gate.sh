#!/bin/sh
set -eu

# A portable branch uses the package manager present in the target image.
if command -v apt-get >/dev/null 2>&1; then
    apt-get --version
elif command -v apk >/dev/null 2>&1; then
    apk --version
else
    printf '%s\n' 'No supported package manager found' >&2
    exit 1
fi
