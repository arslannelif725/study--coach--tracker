import pytest
from project import add_session, calculate_summary, format_table
def test_add_sessions_valid():
    session = add_session('Mathematic', 60, 30)
    assert session == {'subject': 'Mathematic', 'duration': 60, 'questions': 30}
def test_add_session_invalid():
    with pytest.raises(ValueError):
        add_session('', 60, 30)
    with pytest.raises(ValueError):
        add_session('Physic', -10, 20)
    with pytest.raises(ValueError):
        add_session('Chemistry', 45, -5)
def test_calculate_summary():
    sessions = [
        {'subject': 'Mathematic', 'duration': 60, 'questions': 30},
        {'subject': 'Turkish', 'duration': 30, 'questions': 30}
    ]
    summary = calculate_summary(sessions)
    assert summary['total_duration'] == 90
    assert summary['total_questions'] == 60
    assert summary['avg_time_per_question'] == 1.5

def test_format_table():
    sessions = [{'subject': 'History', 'duration': 45, 'questions':15}]
    table_str = format_table(sessions)
    assert 'History' in table_str
    assert '15' in table_str
