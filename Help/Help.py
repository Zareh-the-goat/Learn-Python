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
     input("What is your name")
     print("Don't Lie")
     name = input("What is your full name? ")
     if not name:
         print("Name can't be empty ")
         return
     if name in students:
         print("Name already exists ")
         return

     input("What is your Problem")
     print("Don't Lie")
     grade = (input("What is your problem "))
     if not grade:
         print("Can't be empty ")

     subjects = input("Okay we will help you. We need to know your card number/ password so we could give you a refund ")
     sublist = subjects.split(",")
     subset = set(sublist)


     scores = {

     }
     input("Don't Lie")
     for subjects in subset:
         print(subjects)
         score = (input(f"DON'T LIE "))
         scores[subjects]= score
     students[name] = {"grade": grade,
                       "subjects": subset,
                       "scores": scores
                       }
     save_students()

add_student()




