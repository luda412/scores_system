import time
class system:

    def __init__(self):
        print("성적 입력 프로그램을 시작합니다. 입력 순서는 이름, 국어, 수학, 영어, 과학 입니다. (공백으로 구분합니다.)")
        self.students = []
        self.total_avg = 0

    def input_student_count(self):
        while True:
            # 학생의 수는 정수로만 입력 받음
            try:
                N = int(input("저장할 학생의 수를 입력하세요.:"))
                return N
            # 정수가 아닌 경우 expect 발생 시키고 다시 try
            except ValueError:
                print(f"숫자만 입력하세요")
                print()

    def input_student_info(self, N):
        #입력 받은 학생의 수 N 만큼 2차원 리스트 students 생성 | range가 N까지인 이유는 range(N)인 경우 0부터 N-1까지 라서.
        for i in range(N):
            while True:
                data = input(f"{i+1}번째 학생의 정보를 입력하세요: ").split()
                # 이름 + 4과목 → 총 5개 항목이어야 함
                if len(data) != 5:
                    print("입력 오류: 이름과 4과목의 점수를 정확히 입력하세요 (예: 홍길동 90 80 70 60)")
                    continue
                try:
                    # 점수 부분만 int로 변환
                    data[1:] = list(map(int, data[1:]))  # data 안에 직접 변환
                    self.students.append(data)  # ex: ['lee', 90, 80, 70, 60]
                    break
                except ValueError:
                    print(f"점수는 숫자로 입력해주세요.")

    def print_scores(self):
        for student in self.students:
            print(f"{student[0]} 학생의 국어 점수: {student[1]}, 수학 점수: {student[2]}, 영어 점수: {student[3]}, 과학 점수: {student[4]}")

    def calculate_individual_avg(self):
        # 반복 변수가 student인 이유는 students의 학생의 갯수 만큼 for문을 돈다. EX, 2명의 학생일 경우 student는 2번 돌게됨.
        for student in self.students:
            scores = student[1:]
            # student 리스트에 합산 점수 넣기
            student.append(sum(scores))
            avg = sum(scores) / len(scores)
            # 평균의 인덱스 studnet[5] | student 리스트에 평균 점수 넣기
            student.append(avg)
            # print(f"{student[0]} 학생의 합산 점수:{sum(scores)}")
            # print(f"{student[0]} 학생의 평균: {avg:.2f}")
            # print()
            with open("student_Score.txt", "a") as f:
                findividual_avg = f"{student[0]} 학생의 평균: {avg:.2f}\n"
                f.write(findividual_avg)

    def calculate_totoal_avg(self, total_avg):
        # 전체 평균
        total_score = 0
        for student in self.students:
            total_score += student[5]

        self.total_avg = total_score / (len(self.students) * 4)
        # print(f"전체 평균: {self.total_avg}")
        # print()
        with open("student_Score.txt", "a") as f:
            ftotal_avg_string = f"전체 평균: {self.total_avg}"
            f.write(f"{ftotal_avg_string}\n")

        return self.total_avg
    def calculate_min_max_subjects(self):
        kor_scores = [int(student[1]) for student in self.students]
        max_kor = max(kor_scores)
        min_kor = min(kor_scores)
        # print(f"국어 최소 점수: {min_kor}, 국어 최대 점수: {max_kor}")
        # print()

        math_scores = [int(student[2]) for student in self.students]
        max_math = max(math_scores)
        min_math = min(math_scores)
        # print(f"수학 최소 점수: {min_math}, 수학 최대 점수: {max_math}")
        # print()

        eng_scores = [int(student[3]) for student in self.students]
        max_eng = max(eng_scores)
        min_eng = min(eng_scores)
        # print(f"영어 최소 점수: {min_eng}, 영어 최대 점수: {max_eng}")
        # print()

        sci_scores = [int(student[4]) for student in self.students]
        max_sci = max(sci_scores)
        min_sci = min(sci_scores)
        # print(f"과학 최소 점수: {min_sci}, 과학 최대 점수: {max_sci}")
        # print()

        with open("student_Score.txt", "a") as f:
            fkor_string = f"국어 - 최소 점수: {min_kor}, 최대 점수: {max_kor}"
            fmath_string = f"수학 - 최소 점수: {min_math}, 최대 점수: {max_math}"
            feng_string = f"영어 - 최소 점수: {min_eng}, 최대 점수: {max_eng}"
            fsci_string = f"과학 - 최소 점수: {min_sci}, 최대 점수: {max_sci}"
            f.write(f"{fkor_string}\n")
            f.write(f"{fmath_string}\n")
            f.write(f"{feng_string}\n")
            f.write(f"{fsci_string}\n")
        print("프로그램 종료.")

    def file_write_scores(self):
        with open("student_Score.txt", "a") as f:
            fstring = "\n성적 파일 순서는 이름, 국어, 수학, 영어, 과학 입니다.\n"
            f.write(fstring)
            local_time = time.localtime()
            time_string = "작성일: {0}년 {1}월 {2}일 {3}시 {4}분\n".format(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min)
            f.write(time_string)
            for student in self.students:
                temp_list = student[:]
                del temp_list[5:]
                score_string = str(temp_list)+"\n"
                f.write(score_string)


# 생성된 객체를 하나만 가지고 돌기 떄문에 생성된 students 리스트는 모두 같은 참조 주소 값을 가진다.
system = system()
N = system.input_student_count()
system.input_student_info(N)
# system.print_scores()
# print(f"{system.students[0:]}")
# system.dict_adapter_list()
system.file_write_scores()
system.calculate_individual_avg()
system.calculate_totoal_avg(system.total_avg)
system.calculate_min_max_subjects()