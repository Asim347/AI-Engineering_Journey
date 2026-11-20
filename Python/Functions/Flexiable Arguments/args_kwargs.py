# *args → Accepts multiple positional arguments (stored as a tuple).
# **kwargs → Accepts multiple keyword arguments (stored as a dictionary).
def calculate(*args):
    total = sum(args)

    return total

print(calculate(10,20,30))


def student_info(**kwargs):

    for key, value in kwargs.items():
        print(f"{key} : {value}")


student_info(name="Asim", Age=21, Coures="Python")

# Using both together

def show(*args, **kwargs):
    print("Arguements :",args)

    print("Details : ", kwargs)

show(10,20,Shop='Pages',Price = 21)