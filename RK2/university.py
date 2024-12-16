"""class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.departments = []  # Связь один-ко-многим с кафедрами

class Department:
    def __init__(self, id, name, faculty_id):
        self.id = id
        self.name = name
        self.faculty_id = faculty_id  # Ссылка на факультет

class Professor:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.departments = []  # Связь многие-ко-многим с кафедрами

class ProfessorDepartment:
    def __init__(self, professor_id, department_id):
        self.professor_id = professor_id
        self.department_id = department_id  # Связь многие-ко-многим
# Факультеты
faculty1 = Faculty(1, "IU")
faculty2 = Faculty(2, "RK")

# Кафедры
department1 = Department(1, "Кафедра U5", faculty1.id)
department2 = Department(2, "RK9", faculty2.id)
department3 = Department(3, "IU4", faculty1.id)

# Добавляем кафедры к факультетам
faculty1.departments.extend([department1, department3])
faculty2.departments.append(department2)

# Преподаватели
professor1 = Professor(1, "Ivanov", 50000)
professor2 = Professor(2, "Petrov", 55000)
professor3 = Professor(3, "Sidorov", 60000)
professor4 = Professor(4, "Smirnov", 58000)

# Установка связей многие-ко-многим между преподавателями и кафедрами
professor_department_relations = [
    ProfessorDepartment(professor1.id, department1.id),
    ProfessorDepartment(professor1.id, department3.id),  
    ProfessorDepartment(professor2.id, department1.id),
    ProfessorDepartment(professor3.id, department2.id),
    ProfessorDepartment(professor4.id, department3.id)
]

# Связываем преподавателей с их кафедрами
department_by_id = {dept.id: dept for dept in [department1, department2, department3]}
professor_by_id = {prof.id: prof for prof in [professor1, professor2, professor3, professor4]}

for relation in professor_department_relations:
    professor_by_id[relation.professor_id].departments.append(department_by_id[relation.department_id])

print("Запрос 1: Список всех связанных Преподавателей и Кафедр, отсортированный по Кафедрам")


departments_with_professors = {dept.name: [] for dept in [department1, department2, department3]}

for relation in professor_department_relations:
    dept_name = department_by_id[relation.department_id].name
    prof_name = professor_by_id[relation.professor_id].name
    departments_with_professors[dept_name].append(prof_name)

for dept_name, profs in sorted(departments_with_professors.items()):
    print(f"Department: {dept_name}")
    for prof_name in profs:
        print(f"  - Professor: {prof_name}")
print("\nЗапрос 2: Cписок Кафедр с суммарной зарплатой Преподавателей в каждом отделе, отсортированный по суммарной зарплате")

salary_by_department = {dept.name: 0 for dept in [department1, department2, department3]}

for relation in professor_department_relations:
    prof = professor_by_id[relation.professor_id]
    dept_name = department_by_id[relation.department_id].name
    salary_by_department[dept_name] += prof.salary


for dept_name, total_salary in sorted(salary_by_department.items(), key=lambda x: x[1], reverse=True):
    print(f"Department: {dept_name}, Total Salary: {total_salary}")
print("\nЗапрос 3: Список всех Кафедр, у которых в названии присутствует слово «Кафедра», и список работающих в них Преподавателей.")


print("Checking departments:")
for dept in [department1, department2, department3]:
    print(f"Department: {dept.name}")
    
departments_with_keyword = {
    dept.id: dept.name for dept in [department1, department2, department3] if "Кафедра" in dept.name
}


print("\nDepartments containing 'Кафедра' in the name:")
for dept_id, dept_name in departments_with_keyword.items():
    print(f"Department: {dept_name}")

result = {}
for dept_id, dept_name in departments_with_keyword.items():
    result[dept_name] = [
        professor_by_id[relation.professor_id].name
        for relation in professor_department_relations if relation.department_id == dept_id
    ]

for dept_name, profs in result.items():
    print(f"Department: {dept_name}")
    for prof_name in profs:
        print(f"  - Professor: {prof_name}"""

class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.departments = []


