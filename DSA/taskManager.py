import subprocess
import re

class TaskManager:
    def __init__(self):
        self.log = []
    
    def execute_command(self, command):
        result = subprocess.run(command, shell=True, capture_output=True)
        self.log.append(result.stdout.decode('utf-8'))
        self.log.append(result.stderr.decode('utf-8'))
        return result.stdout.decode('utf-8')
    
    def parse_logs(self):
        error_pattern = r"error|warning|cannot access|not found|no such file|cannot open|failed to open"
        error = []
        for log in self.log:
            error.extend(re.findall(error_pattern, log, re.IGNORECASE))
        return error
    
task_manager = TaskManager()
output = task_manager.execute_command("ls -l")
error = task_manager.parse_logs()

with open("file.txt", "w") as f:
    f.writelines("\n".join(task_manager.log))