def is_report_safe(report: list):
    direction = None
    for i in range(1, len(report)):
        change = report[i - 1] - report[i]
        if is_bad_level(change, direction):
            return False
        direction = get_direction(direction, change)
    return True


def with_problem_dampener(report: list):
    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def get_direction(direction, change):
    if direction is not None:
        return direction
    return "Increasing" if change > 0 else "Decreasing"


def is_bad_level(change, direction):
    if abs(change) > 3:
        return True
    if change == 0:
        return True
    if direction == "Increasing" and change < 0:
        return True
    if direction == "Decreasing" and change > 0:
        return True
    return False


def main():
    with open("two/input.txt") as file:
        safe_reports = 0
        while line := file.readline():
            report = [int(level) for level in line.split()]
            if is_report_safe(report):
                safe_reports += 1
                continue
            if with_problem_dampener(report):
                safe_reports += 1
                continue

        print(f"safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
