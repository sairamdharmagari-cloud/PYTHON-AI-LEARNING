class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class AIEngineer(Employee):
    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill

    def display_skill(self):
        print("AI Skill:", self.skill)


engineer = AIEngineer(
    "Sairam",
    50000,
    "Machine Learning"
)

engineer.display()
engineer.display_skill()

#Inheritance       → Reuse parent class code
#Method overriding → Child changes parent behavior
#super()           → Access parent class functionality
#SChild class       → Gets functionality from parent