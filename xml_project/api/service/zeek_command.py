# zeek_command.py

import subprocess

class ZeekCommand:
    def __init__(self, zeekctl_path="/opt/zeek/bin/zeekctl"):
        self.zeekctl_path = zeekctl_path

    def run_command(self, command):
        try:
            result = subprocess.run(["sudo", self.zeekctl_path, command], check=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)
            return_object = {
                "message_status" : f"Command 'zeekctl {command}' executed successfully",
                "execution_detail" : f"'{result}'" 
            }
            return return_object
        except subprocess.CalledProcessError as e:
            return f"Error running 'zeekctl {command}': {e}"
