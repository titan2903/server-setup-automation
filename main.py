import paramiko
from dotenv import load_dotenv
import os
import subprocess

# Load environment variables from the .env file
load_dotenv()

# Get values from environment variables
hostname = os.getenv('HOSTNAME')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Check if any of the required variables is missing
if not hostname or not username or not password:
    print("TEST")
    raise ValueError("Please provide values for HOSTNAME, USERNAME, and PASSWORD in the .env file.")

# Commands for server setup
commands = [
    'sudo timedatectl set-timezone Asia/Jakarta',
    'sudo apt update',
    'sudo apt upgrade -y',
    'sudo apt install -y git curl zip python3 python3-pip',
    'sudo apt install -y docker.io',
    'sudo usermod -aG docker $USER',
    'echo "Setup completed successfully"'
]

# Function to run SSH command
def run_ssh_command(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password, allow_agent=False)
    
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    
    client.close()
    
    return output, error

# Loop to execute each command
for command in commands:
    if command.startswith('sudo apt update'):
        # Use subprocess to run apt update command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode('utf-8')
        error = error.decode('utf-8')
        if error:
            print(f"Error running command start with apt update: {command}\n{error}")
    else:
        output, error = run_ssh_command(command)
        if error:
            print(f"Error running command: {command}\n{error}")

    print(f"Command executed successfully: {command}\n{output}")
