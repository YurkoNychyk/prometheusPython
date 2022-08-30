from holes_counter import count_holes
from morze_coding import encode_morze
from saddle_point import saddle_point
from most_frequent_words import find_most_frequent
from base_conversion import convert_n_to_m
print count_holes('123')
print
print count_holes(906)
print
print count_holes('001')
print
print count_holes(-8)
print
print count_holes(-8.0)

print count_holes(000000000010)
print count_holes(1234)

print "Morze"
print encode_morze('Morze code') == "^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^"
print encode_morze('Prometheus') == "^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^"
print encode_morze('SOS') == "^_^_^___^^^_^^^_^^^___^_^_^"
print encode_morze("SOS")
print encode_morze('1')
print "Sadle point \n"
print saddle_point([[1,2,3],[3,2,1]]) == False
print saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]) == (1,2)
print saddle_point([[21]]) == (0,0)
print saddle_point([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                    [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
                    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
                    [13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
                    [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
                    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
                    [16, 15, 14, 13, 12, 11, 10, 9, 8, 7],
                    [17, 16, 15, 14, 13, 12, 11, 10, 9, 8],
                    [18, 17, 16, 15, 14, 13, 12, 11, 10, 9],
                    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]) == (9,9)


print find_most_frequent('Hello,Hello, my dear!')
print find_most_frequent('to understand recursion you need first to understand recursion...')
print find_most_frequent('Mom! Mom! Are you sleeping?!!!')
print find_most_frequent('')

print "Conversion"


print convert_n_to_m('qweasd', 33, 36)
print convert_n_to_m('000', 10, 2)

print saddle_point([[13]])
print saddle_point([[5,5,5], [5,5,6], [5,4,5]])
