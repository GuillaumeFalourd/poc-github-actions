# Contribution

You're welcome to add useful actions to the repository

## New contents for the project

**Always** base your work on the project's `main` branch, naming your new branch
according to the following guide:

![branchs](/git-branchs.png)

**Examples: `feature/new-action-name` or `fix/action-name`**

## Guidelines

- Contents should be written in English.

- Add new actions on the [Global Actions section](https://github.com/GuillaumeFalourd/useful-actions#-global-actions), the [Docker Actions section](https://github.com/GuillaumeFalourd/useful-actions#-docker-actions) or on the [Other Tools Actions section](https://github.com/GuillaumeFalourd/useful-actions#-other-tools-actions) on the main README file (respect an `alphabetical` order).

- New actions should be associated to a workflow example on the `.github/workflows` directory of the [Useful Actions](https://github.com/GuillaumeFalourd/useful-actions) repository, based on the official action repository examples.

_Observation: If the action can be triggered through a `workflow_dispatch` event, please add it to the trigger options on the workflow implementation. It will make tests easier._
