# dev env setup

This project uses `poetry`, `pre-commit`, and optionally `direnv` (for `poetry` python version management).

**NOTE**: You don't need any of this to _use_ `ppsql`.  However, I'd appreciate if you used this environment to submit an PRs.

1.  Change to this folder
1.  Create and activate a Python3.6+ environment (use `direnv allow .` if you are using `direnv`)
1.  Install poetry (if you don't have it installed globally):  
    `pip install poetry`
1.  Install required packages:  
    `poetry install`
1.  Install the `pre-commit` hooks:  
    `pre-commit install`

That should do it.  `pre-commit` yells at you a lot, but that's a good thing.
