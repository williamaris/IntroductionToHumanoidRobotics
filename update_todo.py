import os

to_do = []
to_test = []
done = []

for (root, dirs, files) in os.walk('./Matlab'):
    for file in files:
        if file == '.gitkeep': continue

        folder = os.path.basename(root)
        
        if folder == 'Matlab':
            to_do.append(file)

        elif folder == '1-to-test':
            to_test.append(file)

        elif folder == '2-done':
            done.append(file)


with open('TODO.md', 'w') as f:

    f.write('## Tasks progression\n')

    f.write('| To Do    | To Test  | Done     |\n')
    f.write('| :---     | :---     | :---     |\n')

    n_rows = len(to_do) if len(to_do) > len(to_test) else len(to_test)
    n_rows = len(done) if len(done) > n_rows else n_rows

    for idx in range(n_rows):
        
        to_do_el = to_do[idx] if idx < len(to_do) else ""
        to_test_el = to_test[idx] if idx < len(to_test) else ""
        done_el = done[idx] if idx < len(done) else ""

        f.write(
            '| ' + to_do_el + ' ' +
            '| ' + to_test_el + ' ' +
            '| ' + done_el + ' |\n')
