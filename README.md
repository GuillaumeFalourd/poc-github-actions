# poc-github-actions

![title](/docs/github-actions.png)

This repository contains various proofs of concept using a Github Actions through workflows 🤖 

## Contents 🇧🇷

- [Introdução ao Github Actions](https://www.zup.com.br/blog/github-actions-ci-cd)
- [Como executar um script usando GitHub Actions](https://www.zup.com.br/blog/executar-script-github-actions)
- [Github Actions – variáveis de ambiente e secrets](https://www.zup.com.br/blog/github-actions-variaveis-de-ambiente-e-secrets)
- [Como manipular outputs no GitHub Actions](https://www.zup.com.br/blog/manipular-outputs-github-actions)
- [Workflows no GitHub Actions: como usar events e triggers](https://www.zup.com.br/blog/workflows-no-github-actions)
- [Como manipular outputs no GitHub Actions](https://www.zup.com.br/blog/manipular-outputs-github-actions)
- [Como usar imagens do Docker com workflows no Github Actions](https://www.zup.com.br/blog/github-actions-docker)
- [Como gerenciar artefatos nos workflows do Github Actions](https://www.zup.com.br/blog/artefatos-github-actions)
- [Como usar condicionais nos workflows do Github Actions ](https://www.zup.com.br/blog/como-usar-condicionais-workflows-github-actions)
- [10 boas práticas e dicas para usar o GitHub Actions](https://www.zup.com.br/blog/github-actions-dicas-boas-praticas)
- [Quando usar Reusable Workflow ou Composite Action no GitHub Actions?](https://www.zup.com.br/blog/reusable-workflow-e-composite-action)
- [Git Flow customizado no Github Actions](https://www.zup.com.br/blog/git-flow)

## Workflow YAML Basic Structure Explanation

```bash
name: Github action workflow name

on:
  push: # Run this workflow every time a new commit pushed to the repository
  pull_request:  # Run this workflow every time a new pull request is opened to the repository
  scheduled: # Run this workflow as a cron job
    - cron: "0 0 * * MON-FRI"
  workflow_dispatch: # Run this workflow on demand (manually)

jobs: # All workflows need at list one job

  job-key: #First job
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

[![01 - Default Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/01-default-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/01-default-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to run some basic commands.

[![02 - Secret Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/02-secret-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/02-secret-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to run some basic commands using repository secrets.

[![03 - Python Script Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/03-python-script-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/03-python-script-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to execute a specific script [run.py](https://github.com/GuillaumeFalourd/poc-github-actions/blob/main/run.py) located on the repository.

[![04 - Remote Dispatch Action Initiator](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/04-dispatch-event-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/04-dispatch-event-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to dispatch an event to the [ritchie-formulas-scheduler-demo repository](https://github.com/GuillaumeFalourd/ritchie-formulas-scheduler-demo).

[![05 - Container Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/05-container-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/05-container-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) with a docker container where Ritchie CLI and Golang are installed, then check Ritchie CLI and Golang versions through commands.

[![06 - Docker Image Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/06-docker-image-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/06-docker-image-workflow.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) and a docker image `foundeo/minibox:latest`. It also specify an `entrypoint` (the command to run inside the container) and `args` (command line arguments to pass to the command specified in entrypoint). It is possible to omit the `entrypoint` if the container already species the entrypoint you want to use.

[![07 - Action workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/07-action-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/07-action-workflow.yml)

This workflow will run an Action each time a `PUSH` event occurs on the repository. This specific action runs a Ritchie CLI formula.

[![08 - Outputs workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/08-outputs-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/08-outputs-workflow.yml)

This workflow illustrates how to set outputs in a job to use them on another job. This specific workflow prints `Hello-World`.

[![09 - Artifacts workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/09-artifacts-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/09-artifacts-workflow.yml)

This workflow illustrates how to pass data between jobs in the same workflow. For more information, see the [actions/upload-artifact](https://github.com/actions/upload-artifact) and [download-artifact](https://github.com/actions/download-artifact) actions. The full math operation performed in this workflow example is `(3 + 7) x 9 = 90`.

[![10 - Environment workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/10-environment-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/10-environment-workflow.yml)

This workflow illustrates how to use `environment` variables from the whole workflow, a specific job, or a specific step, as well as for an environment secret.

[![11 - Input workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/11-input-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/11-input-workflow.yml)

This workflow illustrates how to use `input` variables on a `workflow_dispatch` event.

[![12 - Run Workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/12-run-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/12-run-workflow.yml)

This workflow illustrates how to run a workflow once another specific one has been completed (with success or failure).

[![13 - Create Pull Request](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/13-create-pull-request.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/13-create-pull-request.yml)

This workflow uses [CRON](https://crontab.guru/#*_*_*_*_*) to automatically create a Pull Request committing updated files.

[![14 - Auto Merge](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/14-auto-merge.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/14-auto-merge.yml)

This workflow illustrates how to automatically merge a Pull Request with a specific label `automerge`.

[![15 - Push Dev](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/15-push-dev.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/15-push-dev.yml)

This workflow only run when a push is made to the `dev` branch.
Note that with this implementation, the workflow needs to be present on the specific branch as well (here `dev`).

[![16 - Conditional](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/16-conditional.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/16-conditional.yml)

This workflow illustrates how to use conditional through the `if` variable.

[![17 - Issue Greeter](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/17-issue-greeter.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/17-issue-greeter.yml)

This workflow illustrates how to write an automatic comment on a new issue, without using action, through the github API.

[![18 - Specific File](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/18-specific-file.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/18-specific-file.yml)

This workflow illustrates how to trigger a workflow when specific files are updated by a `push` or `pull_request` event.

[![19 - Push Event](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/19-push-event.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/19-push-event.yml)

This workflow illustrates how use the [checkout action](https://github.com/actions/checkout) to create a push event, updating a file and committing it to the branch.

[![20 - Generate Patch Tag with Cherry Pick](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/20-generate-patch-tag-cherry-pick.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/20-generate-patch-tag-cherry-pick.yml)

This workflow illustrates how use cherry-pick to generate a new repository tag informing 3 inputs (`reference tag`, `new tag`, and `commit hash`).

[![21 - Generate Release Branch with Cherry Pick](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/21-generate-release-branch-cherry-pick.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/21-generate-release-branch-cherry-pick.yml)

This workflow illustrates how use cherry-pick to generate a new release branch informing 3 inputs (`reference tag`, `new tag`, and `commit hash`).

[![22 - Install runner tools](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/22-install-runner-tools.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/22-install-runner-tools.yml)

This workflow illustrates how to install tools not supported by the ubuntu runner using `apt-get install`.

[![23 - Upload reset Asset](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/23-upload-release-asset.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/23-upload-release-asset.yml)

This workflow illustrates how to upload a release asset. [Example]( https://github.com/GuillaumeFalourd/poc-github-actions/releases/tag/821d0256)

[![24 - Github Context](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/24-contexts.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/24-contexts.yml)

This workflow illustrates how to access various context variables on a workflow.

[![25 - Artifacts between Workflows 1](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/25-artifacts-between-workflows-1.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/25-artifacts-between-workflows-1.yml) [![25 - Artifacts between Workflows 2](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/25-artifacts-between-workflows-2.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/25-artifacts-between-workflows-2.yml)

These workflows illustrate how to share datas between various workflows using artifacts.

[![26 - Create branch on another repo](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/26-create-release-branch-other-repo.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/26-create-release-branch-other-repo.yml)

This workflow illustrates how to create a new branch on another repository based on the current repository tag.

[![27 - Check Tags](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/27-check-tags.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/27-check-tags.yml)

This workflow illustrates how to use outputs between jobs with the `needs` context to check tags and manage them to perfom some operation according to their name.

[![28 - Create Pull Request (Workflow)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/28-create-pull-request.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/28-create-pull-request.yml)

This workflow illustrates how to create a new Pull Request based on a branch name after a push event.

[![29 - Check Actor on PR or PUSH](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/29-check-actor-pr-or-push.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/29-check-actor-pr-or-push.yml)

This workflow illustrates how to add a comment on a new Pull Request based on the github actor name after a PR event.

[![30 - Webhook Release](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/30-webhook-release.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/30-webhook-release.yml) - DEPRECATED

This workflow illustrates how to call a webhook on each release extracting the release tag.

[![31 - Untouchable file](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/31-untouchable-file.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/31-untouchable-file.yml)

This workflow illustrates how to close a Pull Request automatically if it updates on file that shouldn't be modified.

[![32 - PR approved and labeled](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/32-pr-approved-and-labeled.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/32-pr-approved-and-labeled.yml)

This workflow illustrates how to perform a specific action when approving a Pull request if it contains a specific label.

[![33 - Reusable workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/33-reusable-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/33-reusable-workflow.yml)

This workflow illustrates how to implement a [reusable workflow](https://docs.github.com/en/actions/learn-github-actions/reusing-workflows).

[![34 - Workflow Call](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/34-workflow-call.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/34-workflow-call.yml)

This workflow illustrates how to use and call a reusable workflow (cf workflow 33 above).

[![35 - Github Config](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/35-github-config.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/35-github-config.yml)

This workflow illustrates how to extract and use the user email and username from the commit using github config log commands.

[![36 - Local Action](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/36-local-action.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/36-local-action.yml)

This workflow illustrates how to use a `local action` file in one (or multiple workflows) and extract its outputs to perform other operations.

[![37 - Continue On Error Matrix](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/37-continue-on-error-matrix.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/37-continue-on-error-matrix.yml)

This workflow illustrates how to use matrix as well as expressions with `continue-on-error` and `if` conditionnal fields.

[![38 - Get PR number from PUSH event](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/38-get-pr-number-on-push-event.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/38-get-pr-number-on-push-event.yml)

This workflow illustrates how to get the related PR number to a push event.

[PR event](https://github.com/GuillaumeFalourd/poc-github-actions/runs/4317001308?check_suite_focus=true) and [Related PUSH event](https://github.com/GuillaumeFalourd/poc-github-actions/runs/4317001027?check_suite_focus=true)

[![39 - Extract From Branch](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/39-extract-from-branch.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/39-extract-from-branch.yml) [![40 - Invoked Workflow Dispatch](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/40-invoked-workflow-dispatch.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/40-invoked-workflow-dispatch.yml)

This workflows illustrate how to extract the tag version when a specific branch is created (e.g: `release-1.2.3`), and how to invoke another workflow through a disptach event sending this tag as input.

[![41 - Commit other repo](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/41-commit-other-repo.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/41-commit-other-repo.yml)

This workflow illustrates how to commit files from the current repo to another repo.

[![43 - Not trigger on tag](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/43-not-trigger-on-tag.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/43-not-trigger-on-tag.yml)

This workflow illustrates how to trigger a workflow on different event but NOT on tag.

[![44 - Check if PR from Fork](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/44-check-if-pr-from-fork.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/44-check-if-pr-from-fork.yml)

This workflow illustrates how to check if a PR is opened from a FORK repository or not.

[![45 - Get all yaml files](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/45-get-all-yaml-files.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/45-get-all-yaml-files.yml)

This workflow illustrates how to list all files from a specific extension (here, `.yaml` or `.yml`).

[![46 - Print env](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/46-print-env.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/46-print-env.yml)

This workflow illustrates how to list all env variables set in the runner.

[![47 - Force Failure](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/47-force-failure.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/47-force-failure.yml) - AS EXPECTED

This workflow illustrates how to force a workflow failure if a condition isn't met.

[![48 - Wait for reusable completion](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/48-wait-for-reusable-completion.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/48-wait-for-reusable-completion.yml) - DEPRECATED

This workflow illustrates how to wait for other workflows completion before executing some operation (using reusable workflows).

[![49 - Rename on release](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/49-rename-on-release.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/49-rename-on-release.yml)

This workflow illustrates how to rename a file according to the `github ref name` (branch or tag name).

[![50 - Create tag](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/50-create-tag.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/50-create-tag.yml)

This workflow illustrates how to simply create a tag in a job.

[![51 - Concurrency](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/51-concurrency.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/51-concurrency.yml)

This workflow illustrates how to use concurrency to avoid the same workflow to run in parallel for different push to the same branch (for example to limit Github actions runner usage in private repo).

[![52 - Print Secret](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/52-print-secret.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/52-print-secret.yml)

This workflow illustrates how to print secrets values on a workflow run. To harden the security of your github actions, have a look at [this guide](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions) on the Github Official Documentation.

[![53 - Concatenation](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/53-concatenation.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/53-concatenation.yml)

This workflow illustrates how to concatenate `env` variables using the environment file.

[![54 - Permissiom](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/54-permission.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/54-permission.yml)

This workflow illustrates how to use the `permission` field at the workflow level. Giving the GITHUB_TOKEN a specific permission scope during the workflow execution.

[![55 - Create Issue](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/55-create-issue.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/55-create-issue.yml) [![55 - Read Issue](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/55-read-issue.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/55-read-issue.yml)

These workflows illustrate how to **create** and **read** an issue body variable according to a specific [issue template](https://github.com/GuillaumeFalourd/poc-github-actions/blob/main/.github/ISSUE_TEMPLATE_DEPLOYMENT.md).

[![57 - Reusable outputs](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/57-reusable-outputs.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/57-reusable-outputs.yml)

This workflow illustrates how to use **outputs** with reusable workflows.

[![58 - Env Expressions](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/58-env-expressions.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/58-env-expressions.yml)

This workflows illustrates how to use **expressions** when setting env variables ath the workflow level, according to the trigger event.

[![59 - Step Context](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/59-step-context.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/59-step-context.yml)

This workflows illustrates how to use **[step context](https://docs.github.com/en/actions/learn-github-actions/contexts#steps-context)**, which contains detail about the execution of each step by default. Using the `outcome` property of each step we can check the result of its execution.

[![60 - Save secrets variables](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/60-save-secrets-variables.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/60-save-secrets-variables.yml)

This workflow illustrates how to save secrets in artifacts to use on later jobs.

[![61 - Create Tag and Release](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/61-create-tag-and-release.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/61-create-tag-and-release.yml) [![62 - Create Trigger on release other workflow](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/62-trigger-on-release-other-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/62-trigger-on-release-other-workflow.yml)

Those workflows illustrate how to **trigger a release creation** (with tag based on a branch syntax) where the release publication could **trigger a deployment pipeline**.

[![63 - Matrix folder](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/63-matrix-folder.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/63-matrix-folder.yml)

This workflow illustrates how to identify updated folders to perfom a similar behavior based on the folder through a reusable workflow with a matrix strategy.

[![65 - Sequential Matrix](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/65-sequential-matrix.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/65-sequential-matrix.yml)

This workflow illustrates how to execute sequencial jobs in specific order using matrix with `max-parallel: 1` strategy.

[![66 - Matrix Object](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/66-matrix-object.yaml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/66-matrix-object.yaml)

This workflow illustrates how to manipulate matrix object to perform different operation according to a object type.

[![67 - From JSON Env Var](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/67-fromjson-env-var.yaml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/67-fromjson-env-var.yaml)

This workflow illustrates how to extract a specific item from a JSON list stored in a environment variable dynamically.

[![68 - OS Types](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/68-ostypes.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/68-ostypes.yml)

This workflow shows the os type value for each github runner os.

[![69 - Run on Push to RC](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/69-run-on-push-to-rc.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/69-run-on-push-to-rc.yml)

This workflow illustrates how to extract a semantic version from a Release Candidate branch name.

[![70 - Post Failure](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/70-post-failure.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/70-post-failure.yml) - AS EXPECTED

This workflow illustrates how to execute a job when a previous job fails (post failure operations).

[![71 - Many Outputs Python](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/71-many-outputs-python.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/71-many-outputs-python.yml)

This workflow illustrates how to save many outputs using a python script and the GITHUB_OUTPUT file.

[![72 - Trigger on comment](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/72-trigger-on-comment.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/72-trigger-on-comment.yml)

This workflow illustrates how to start a workflow by commenting using a specific keyword in a Pull Request review.

[![73 - Check if file exists](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/73-if-file-exists.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/73-if-file-exists.yml) - AS EXPECTED

This workflow illustrates how to check if a file exists in a workflow after a failure, to perform some custom operations.

[![74 - n8N integration](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/74-n8n-integration.yml/badge.svg)](https://github.com/GuillaumeFalourd/poc-github-actions/actions/workflows/74-n8n-integration.yml) - AS EXPECTED

This workflow illustrates how to integrate github actions with a n8n workflow automation (http://n8n.io) using a webhook.