class Department:
    def __init__(self, id, name, faculty_id):
        self.id = id
        self.name = name
        self.faculty_id = faculty_id


class Professor:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.departments = []


class ProfessorDepartment:
    def __init__(self, professor_id, department_id):
        self.professor_id = professor_id
        self.department_id = department_id


def get_professor_department_mapping(professor_department_relations, professors, departments):
    """Создает отображение кафедра-преподаватели."""
    department_by_id = {dept.id: dept for dept in departments}
    professor_by_id = {prof.id: prof for prof in professors}

    for relation in professor_department_relations:
        professor_by_id[relation.professor_id].departments.append(department_by_id[relation.department_id])

    departments_with_professors = {dept.name: [] for dept in departments}
    for relation in professor_department_relations:
        dept_name = department_by_id[relation.department_id].name
        prof_name = professor_by_id[relation.professor_id].name
        departments_with_professors[dept_name].append(prof_name)

    return departments_with_professors


def calculate_total_salary_by_department(professor_department_relations, professors, departments):
    """Рассчитывает суммарную зарплату по кафедрам."""
    department_by_id = {dept.id: dept for dept in departments}
    professor_by_id = {prof.id: prof for prof in professors}

    salary_by_department = {dept.name: 0 for dept in departments}
    for relation in professor_department_relations:
        prof = professor_by_id[relation.professor_id]
        dept_name = department_by_id[relation.department_id].name
        salary_by_department[dept_name] += prof.salary

    return salary_by_department


def get_departments_with_keyword(keyword, professor_department_relations, professors, departments):
    """Возвращает кафедры с указанным ключевым словом и связанных с ними преподавателей."""
    professor_by_id = {prof.id: prof for prof in professors}

    departments_with_keyword = {
        dept.id: dept.name for dept in departments if keyword in dept.name
    }

    result = {}
    for dept_id, dept_name in departments_with_keyword.items():
        result[dept_name] = [
            professor_by_id[relation.professor_id].name
            for relation in professor_department_relations
            if relation.department_id == dept_id
        ]

    return result


# Данные для тестов
faculty1 = Faculty(1, "IU")
faculty2 = Faculty(2, "RK")

# Кафедры
department1 = Department(1, "Кафедра U5", faculty1.id)
department2 = Department(2, "RK9", faculty2.id)
department3 = Department(3, "IU4", faculty1.id)
faculty1.departments.extend([department1, department3])
faculty2.departments.append(department2)

# Преподаватели
professor1 = Professor(1, "Ivanov", 50000)
professor2 = Professor(2, "Petrov", 55000)
professor3 = Professor(3, "Sidorov", 60000)
professor4 = Professor(4, "Smirnov", 58000)

professor_department_relations = [
    ProfessorDepartment(professor1.id, department1.id),
    ProfessorDepartment(professor1.id, department3.id),
    ProfessorDepartment(professor2.id, department1.id),
    ProfessorDepartment(professor3.id, department2.id),
    ProfessorDepartment(professor4.id, department3.id),
]

# Тесты
if __name__ == "__main__":
    import unittest

    class TestFacultySystem(unittest.TestCase):
        def setUp(self):
            self.professors = [professor1, professor2, professor3, professor4]
            self.departments = [department1, department2, department3]
            self.relations = professor_department_relations

        def test_professor_department_mapping(self):
            result = get_professor_department_mapping(self.relations, self.professors, self.departments)
            self.assertIn("Кафедра U5", result)
            self.assertIn("Ivanov", result["Кафедра U5"])

        def test_calculate_total_salary_by_department(self):
            result = calculate_total_salary_by_department(self.relations, self.professors, self.departments)
            self.assertEqual(result["Кафедра U5"], 105000)  # Ivanov + Petrov
            self.assertEqual(result["IU4"], 108000)         # Ivanov + Smirnov

        def test_get_departments_with_keyword(self):
            result = get_departments_with_keyword("Кафедра", self.relations, self.professors, self.departments)
            self.assertIn("Кафедра U5", result)
            self.assertIn("Ivanov", result["Кафедра U5"])

    unittest.main()
