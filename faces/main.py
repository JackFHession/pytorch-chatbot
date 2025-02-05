import os

def read_face(path):
    path = f"./faces/{path}"
    os.system("clear")
    with open(path, "r") as face:
        data = face.read()
        lines = data.split("\n")
    
    for line in lines:
        print(f"{line}")

if __name__ == "__main__":
    path = input("Path: ")
    read_face(path)