# SlackBashBackdoor

![pio1](https://github.com/ener1-s3c/bmap_checker/assets/29269177/d2a26267-8dc5-426f-8005-610fc18b51eb)


## Description
The tool is a Python Flask application designed to enhance communication and automation by allowing users to execute bash commands remotely through a user-friendly interface and receive the output in a Slack channel. It serves as a bridge between command-line operations and Slack notifications, streamlining workflow and facilitating system management tasks.

## Keyword
Shell Backdoor, Slack Shell Backdoor, Slack execute bash, 

## Installation

```
pip3 install -r requirements.txt
```

### Set Up the Slack Slash Command

- Go to your Slack workspace.
- Navigate to "Settings & administration" > "Manage apps."
- Click on "Custom Integrations" and then "Slash Commands."
- Click on "Create New Command."
- Fill in the details for your slash command:
- Command: /runcmd
- Request URL: Enter the URL where your Flask app is running, e.g., http://your-server-ip:5000/
Short Description: Provide a brief description of what the command does.
Usage Hint: Provide usage instructions for the command.

### Export Slack Webhook
```
export SLACK_WEBHOOK_URL='YOUR_SLACK_WEBHOOK_URL'
```

### Run
```
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Test the Slack Slash Command
```
/runcmd ls
```
