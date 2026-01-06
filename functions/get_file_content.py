import os
from constants import MAX_CHARS
def get_file_content(working_directory, file_path,MAX_CHARS):
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


