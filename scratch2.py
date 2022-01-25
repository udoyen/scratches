import pandas as pd
import sys
import profile
import memory_profiler
import pandas as pd


@memory_profiler.profile
def teams():
    return (f'#team-{i}-{j:03d}' for i in ['aad', 'gcp', 'mws'] for j in range(1, 381))

@memory_profiler.profile
def less_team():
    return list((f'team-gcp-{j:02d}' for j in range(1, 381)))

data = {}

@memory_profiler.profile
def data_display():
    # global df
    data['GCP'] = [f'team-gcp-{j:02d}' for j in range(1, 381)]
    data['MENTORS-GCP'] = " "
    data['AAD'] = list((f'team-aad-{j:02d}' for j in range(1, 381)))
    data['MENTORS-AAD'] = " "
    data['MWS'] = list((f'team-mws-{j:02d}' for j in range(1, 381)))
    data['MENTORS-MWS'] = " "

    # print(data)
    df = pd.DataFrame(data)

    return df

sample = "106_LB01_GP61_HAL;LB01;10892;DIGITAL;0;0;0;0;;;Smutsigt tilluftsfilter;;"
check = """"Prefix": "106_LB01_GP61","""

if __name__ == '__main__':

    import re

    print(len(re.split(r"\s |;", sample)))
    sam = re.split(r"; |\s |;", sample)
    che = re.split(r"\" |\s |: |\"", check)
    print(che)
    print(sam)
    for i in sam:
        print(f'i :{i}')
        for j in che:
            if i == j:
                print(f'found: {j}')
    # for j in check.split()
    # teams()

    # profile.run("[f'#team-{i}-{j:03d}' for i in ['aad', 'gcp', 'mws'] for j in range(1, 381)]")
    # less_team()
    # print({ k: [f'#team-{i}-{j:03d}' for i in ['aad', 'gcp', 'mws'] for j in range(1, 381)] for k in ['aad', 'gcp', 'mws']})
    print(data_display())
