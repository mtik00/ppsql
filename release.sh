#!/bin/bash
ERRORS=0

# Make sure we're clean
if [[ -n $(git status --porcelain) ]]; then
    echo "ERROR: branch not clean"
    ERRORS=1
fi

# Make sure we've pushed everything
if [[ -n $(git log origin/master..master) ]]; then
    echo "ERROR: Need to push changes upstream"
    ERRORS=1
fi

# Make sure our versions match
TOML_VERSION=$(grep -oP 'version = "\K(.*)(?=")' pyproject.toml)
PACKAGE_VERSION=$(grep -oP '__version__ = "\K(.*)(?=")' ppsql/__init__.py)

if [[ "${TOML_VERSION}" != "${PACKAGE_VERSION}" ]]; then
    echo "ERROR: toml and package version mismatch"
    echo "...package version: ${PACKAGE_VERSION}"
    echo "...   toml version: ${TOML_VERSION}"
    ERRORS=1
fi

if [[ ${ERRORS} != 0 ]]; then
    exit 1
fi

# Clear the build folder
rm -rf ./dist/*

# Build the packages
poetry build

# Upload the release to GitHub
hub release create \
-a dist/ppsql-${TOML_VERSION}-py2.py3-none-any.whl \
-a dist/ppsql-${TOML_VERSION}.tar.gz \
-m "Version v${TOML_VERSION}" \
v${TOML_VERSION}
