workers = {}

def add_employee(surname, position, efficiency, projects):
    workers[surname] = {
        "Position": position,
        "Efficiency": efficiency,
        "Projects": projects
    }


def get_all_surnames():
    return list(workers.keys())


def get_most_efficient_employee():
    if not workers:
        return None
    return max(workers, key=lambda surname: workers[surname]["Efficiency"])


def get_all_positions():
    return [worker["Position"] for worker in workers.values()]


add_employee("Джо", "Создатель", 95, ["Project A", "Project B", "Project C"])
add_employee("Джонсон", "Менеджер", 90, ["Project D", "Project E", "Project F"])
add_employee("Виллиам", "Тестер", 85, ["Project G", "Project H", "Project I"])


print("Всі Прізвища:", get_all_surnames())
print("Найефективніший працівник:", get_most_efficient_employee())
print("Всі посади:", get_all_positions())
