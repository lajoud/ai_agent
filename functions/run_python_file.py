import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file and return the result",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get the content from, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments used to launch the process. This may be a list or a string.",
            ),
        }
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(os.path.normpath(full_path))
        work_dir_path=os.path.abspath(working_directory)
        
        if os.path.commonpath([work_dir_path, full_path]) == work_dir_path:
            pass
        else:
            raise Exception(f"""Cannot execute "{file_path}" as it is outside the permitted working directory""")
        
        
        if os.path.isfile(full_path):
            pass
        else:
            raise Exception(f""" "{file_path}" does not exist or is not a regular file""")
        
        if os.path.splitext(file_path)[1] != ".py":
            raise Exception(f""""{file_path}" is not a Python file""")

        command = ["python", full_path]
        if args!=None:
            command.extend(args)
        
        completed_process=subprocess.run(command, capture_output=True, timeout=30, text=True)

        if completed_process.returncode!=0:
            return f"Process exited with code {completed_process.returncode}"
        elif completed_process.stdout=="" and completed_process.stderr=="":
            return "No output produced"
        else:
            return f"STDOUT: {completed_process.stdout}/n STDERR: {completed_process.stderr}"
        
    except Exception as e:
        return f"Error: {e}"