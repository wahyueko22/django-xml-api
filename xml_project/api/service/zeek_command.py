# zeek_command.py

import subprocess
import uuid
import os

class ZeekCommand:
   
    def run_command(self, command):
        result = subprocess.run(["sudo", zeekctl_path, command], check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True)
        return_object = {
            "execution_status" : f"Command 'zeekctl {command}' executed successfully",
            "execution_detail" : f"'{result}'" 
        }
        return return_object

    
    def create_zeek_script_file(self, sig_file_name, zeek_file_name, signature_content, zeek_script_content, file_script_directory):
        # Define the file name
        # Write the content to the file
        with open(os.path.join(file_script_directory, sig_file_name), 'w') as file:
            file.write(signature_content)
            

        # Write the content to the file
        with open(os.path.join(file_script_directory, zeek_file_name), 'w') as file:
            file.write(zeek_script_content)   
        
        print(f"{os.path.join(file_script_directory, zeek_file_name)}")
        

    def execute_pcap(self, pcap_path, zeek_file_name, execution_path, file_script_directory):
        execution_directory = os.path.expanduser(execution_path)
        # Step 2: Change the current working directory to the home directory
        os.chdir(execution_directory)
        command = ["zeek", "-r", pcap_path,  "-C", f"{os.path.join(file_script_directory, zeek_file_name)}"]
        # Execute the command and capture the output
        subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
  