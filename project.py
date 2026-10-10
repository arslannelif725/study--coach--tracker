import sys
from tabulate import tabulate
def main():
    sessions = []
    print('=== Study Coach & Tracker ===')

    while True:
        try:
            subject = input('Course Name (Press Enter to exit): ').strip()
            if not subject:
                break
            duration = int(input('Studying Time (minutes): '))
            questions = int(input('Number of Questions Solved: '))
            session = add_session(subject, duration, questions)
            sessions.append(session)
        except ValueError as e:
            print(f'Error: {e}\n')
            continue
    if not sessions:
        sys.exit('no study data has been entered.')
    print('\n--- Study History ---')
    print(format_table(sessions))
    summary = calculate_summary(sessions)
    print('\n--- Summary of Performance ---')
    print(f"Total Working Time: {summary['total_duration']} minutes")
    print(f"Total Number of Questions: {summary['total_questions']} questions")
    print(f"Average per Question: {summary['avg_time_per_question']:.2f} minutes/question")

def add_session(subject, duration, questions):
    if not subject:
        raise ValueError('the course name cannot be empty.')
    if duration <= 0:
        raise ValueError('the duration must be greater than 0.')
    if questions < 0:
        raise ValueError('the number of questions cannot be negative.')
    return {
        'subject': subject,
        'duration': duration,
        'questions': questions
    }
def calculate_summary(sessions):
    if not sessions:
        return {'total_duration': 0, 'total_questions': 0, 'avg_time_per_question':0.0}
    total_duration = sum(s['duration'] for s in sessions)
    total_questions = sum(s['questions'] for s in sessions)
    avg_time = (total_duration / total_questions) if total_questions > 0 else 0.0
    return {
        'total_duration': total_duration,
        'total_questions': total_questions,
        'avg_time_per_question': avg_time
    }
def format_table(sessions):
    headers = ['Course Name', 'duration (minutes)', 'Number of Questions']
    rows = [[s['subject'], s['duration'], s['questions']] for s in sessions]
    return tabulate(rows, headers=headers, tablefmt='grid')
if __name__ =='__main__':
    main()
