import os
from google.genai import types



schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="A function that allow to write a content (a string) into a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the content to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that has to be writen in the file",
            ),
        }
    ),
)


def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(os.path.normpath(full_path))
        work_dir_path=os.path.abspath(working_directory)
        
        if os.path.commonpath([work_dir_path, full_path]) == work_dir_path:
            pass
        else:
            raise Exception(f"""Cannot write to "{file_path}" as it is outside the permitted working directory""")
        
        
        if os.path.isdir(full_path):
            raise Exception(f"""Cannot write to "{file_path}" as it is a directory""")
        
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path,"w") as f:
            f.write(content)
            return (f"""Successfully wrote to "{file_path}" ({len(content)} characters written)""")
    except Exception as e:
        return f"Error: {e}"