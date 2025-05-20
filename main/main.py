from figures import Triangle, Rectangle, Trapeze, Parallelogram, Circle

def parse_figure(line):
    parts = line.strip().split()
    if not parts:
        return None
    name = parts[0]
    try:
        numbers = list(map(float, parts[1:]))
    except ValueError:
        return None

    if name == "Triangle" and len(numbers) == 3:
        return Triangle(*numbers)
    elif name == "Rectangle" and len(numbers) == 2:
        return Rectangle(*numbers)
    elif name == "Trapeze" and len(numbers) == 4:
        return Trapeze(*numbers)
    elif name == "Parallelogram" and len(numbers) == 3:
        return Parallelogram(*numbers)
    elif name == "Circle" and len(numbers) == 1:
        return Circle(*numbers)
    return None

figures = []

for file in ["input01.txt", "input02.txt", "input03.txt"]:
    try:
        with open(file, "r") as f:
            for line in f:
                fig = parse_figure(line)
                if fig:
                    figures.append(fig)
    except FileNotFoundError:
        continue

max_area = max(figures, key=lambda f: f.area(), default=None)
max_perimeter = max(figures, key=lambda f: f.perimeter(), default=None)

with open("output.txt", "w") as out:
    if max_area:
        out.write(f"Фігура з найбільшою площею: {max_area.__class__.__name__}, площа = {max_area.area():.2f}\n")
    if max_perimeter:
        out.write(f"Фігура з найбільшим периметром: {max_perimeter.__class__.__name__}, периметр = {max_perimeter.perimeter():.2f}\n")
