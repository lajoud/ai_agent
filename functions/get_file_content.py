import os
from constants import MAX_CHARS
from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of a file and return the whole content in a string, or, if it is too long, return the first n characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get the content from, relative to the working directory",
            ),
        }
    ),
)

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(os.path.normpath(full_path))
        work_dir_path=os.path.abspath(working_directory)
        
        if os.path.commonpath([work_dir_path, full_path]) == work_dir_path:
            pass
        else:
            raise Exception(f"""Error: Cannot read "{file_path}" as it is outside the permitted working directory""")
        isfile = os.path.isfile(full_path)   
        if isfile:
            pass
        else:
            raise Exception(f"""Error: File not found or is not a regular file: {file_path}""")
        
        with open(full_path,"r") as f:
            content=f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            f.close()
        return content
    except Exception as e:
        return f"Error: {e}"


