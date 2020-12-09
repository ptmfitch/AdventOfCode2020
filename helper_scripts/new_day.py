import datetime

dayofmonth = datetime.date.today().day
print('Setting up files for today ({} December)'.format(dayofmonth))


def create_file(filepath, content=''):
    try:
        with open(filepath, 'x') as fp:
            print('Created file {}'.format(filepath))
            fp.write(content)
    except FileExistsError:
        print('File {} already exists'.format(filepath))


script_template = "with open(\"inputs/day{}.txt\") as input_file:\n" \
                  "    for line in input_file:\n" \
                  "        pass\n".format(dayofmonth)


create_file('../inputs/day{}.txt'.format(dayofmonth))
create_file('../inputs/day{}_example.txt'.format(dayofmonth))
create_file('../day{}part1.py'.format(dayofmonth), script_template)
create_file('../day{}part2.py'.format(dayofmonth), script_template)
