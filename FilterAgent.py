
from database import dbhelper, Post
from words import unwanted_words, filter_targets, map_to_class
from datetime import datetime

class FilterAgent(dbhelper):
    __session = None
    def __init__(self) -> None:
        super().__init__()
        self.__session = next(self.get_session())
        
    def test(self):
        query = "UPDATE post SET full_name = REPLACE(full_name, 'this', '') WHERE id=1;"
        res = self.__session.execute(query)
        self.__session.commit()


    def start_filtering(self):
        print('Starting ....')
        start = datetime.now()    
        
        for table, target_columns in filter_targets.items():
            all_rows = self.__session.query(map_to_class[table]).all()
            for row in all_rows:
                for column in target_columns:
                    for word in unwanted_words:
                        query = f"UPDATE {table} SET {column} = REPLACE({column}, '{word} ', '') WHERE id={row.id}"
                        res = self.__session.execute(query)
                        query = f"UPDATE {table} SET {column} = REPLACE({column}, ' {word}', '') WHERE id={row.id}"
                        res = self.__session.execute(query)
        self.__session.commit()

        end = datetime.now()
        print('Done', end-start)
        return True
        
    def create_sample_data(self):
        self.__session.add(Post(full_name='this maybe', title='is ha', content='nutty'))
        self.__session.add(Post(full_name='issa', title='my nut', content='roll this'))
        self.__session.commit()
        
    def get_session(self):
        session = self._Session()
        try:
            yield session
        finally:
            session.close() 
    