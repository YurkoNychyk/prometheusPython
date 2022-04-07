#Lesson5.py
from cleaning_lists import clean_list 
from counter_a_b import counter
from super_fibonacci import super_fibonacci
from file_search import file_search

print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
print file_search(['C:'], 'ideas.txt')
print file_search(['C:', ['eee', 'rrr', 'ttt'], ['yyy', 'ideas.txt']], 'ideas.txt') 
