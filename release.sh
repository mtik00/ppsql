#!/bin/bash
###############################################################################
# This bash script is used to automate GitHub releases using the `hub`
# command-line tool (https://github.com/github/hub#installation).
#
# You can test the status by running `release.sh test`.  This will stop
# execution just before clearing the build folder.
###############################################################################
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
README_VERSION1=$(grep -oP 'download/v\K(.*?)(?=/)' README.md)
README_VERSION2=$(grep -oP 'ppsql-\K(.*?)(?=-)' README.md)

if [[ "${TOML_VERSION}" != "${PACKAGE_VERSION}" ]]; then
    echo "ERROR: toml and package version mismatch"
    echo "...package version: ${PACKAGE_VERSION}"
    echo "...   toml version: ${TOML_VERSION}"
    ERRORS=1
fi

if [[ "${README_VERSION1}" != "${README_VERSION2}" ]]; then
    echo "ERROR: inconsistent versions in README.md"
    ERRORS=1
fi

if [[ "${README_VERSION1}" != "${TOML_VERSION}" ]]; then
    echo "ERROR: toml and README version mismatch"
    echo "...README version: ${README_VERSION1}"
    echo "...  toml version: ${TOML_VERSION}"
    ERRORS=1
fi

if [[ ${ERRORS} != 0 ]]; then
    exit 1
fi

if [[ "${1}" == "test" ]]; then
    echo "test complete"
    exit
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
