# useful-actions

![title](/useful-github-actions.png)

This repository lists some useful generic Actions to use in your Github workflows and repositories.

## Summary

- [Good to Know](https://github.com/GuillaumeFalourd/useful-actions#-good-to-know)
- [Useful Actions](https://github.com/GuillaumeFalourd/useful-actions#-useful-actions)
  - [Global Actions](https://github.com/GuillaumeFalourd/useful-actions#-global-actions)
  - [Docker Actions](https://github.com/GuillaumeFalourd/useful-actions#-docker-actions)
  - [Other Tools Actions](https://github.com/GuillaumeFalourd/useful-actions#-other-tools-actions)
- [How to create new actions](https://github.com/GuillaumeFalourd/useful-actions#-how-to-create-new-actions)
- [How to debug workflows](https://github.com/GuillaumeFalourd/useful-actions#%EF%B8%8F-how-to-debug-workflows)
- [How to test actions locally](https://github.com/GuillaumeFalourd/useful-actions#-how-to-test-actions-locally)
- [Contribution](CONTRIBUTING.md)

***

## 💡 Good To Know

- [Usage Limits](https://docs.github.com/en/actions/reference/usage-limits-billing-and-administration)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Authentication in a workflow](https://docs.github.com/en/actions/reference/authentication-in-a-workflow)
- [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

***

## 🔎 Useful Actions

***

## 🌐 Global Actions

[![Action Cond](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/action-cond.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/action-cond.yml)

[Action Cond](https://github.com/marketplace/actions/conditional-value-for-github-action): GitHub Action to use a `if-else` operation when needed, to set dynamic configuration of other steps.

[![Add Label](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/add-label.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/add-label.yml)

[Add Label](https://github.com/marketplace/actions/actions-ecosystem-add-labels): GitHub Action to add GitHub labels to an issue or a pull request.

[![Add Reviewers](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/add-reviewers.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/add-reviewers.yml)

[Add Reviewers](https://github.com/marketplace/actions/add-reviewers): Github action that adds Reviewers to the Pull Request.

[![App Token](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/app-token.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/app-token.yml)

[App Token](https://github.com/marketplace/actions/github-app-token): Github Action to impersonate a GitHub App when `secrets.GITHUB_TOKEN`'s limitations are too restrictive and a personal access token is not suitable.

[![Assert command line output](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/assert-command-line-output.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/assert-command-line-output.yml)

[Assert command line output](https://github.com/marketplace/actions/assert-command-line-output): Github Action to assert / check a command line output.

[![Auto Accept Collabs](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-accept-collabs.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-accept-collabs.yml)

[Auto Accept Collabs](https://github.com/marketplace/actions/auto-accept-collabs): Github Action to accept automatically all collaboration invites. Useful for a bot account.

[![Auto approve](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-approve.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-approve.yml)

[Auto Approve](https://github.com/marketplace/actions/auto-approve): Github Action to automatically approve pull requests.

[![Auto Assign](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-assign.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-assign.yml)

[Auto Assign](https://github.com/marketplace/actions/auto-assign-action): Github Action to add reviewers and assignees to a pull request when opened (needs [auto_assign.yml](https://github.com/GuillaumeFalourd/useful-actions/actions/auto_assign.yml) configuration file).

[![Auto Assign Author](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-assign-author.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-assign-author.yml)

[Auto Assign Author](https://github.com/marketplace/actions/auto-author-assign): Github Action to automatically assigns PR author as an assignee.

[![Auto merge](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-merge.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/auto-merge.yml)

[Auto Merge](https://github.com/marketplace/actions/merge-pull-requests): GitHub Action to automatically merge pull requests when they are ready (`automerged` label).

[![Branch Names](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/branch-names.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/branch-names.yml)

[Branch Names](https://github.com/marketplace/actions/branch-names): Github Action to get branch or tag information without the `/ref/*` prefix.

[![Cache](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/cache.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/cache.yml)

[Cache](https://github.com/marketplace/actions/cache): Github Action to cache dependencies and build outputs to improve workflow execution time.

[![Cancel Workflow](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/cancel-workflow.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/cancel-workflow.yml)

[Cancel Workflow](https://github.com/marketplace/actions/cancel-workflow-action): Github Action cancel any previous runs that are not `completed` for a given workflow. This includes runs with a status of `queued` or `in_progress`.

[![Changed Files](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/changed-files.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/changed-files.yml)

[Changed Files](https://github.com/marketplace/actions/changed-files): Github Action to retrieve all changed files relative to the default branch (`pull_request*` based events) or the last remote commit (`push` based event) returning the **absolute path** to all changed files from the project root.

[![Checkout](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/checkout.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/checkout.yml)

[Checkout](https://github.com/marketplace/actions/checkout): Github Action to checks-out your repository under `$GITHUB_WORKSPACE`, so your workflow can access it.

[![Close Pull Request](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/close-pull-request.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/close-pull-request.yml)

[Close Pull Request](https://github.com/marketplace/actions/close-pull-request): Github Action to automatically close a pull request (for example if modifying _untouchable files_).

[![Commit And Push](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/commit-and-push.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/commit-and-push.yml)

[Commit And Push](https://github.com/marketplace/actions/git-commit-and-push): Github Action to commit and push new code to the repository.

[![Compress Images](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/compress-image.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/compress-image.yml)

[Compress Images](https://github.com/marketplace/actions/image-actions): Github Action to automatically compresses JPEGs, PNGs and WebPs in Pull Requests.

[![Copycat](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/copycat.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/copycat.yml)

[Copycat](https://github.com/marketplace/actions/copycat-action): GitHub Action to copy files from your repository to another external repository. It is also possible to copy files from/to repository Wikis.

[![Create JSON](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/create-json.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/create-json.yml)

[Create JSON](https://github.com/marketplace/actions/create-json): GitHub Action to create a .json file dynamically on your workflow.

[![Create Pull Request](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/create-pull-request.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/create-pull-request.yml)

[Create Pull Request](https://github.com/marketplace/actions/create-pull-request): GitHub Action to create a pull request for changes to your repository in the actions workspace.

[![Curl](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/curl.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/curl.yml)

[Curl](https://github.com/marketplace/actions/github-action-for-curl): GitHub Action to use the curl CLI to perform http requests.

[![Debug](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/debug.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/debug.yml)

[Debug](https://github.com/marketplace/actions/debug-action): GitHub Action to print the environment variables and the event payload. Useful for developing or debugging GitHub Actions.

[![Delete Artifacts](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/delete-artifact.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/delete-artifact.yml)

[Delete Artifacts](https://github.com/marketplace/actions/delete-artifact): GitHub Action to delete artifacts within a workflow run. This can be useful when artifacts are shared across jobs, but are no longer needed when the workflow is complete.

[![Enforce PR labels](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/enforce-labels.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/enforce-labels.yml)

[Enforce PR labels](https://github.com/marketplace/actions/enforce-pr-labels): GitHub Action to enforce assigning labels before merging PR's. Useful for generating automatic changelog and release notes with `github-release-notes`.

[![Env Vars](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/env-vars.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/env-vars.yml)

[Env Vars](https://github.com/marketplace/actions/github-environment-variables-action): GitHub Action to expose useful environment variables.

[![File Existence](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/file-existence.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/file-existence.yml)

[File Existence](https://github.com/marketplace/actions/file-existence): Github Action to check if files exists or not.

[![First Interaction](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/first-interaction.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/first-interaction.yml)

[First Interaction](https://github.com/marketplace/actions/first-interaction): Github Action to filter pull requests and issues from first-time contributors.

[![Get Workflow Origin](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/get-workflow-origin.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/get-workflow-origin.yml) [![Get Workflow Origin Information](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/get-workflow-origin-run.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/get-workflow-origin-run.yml)

[Get Workflow Origin](https://github.com/potiuk/get-workflow-origin): Github Action to provide information about the pull requests that triggered the workflow for the `pull_request` and `pull_request_review` events or for the `workflow_run` event that is triggered by one of those events.

[![GHAction Dump Context](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/ghaction-dump-context.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/ghaction-dump-context.yml)

[GHAction Dump Context](https://github.com/marketplace/actions/dump-context): GitHub Action to dump context of your workflow (which allows to check all variables available using the `github.event` syntax in the workflow).

[![GHAction Github Status](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/ghaction-github-status.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/ghaction-github-status.yml)

[GHAction Github Status](https://github.com/marketplace/actions/github-status): GitHub Action to check [GitHub Status](https://www.githubstatus.com/) in workflows, allowinf to trigger error if GitHub services are down.

[![Git Auto Commit](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/git-auto-commit.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/git-auto-commit.yml)

[Git Auto Commit](https://github.com/marketplace/actions/git-auto-commit): GitHub Action to detect changed files during a Workflow run and to commit and push them back to the GitHub repository. By default, the commit is made in the name of "GitHub Actions" and co-authored by the user that made the last commit.

[![Github Environment Variables](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/github-environment-variables.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/github-environment-variables.yml)

[Github Environment Variables](https://github.com/marketplace/actions/github-environment-variables-action): GitHub Action to expose useful environment variables.

[![Github Script](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/github-script.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/github-script.yml)

[Github Script](https://github.com/marketplace/actions/github-script): Github Action to make it easy to quickly write a script in your workflow that uses the GitHub API and the workflow run context.

[![Gitleaks](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/gitleaks.yml)

[Gitleaks](https://github.com/marketplace/actions/gitleaks): Github Action to detect hardcoded secrets like passwords, api keys, and tokens in git repos.

[![GPT Review](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/gpt-review.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/gpt-review.yml) - QUOTA EXCEEDED

[GPT Review](https://github.com/marketplace/actions/chat-gpt-code-peer-review): Github Action enabling automatic code reviewing in your repository by sending the git diff patches between a head ref and a base ref to OpenAI's API for annotation using Chat GPT (needs [OpenAi API Key](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt)).

[![Manual Approval](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/manual-approval.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/manual-approval.yml)

[Manual Approval](https://github.com/marketplace/actions/manual-workflow-approval): Github Action to pause a workflow and require manual approval from **one or more** approvers before continuing.

[![Paths Filter](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/paths-filter.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/paths-filter.yml)

[Paths Filter](https://github.com/marketplace/actions/paths-changes-filter): Github Action that enables conditional execution of workflow steps and jobs, based on the files modified by pull request, on a feature branch, or by the recently pushed commits.

[![Pull Request](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/pull-request.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/pull-request.yml)

[Pull Request](https://github.com/marketplace/actions/github-pull-request-action): GitHub Action to create pull requests automatically.

[![Purge Artifacts](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/purge-artifacts.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/purge-artifacts.yml)

[Purge Artifacts](https://github.com/marketplace/actions/purge-artifacts): Github Action responsible for deleting old artifacts by setting expire duration.

[![Read File](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/read-file.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/read-file.yml)

[Read File](https://github.com/marketplace/actions/read-file): Github Action to read file contents.

[![Recreate Release](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/recreate-release.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/recreate-release.yml)

[Recreate Release](https://github.com/GongT/actions-recreate-release): Github Action to delete previous release by `tag_name` or `release_name` and then call `actions/create-release` to create it again.

[![Release](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/release.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/release.yml)

[Release](https://github.com/marketplace/actions/gh-release): GitHub Action for creating GitHub Releases on Linux, Windows, and macOS virtual environments.

[![Replace Token](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/replace-token.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/replace-token.yml)

[Replace Token](https://github.com/marketplace/actions/replace-tokens): GitHub Action for replacing tokens in files.

[![Replace Values Action](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/replace-values-action.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/replace-values-action.yml): Github Action to replace values in files (secrets or fields).

[![Repository-Dispatch](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/repository-dispatch.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/repository-dispatch.yml) [![Repository-Dispatch-Triggered](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/repository-dispatch-triggered.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/repository-dispatch-triggered.yml)

[Repository-Dispatch](https://github.com/marketplace/actions/repository-dispatch): GitHub Action to create a repository dispatch event.

[![Retry Action](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/retry-action.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/retry-action.yml)

[Retry Action](https://github.com/marketplace/actions/retry-action): GitHub Action to rerun another GitHub Actions and commands.

[![Set Secrets](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/set-secrets.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/set-secrets.yml)

[Set Secrets](https://github.com/marketplace/actions/set-action-secret): Github Action to Create or edit actions secrets in repository or organizations.

<img width="731" alt="Example" src="https://user-images.githubusercontent.com/22433243/114315936-ac0b4d00-9ad7-11eb-8841-4e61b75b44ed.png">

[![Skip duplicate](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/skip-duplicate.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/skip-duplicate.yml)

[Skip duplicate](https://github.com/marketplace/actions/skip-duplicate-actions): GitHub Action to skip duplicate workflow-runs (after merges, pull requests or similar), skip concurrent or parallel workflow-runs for things that you do not want to run twice, skip ignored paths to speedup documentation-changes or similar, skip if paths not changed for something like directory-specific tests, cancel outdated workflow-runs after branch-pushes.

[![Stale](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/stale.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/stale.yml)

[Stale](https://github.com/marketplace/actions/close-stale-issues): GitHub Action to warn and then close issues and PRs that have had no activity for a specified amount of time.

[![Super Linter](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/super-linter.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/super-linter.yml)

[Super Linter](https://github.com/marketplace/actions/super-linter): Github Action to help validate your source code.

[![Upload & Download Artifacts](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/upload-download-artifacts.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/upload-download-artifacts.yml)

[Upload Artifact](https://github.com/marketplace/actions/upload-a-build-artifact): Github Action to share data between jobs and store data once a workflow is complete  ([example](https://docs.github.com/en/actions/guides/storing-workflow-data-as-artifacts#passing-data-between-jobs-in-a-workflow)).

[Download Artifact](https://github.com/marketplace/actions/download-a-build-artifact): Github Action to download artifacts from your build ([example](https://docs.github.com/en/actions/guides/storing-workflow-data-as-artifacts#passing-data-between-jobs-in-a-workflow)).

[![Wait on check](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/wait-on-check.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/wait-on-check.yml)

[Wait on check](https://github.com/marketplace/actions/wait-on-check): Github Action to pause a workflow until a job in another workflow completes successfully.

[![Workflow Dispatch](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/workflow-dispatch.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/workflow-dispatch.yml) [![Workflow Dispatch Triggered](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/workflow-dispatch-triggerred.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/workflow-dispatch-triggerred.yml)

[Workflow Dispatch](https://github.com/marketplace/actions/workflow-dispatch): Github Action to trigger another GitHub Actions workflow, using the `workflow_dispatch` event. The workflow must be configured for this event type `e.g. on: [workflow_dispatch]`. This allows you to chain workflows, the classic use case is have a CI build workflow, trigger a CD release/deploy workflow when it completes. Allowing you to maintain separate workflows for CI and CD, and pass data between them as required.

***

## 🐳 Docker Actions

[![GHAction Container Scan](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/ghaction-container-scan.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/ghaction-container-scan.yml)

[GHAction Container Scan](https://github.com/marketplace/actions/container-scan): GitHub Action to check for vulnerabilities in a container image with [Trivy](https://github.com/aquasecurity/trivy).

[![Hadolint](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/hadolint.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/hadolint.yml)

[Hadolint](https://github.com/burdzwastaken/hadolint-action): Github Action to run Hadolint and reports violations given a Dockerfile within a repository on a pull request.

[![Phonito](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/phonito.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/phonito.yml)

[Phonito](https://github.com/marketplace/actions/docker-vulnerability-scan-with-phonito-security): Github Action to automate scanning Docker images for OS & library vulnerabilities. Need a free Phonito Security account at [https://phonito.io](https://phonito.io).

[![Publish Docker](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/publish-docker.yml/badge.svg)](https://github.com/GuillaumeFalourd/useful-actions/actions/workflows/publish-docker.yml)

[Publish Docker](https://github.com/marketplace/actions/publish-docker): Github Action to build and push containers.

## 🦾 Other Tools Actions

_TODO_

***

## 🧐 How to create new actions

The [Github tutorial](https://docs.github.com/en/actions/creating-actions) is great to understand how to create:

- [Docker Container Actions](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)
- [Javascript Actions](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action)
- [Composite Run Steps Actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-run-steps-action)

***

## 🕵️ How to debug workflows

The [action-upterm](https://github.com/lhotari/action-upterm) uses [upterm](https://upterm.dev/) and [tmux](https://github.com/tmux/tmux/wiki) to offer a direct way to interact with the host system on which the actual actions will run.

By using this minimal example a upterm session will be created.

```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup upterm session
      uses: lhotari/action-upterm@v1
```

To get the `ssh` connection string, just open the workflow `Checks` tab and scroll to the bottom.

_Note: If you want to continue a workflow and you are inside a upterm session, just create a empty file with the name `continue` either in the root directory or in the workspace directory by running `touch continue` or `sudo touch /continue`. Closing the terminal will also continue the workflow. However you won't be able to reconnect in that case. It's possible to detach from the terminal and not continue by first pressing C-b and then d (tmux detach command keys)._

***

## 🤖 How to test actions locally

This tool can be used to test actions locally: [Act](https://github.com/nektos/act)

<img width="684" alt="Screenshot" src="https://user-images.githubusercontent.com/22433243/114316117-89c5ff00-9ad8-11eb-9408-bd163d39daea.png">

***

## 🤝 Contribution

Would like to contribute to the repository? Here are the [guidelines](CONTRIBUTING.md) 🚀


<a href="https://github.com/GuillaumeFalourd/useful-actions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GuillaumeFalourd/useful-actions" />
</a>

(Made with [contributors-img](https://contrib.rocks))
