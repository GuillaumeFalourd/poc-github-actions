# poc-github-actions

![title](/docs/github-actions.png)

This repository is a Github Actions POC with various examples regarding how to create workflows 🤖 

## Workflow YAML Structure Explanation

```bash
name: Github action workflow name

on:
  push: # Run this workflow every time a new commit pushed to the repository
  pull_request:  # Run this workflow every time a new pull request is opened to the repository
  scheduled: # Run this workflow as a cron job
    - cron: "0 0 * * *"
  workflow_dispatch: # Run this workflow on demand (manually)

jobs: # All workflows need at list one job
  job-key:
    name: Job Name
    runs-on: ubuntu-latest # Set the type of machine the workflow will run on

    steps: # Each job can be divided in many steps
      
      - name: Checkout code # Step name
        uses: actions/checkout@v2 # Action used on the step

      - name: Run Super-Linter # Another step name
        uses: github/super-linter@v3  # Action used on the step
        env:  # Environment variables used on the step
          DEFAULT_BRANCH: main
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          
      - name: Run specific commands # Another step name
        run: |
          ls -lha
          echo "This is a shell command"
          
```

## Examples

[![1 - Default Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/1-default-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/1-default-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to run some basic commands.

[![2 - Secret Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/2-secret-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/2-secret-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to run some basic commands using repository secrets.

[![3 - Python Script Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/3-python-script-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/3-python-script-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to execute a specific script [run.py](https://github.com/GuillaumeFalourd/poc-github-actions/blob/main/run.py) located on the repository.

[![4 - Remote Dispatch Action Initiator](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/4-dispatch-event-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/4-dispatch-event-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to dispatch an event to the [ritchie-formulas-scheduler-demo repository](https://github.com/GuillaumeFalourd/ritchie-formulas-scheduler-demo).
