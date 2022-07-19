# Code Scanner

## This template uses 2 inputs:
  * `codeScannerRef`: The branch or tag to use. (Optional)
  * `slackUrl`: The slack webhook to send alerts to. (Mandatory)

## Example usage:

```
name: Code Scanner

on:
  push:
    branches: 
      - '*'
jobs:
  trigger-semgrep:
    name: Scan
    uses: Zooz/code-scanner/.github/workflows/semgrep.yml@main
    with:
      codeScannerRef: main
    secrets:
      slackUrl: ${{ secrets.SLACK_WEBHOOK }}
```
