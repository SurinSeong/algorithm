# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## 복불복 팀플 조편성
# * 20명의 교육생 --> 한 팀당 5명 (무작위 뽑기)
# * pandas의 read_csv 이용, 파일 읽은 후, 파이썬 알고리즘 작성

import numpy as np
import pandas as pd


# 함수 --> 작동 안됨..
# 팀 만들기
def make_teams(df, team_mem):
    
    # 전체 인원수
    total = len(df)
    # sample() 사용해서 순서 섞기
    new_df = df.sample(frac=1, replace=False)
    # 팀 수 정하기
    team_num = total // team_mem
    
    # 전체 팀 넣는 리스트
    teams = []
    for i in range(team_num):
        start_i = i * team_mem
        team = new_df[start_i : start_i + team_mem]
        teams.append(team)
        
    # 나머지 찾기
    rem = total % team_num
    if rem != 0:
        rem_df = new_df[total-rem:]
    else:
        rem_df = None

    # 나머지 팀에 넣기
    if rem_df is None:
        print('남은 멤버가 없습니다.')
    else:
        n = len(rem_df)
        for i in range(len(teams)):
            teams[i].loc[len(teams[i])] = [rem_df[i]]
            
        # final_teams = pd.DataFrame(teams)
    return teams
    


# +
# 다른 함수 --> 뭔가 맘에 안들게 작동됨..
# 나머지 있나 확인 후 나머지 있으면 그 수만큼 먼저 배치 하고 시작하기

def mk_teams(name_df, mem_num):
    n = len(name_df)
    remain = n % mem_num
    if remain != 0:
        for i in range(remain):
            name_df.loc[i] = None
        n = len(name_df)
        new_df = np.array(name_df).reshape(-1, mem_num+1)
    else:
        new_df = np.array(name_df).reshape(-1, mem_num)
    return new_df


# +
# 변수
# path
path = '../Desktop/multicampus/algorithm/students.csv'

# 데이터프레임 생성
students = pd.read_csv(path, encoding='cp949')

# -

mk_teams(students, 3)

# +
# 메인
# 남는 인원이 있다면?
# 예를 들어서 21명인데 4명이 한팀이 기본이라면?
# 남은 사람을 첫 번째 팀에 넣는다.

np.random.seed(100)
all_teams = make_teams(students, 3)
print(all_teams)


# +
# 총 인원수가 팀원수로 딱 나누어 떨어질 경우

# path
path = '../Desktop/multicampus/algorithm/students.csv'

# 데이터프레임 생성
students = pd.read_csv(path, encoding='cp949')
# print(len(students))

# sample() 사용해서 순서 섞기
students_df = students.sample(frac=1, replace=False, ignore_index=False)

# 팀원수 입력
team_mem = int(input("팀 당 인원수 : "))

# 총 인원 수
total_mem_num = len(np.array(students_df))

# 팀 수
team_num = total_mem_num // team_mem

# 팀 배정

for i in range(team_num):
    start_index = i * team_mem
    team = students_df[start_index : start_index + team_mem]
    print(f'TEAM {i+1}\n{team}\n')
    # file_name = f'team {i+1}'
    # team.to_csv(file_name, index=False)

# -




