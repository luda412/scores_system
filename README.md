# 🧮 Student Grade Management System (Python)

**파이썬 기반 성적 입력 및 분석 프로그램**  
콘솔을 통해 학생 정보를 입력받고, 평균 및 과목별 통계를 자동 계산하여 포맷화된 텍스트 파일로 저장하는 시스템입니다.

---

## 📘 프로젝트 개요

이 프로젝트는 **데이터 입력 → 검증 → 분석 → 결과 파일 출력**의 전 과정을 객체지향적으로 설계한 프로그램입니다.
입력 예외 처리, 평균 계산 자동화, 시간 기반 로그 출력 등 **기본기에 충실하면서도 확장성 있는 구조**를 지향합니다.

---

## 🚀 주요 기능 요약

| 기능 | 설명 |
|------|------|
| 🎯 학생 수 입력 예외 처리 | 숫자만 입력 가능하며, 잘못된 값 입력 시 재입력 요구 |
| 🧾 학생 정보 유효성 검사 | 이름 + 4과목 점수(총 5개 항목) 형식 검증 및 점수 타입 체크 |
| 📊 학생 평균 및 전체 평균 계산 | 학생별 평균 점수 및 전체 평균 자동 계산 |
| 📈 과목별 최대/최소 점수 분석 | 각 과목의 최고점과 최저점을 자동 탐색 |
| 🕓 결과 파일 포맷화 | 입력 순서, 시간, 이름 순으로 정렬된 결과 저장 |

---

## 🧩 주요 코드 구조

> 전체 코드는 `system` 클래스로 구성되어 있으며,  
> 아래는 핵심 기능만 발췌한 코드입니다.

```python
def input_student_count(self):
    while True:
        try:
            N = int(input("저장할 학생의 수를 입력하세요.:"))
            return N
        except ValueError:
            print("⚠️ 숫자만 입력하세요.\n")
```
- 학생 수는 반드시 숫자로만 입력받습니다.
- try-except를 활용해 문자열, 공백, 특수문자 입력 시 오류를 방지했습니다.
---
```python
    if len(data) != 5:
        print("입력 오류: 이름과 4과목 점수를 입력해주세요.")
        continue
    try:
        data[1:] = list(map(int, data[1:]))
        self.students.append(data)
        break
    except ValueError:
        print("⚠️ 점수는 숫자로 입력해주세요.")
```
- 학생 정보를 공백 기준으로 입력받고, 과목 수가 맞지 않거나 점수 입력이 숫자가 아닐 경우 재입력하도록 유도합니다.
이 과정을 통해 데이터 무결성을 유지합니다.
---

```python
def calculate_individual_avg(self):
    for student in self.students:
        scores = student[1:]
        avg = sum(scores) / len(scores)
        student.append(avg)
        with open("student_Score.txt", "a") as f:
            f.write(f"{student[0]} 학생의 평균: {avg:.2f}\n")
```
- 각 학생별 평균 점수를 계산해 소수점 둘째 자리까지 반올림해 저장합니다.
- 또한 결과를 파일에 직접 기록하여 재확인 및 관리가 용이합니다.

---

```python
def calculate_totoal_avg(self, total_avg):
    total_score = sum(student[5] for student in self.students)
    self.total_avg = total_score / (len(self.students) * 4)
    with open("student_Score.txt", "a") as f:
        f.write(f"전체 평균: {self.total_avg}\n")
```
- 전체 학생의 총점을 기반으로 전체 평균을 계산합니다.
- 학생 수와 과목 수를 기준으로 자동 조정되어, 입력 인원 변경에도 안정적으로 동작합니다.
---

```python
def file_write_scores(self):
    with open("student_Score.txt", "a") as f:
        local_time = time.localtime()
        f.write("작성일: {0}년 {1}월 {2}일 {3}시 {4}분\n".format(
            local_time.tm_year, local_time.tm_mon, local_time.tm_mday,
            local_time.tm_hour, local_time.tm_min))
```
- 출력 파일에 작성 시간을 자동 기록하여, 실행 시점의 결과를 명확히 남길 수 있습니다.
- (시간 순 기록 → 데이터 관리의 신뢰성 확보)

### 입력 예시
```
저장할 학생의 수를 입력하세요.: 3
1번째 학생의 정보를 입력하세요: 홍길동 90 85 80 75
2번째 학생의 정보를 입력하세요: 이순신 100 90 95 85
3번째 학생의 정보를 입력하세요: 유관순 85 80 70 65
```

### 결과 파일 예시
```
성적 파일 순서는 이름, 국어, 수학, 영어, 과학 입니다.
작성일: 2025년 11월 11일 14시 27분
['이', 100, 95, 90, 85]
['김', 95, 90, 80, 70]
['박', 100, 90, 95, 80]
['최', 80, 95, 70, 85]
['정', 90, 80, 85, 70]
이 학생의 평균: 92.50
김 학생의 평균: 83.75
박 학생의 평균: 91.25
최 학생의 평균: 82.50
정 학생의 평균: 81.25
전체 평균: 86.25
국어 - 최소 점수: 80, 최대 점수: 100
수학 - 최소 점수: 80, 최대 점수: 95
영어 - 최소 점수: 70, 최대 점수: 95
과학 - 최소 점수: 70, 최대 점수: 85
```



