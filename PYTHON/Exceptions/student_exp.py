experience = input()
try:
    experience = int(experience)
    print("Experience", experience)
except ValueError:
    print("Invalid experience")