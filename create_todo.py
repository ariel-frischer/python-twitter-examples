import os

# Define the path for the TODO.md file
todo_path = 'TODO.md'

# Check if the file already exists
if not os.path.exists(todo_path):
    # Create the TODO.md file with a checklist
    with open(todo_path, 'w') as todo_file:
        todo_file.write("## TODO List\n\n- [ ] First item\n")

    print(f"Created {todo_path}")
else:
    print(f"{todo_path} already exists.")
