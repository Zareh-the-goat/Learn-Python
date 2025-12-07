import json
from pathlib import Path
DATA_FILE = Path("students.json")

def _encode(students):
    """Convert sets to lists so JSON can serialize."""
    out = {}
    for name, d in students.items():
        out[name] = {
            "grade": d["grade"],
            "subjects": sorted(list(d["subjects"])),
            "scores": d["scores"],
        }
    return out
def _decode(raw: dict) -> dict:
    """Convert lists back to sets."""
    out = {}
    for name, d in raw.items():
        out[name] = {
            "grade": int(d.get("grade", 0)),
            "subjects": set(d.get("subjects", [])),
            "scores": {k: int(v) for k, v in d.get("scores", {}).items()},
        }
    return out

def save_students():
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(_encode(students), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[WARN] Failed to save: {e}")

def load_students():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        return _decode(raw)
    except Exception as e:
        print(f"[WARN] Failed to load, starting fresh: {e}")
        return {}
students = load_students()

def view_students():
    if not students:
        print("No students yet.")
        return
    for name in sorted(students.keys()):
        print_student(name, students[name])
        print("-")

def print_student(name,data):
    print(f"{name} is in grade {data["grade"]}")

    if not data["subjects"]:
        print("There is no subjects for this student")
    else:
        for x in data["subjects"]:
            sc = data["scores"][x]
            print(x, sc)

# print_student("Alice",students["Alice"])

def add_student():
     name = input("What is the students name?")
     if not name:
         print("Name can't be empty")
         return
     if name in students:
         print("Name already exists")
         return

     grade = int(input("What is the students grade?"))
     if not grade:
         print("Grade can't be empty")

     subjects = input("What subjects do you take? Note: Put comma between words")
     sublist = subjects.split(",")
     subset = set(sublist)


     scores = {

     }

     for subjects in subset:
         print(subjects)
         score = int(input(f"What is your grade for {subjects}"))
         scores[subjects]= score
     students[name] = {"grade": grade,
                       "subjects": subset,
                       "scores": scores
                       }
     save_students()

def search_student():
    studname = input("What is the students name ")
    data = students.get(studname)

    if not data:
        print("Student is not found")
        return
    else:
        print_student(studname,data)



def del_student():
    studelname = input("What is the students name that you want to delete?")

    if studelname not in students:
        print("Student not found")
        return
    else:
        del students[studelname]
        print("Student deleted")

    save_students()

def menu():
    print("\n--- Student Management (Simple) ---")
    print("1. View students")
    print("2. Add student")
    print("3. Search student")
    print("4. Update grade")
    print("5. Manage subjects/scores")
    print("6. Delete student")
    print("0. Exit")



def main():
    while True:
        menu()
        choice = input("Choose which one you want ")
        if choice == "3":
            search_student()
        elif choice == "2":
            add_student()
        elif choice == "1":
            view_students()
        elif choice == "6":
            del_student()
        elif choice == "4":
            print("Sorry, we can't do that yet.")
        elif choice == "5":
            print("Sorry, we can't do that yet.")
        elif choice == "0":
            break
        else:
            print("Pick a valid option")

main()










