import os

def create_todo():
    if not os.path.exists('TODO.md'):
        with open('TODO.md', 'w') as file:
            file.write('- [ ] First item\n')

if __name__ == "__main__":
    create_todo()
