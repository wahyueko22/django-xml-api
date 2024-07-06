# config/config.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define global variables
GREETING_NAME = os.getenv("GREETING_APP_NAME", "pcap-analyzer-app")

ZEEKCTL_PATH=os.getenv("ZEEKCTL_PATH", "default")
PCAP_FILE_PATH = os.getenv("PCAP_FILE_PATH", "default")
SIGNATURE_FILE_SCRIPT_DIRECTORY = os.getenv("SIGNATURE_FILE_SCRIPT_DIRECTORY", "default")
ZEEK_EXECUTION_PATH = os.getenv("ZEEK_EXECUTION_PATH", "default")