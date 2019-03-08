import os

dir_path = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
result_dir = os.path.join(base_dir, "Results")

# x = list(filter(os.path.isdir, os.listdir(result_dir+"\\")))
x = [allbuild for allbuild in os.listdir(result_dir+"\\") if os.path.isdir(os.path.join(result_dir+"\\", allbuild))]
print(x)

z = x
for y in x:
    if y.__contains__("."):
        z.remove(y)

print(z)