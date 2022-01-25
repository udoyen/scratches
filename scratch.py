import itertools
import re
import profile

sample = r"""
         2020-06-04 21:04:59,661 Worker-9 DEBUG [com.test.bs.engine.Action                       ] Choose engine based on parameters: jobid='1A23456789', jobcode=null
         2020-06-04 21:04:59,662 Worker-9 DEBUG [com.test.bs.engine.Action                        ] Performing existence check for object_id='1AE1C4321' using sql: select first_name from employees where employee_id=?
         2020-06-04 21:04:59,662 Worker-9 DEBUG [com.sql.ConnectionProviderJBoss            ] --> Using DB connection from pool java:jboss/datasources: [#21837933]
         2020-06-04 21:04:59,665 Worker-9 DEBUG [com.sql.ConnectionProviderJBoss              ] <-- Connection [#21837933] returned to DB pool. Statement=[closed]. ResultSet=[closed].
         """

sample2 = """
        Balanced Quantum Classical Evolutionary Algorithm(BQCEA)Muhammad Shahid, Hasan Mujtaba, Muhammad Asim, Omer BegAbstractWith advancement in Quantum computing, classical algorithms are adapted and integratedwith Quantum properties such as qubit representation and entanglement. Although theseproperties perform better however pre-mature convergence is the main issue in QuantumEvolutionary Algorithms(QEA) because QEA uses only the best individual to update quan-tum population. In this paper, we introduced a new way to update the quantum populationof QEA to avoid premature convergence.
"""


def m_replace():
    digits = [str(i) for i in range(0, 10)]
    t = []
    for i in sentences:
        print(f"i: {i}")
        for j in digits:
            i = i.replace(j, '')
        t.append(i)
    print(t[0:5])


if __name__ == '__main__':

    ##################################################################################

    # pattern = re.compile(r"select.*\?\n.*\n.*")
    # try:
    #     with open('log.txt') as f:
    #         line = f.read()
    #         for match in re.finditer(pattern, line):
    #             print(f'lines: {match.group()}')
    # except Exception as e_rr:
    #     print('Error: {}'.format(e_rr))

    # m = [{'label': "['Tennessee'] 22960 Packages", 'value': 'TN'},
    #      {'label': "['Illinois'] 6277 Packages", 'value': 'IL'},
    #      {'label': "['California'] 4 Packages", 'value': 'CA'}, ]
    #
    # for i in range(0, 3):
    #     m[i]['label'] = m[i]['label'].replace("['", "").replace("']", "")
    # print(m)

    ####################################################################################

    # test = r"""
    # chartData.push({
    #     date: newDate,
    #     visits': 9710,
    #     color: "#016b92",
    #     description: "9710"
    # })
    # var newDate = new Date()
    # newDate.setFullYear(
    #     2007,
    #     10,
    #     1);"""
    #
    # m = re.search(r".*newDate\.setFullYear(\(\n.*\n.*\n.*\));", test, re.DOTALL)
    #
    # print(type(m))
    # print(m.group(1).rstrip("\n").replace("\n", "").replace(" ", ""))

    ####################################################################################

    # A = [[[['a', 'b'], ['e', 'f']], ['e', 'g']],
    #      [[['d', 'r'], ['d', 'g']], ['l', 'm']],
    #      [[['g', 'd'], ['e', 'r']], ['g', 't']]]

    # pattern = re.compile(r"^(.*\(BQCEA\))(.*Beg)(Abstract)(With.*)")
    #
    # try:
    #     with open('sample.txt', 'r') as f:
    #         line = f.read()
    #         # remove some unwanted characters
    #         r = line.replace('\\n', "").replace("'", "").replace("\n", "")
    #         print(r)
    #         for match in re.finditer(pattern, r):
    #             print(match.group(1))
    #             print('\n')
    #             print(match.group(2))
    #             print('\n')
    #             print(match.group(3))
    #             print(match.group(4))
    # except Exception as er:
    #     print(er)

    ###########################################################################################

    # container = []
    # for index, item in enumerate(A):
    #     f_1 = itertools.chain(A[index][0] + [A[index][1]])
    #     container.append(list(f_1))
    #
    # m = [list(itertools.chain(i[0] + [i[1]])) for i in A]
    #
    #
    # print(container)
    # print(m)

    ############################################################################################

    # import keyboard  # using module keyboard
    #
    # while True:  # making a loop
    #     key = input('Please press any key: ')
    #     try:  # used try so that if user pressed other than the given key error will not be shown
    #         print('Key: {}'.format(key))
    #         if keyboard.read_key() == 'q':  # if key 'q' is pressed
    #             print('You Pressed A Key! {}'.format(key))
    #             break  # finishing the loop
    #     except Exception as e_rr:
    #         print('Exception: {} Type: {}'.format(e_rr, type(e_rr)))
    #         break

    #####################################################################################################

    # checker = 'C1:52,11'
    # present = False
    # new_file = []
    # with open('change.txt', 'r') as f:
    #     for line in f:
    #         if checker[:2] == line[:2] and checker[3:] is not line[3:]:
    #                 new_file.append(line.replace(line[3:].strip('\n'), checker[3:]))
    #                 present = True
    #         else:
    #             new_file.append(line)
    #
    # with open('change.txt', 'w') as f:
    #     f.writelines(new_file)
    #     if not present:
    #         f.writelines('\n')
    #         f.writelines(checker)

    ###################################################################################################

    # Department_List = ["Department_1", "Department_2", "Department_2"]
    #
    # Category_List = ["Cat_1", "Cat_3", "Cat_1", "Cat_5", "Cat_2", "Cat_2"]
    #
    # sublist = {'SubCategory': [j for j in Department_List for i in Category_List if i[-2:] == j[-2:]]}
    #
    # print(sublist)

    #############################################################################################


    sentences = ['So there is no way for me to plug it in here in the US unless I go by a converter.',
     'Good case, Excellent value.',
     'Great for the jawbone.',
     'Tied to charger for conversations lasting more than 45 minutes.MAJOR PROBLEMS!!',
     'The mic is great.']
    print(sentences[0:5])

    profile.run('m_replace()')

