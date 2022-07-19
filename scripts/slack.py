#!/usr/bin/python3

import json
import requests
import argparse
import sys
import os


parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]), description='Python3 script to send slack alert')
parser.add_argument('--url', help='Slack URL')
parser.add_argument('--title', default="Github Actions Vulnerability Alert", help='The title of the alert')
parser.add_argument('--message', help='The alert message')
parser.add_argument('--username', help='The username of the alert to display', default="Github Actions Bot")
parser.add_argument('--iconEmoji', help="Emoji to send in the alert", default=":sos:")
parser.add_argument('--channel', help="To which channel send the alert", default="#alert-test")
parser.add_argument('--color', help="The color of the message", default="danger")
parser.add_argument('--actionLink', help="The link to the github action")
parser.add_argument('--branch', help="The branch name")

args = parser.parse_args()


slack_data = {
    "username": args.username,
    "icon_emoji": args.iconEmoji,
    "channel" : args.channel,
    "attachments": [
        {
            "color": args.color,
            "fields": [
                {
                    "title": args.title,
                    "value": args.message,
                    "short": "true"
                },
                {
                    "title": "Action URL",
                    "value": args.actionLink,
                    "short": "false"
                },
                {
                    "title": "Branch",
                    "value": args.branch,
                    "short": "false"
                }
            ]
        }
    ]
}

headers = {'Content-Type': "application/json"}
response = requests.post(args.url, data=json.dumps(slack_data), headers=headers)
if response.status_code != 200:
    raise Exception(response.status_code, response.text)