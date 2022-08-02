# Code Scanner

## This template uses 2 inputs:
  * `codeScannerRef`: The branch or tag to use. (Optional)

## This template expects 4 mandatory secrets
  * `slackUrl`: The slack webhook to send alerts to.
  * `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`: Required for authentication with AWS in order to upload results to s3 bucket.  
  * `S3_BUCKET_NAME`: The s3 bucket which results will be uploaded to.
  * `AWS_REGION`: The region the s3 was deployed in.

## Example usage:

Create the next file structure in your repository `.github/workflows/scanner.yml`
Enter the next into the file `scanner.yml`

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
      slackUrl: ${{ secrets.SEMGREP_SLACK_ALERT }}
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      S3_BUCKET_NAME: ${{ secrets.S3_BUCKET_NAME }}
      AWS_REGION: ${{ secrets.AWS_REGION }}
```
