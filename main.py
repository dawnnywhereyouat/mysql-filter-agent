from database import dbhelper
from FilterAgent import FilterAgent
from words import filter_targets

def a():
    dbhelper().create_db()
    FilterAgent().create_sample_data()

if __name__ == '__main__':
    a()
    print(FilterAgent().start_filtering())