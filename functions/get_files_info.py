import os



from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:

        work_dir_path=os.path.abspath(working_directory)
        target_dir=os.path.normpath(os.path.join(work_dir_path,directory))
        print(work_dir_path,target_dir)
        isdir = os.path.isdir(target_dir)   
        if isdir:
            
            if os.path.commonpath([work_dir_path, target_dir]) == work_dir_path:
                pass
            else:
                raise Exception(f"""Error: Cannot list "{directory}" as it is outside the permitted working directory""")
        else:
            raise Exception(f"""Error: "{directory}" is not a directory""")
        
        print(os.listdir(target_dir))
        string_return=""
        for element in os.listdir(target_dir):
            string_return +="".join(f"""- {element}: file_size={os.path.getsize(os.path.join(target_dir,element))}, is_dir={os.path.isdir(os.path.join(target_dir,element))}\n""")
        return string_return
    except Exception as e:
        return f"Error: {e}"
    

    
     
