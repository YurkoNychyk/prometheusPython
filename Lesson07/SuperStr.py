class SuperStr (str):
    def __init__(self, s = ''):
        super(SuperStr, self).__init__(s)

    def  is_repeatance(self, s = ''):
        if type(s) == str:
            return len(self) == self.count(str(s)) * len(s) and len(s) > 0
        else:
            return False

    def is_palindrom(self):
        start_ch = 0
        starting_half = ''
        ending_half = ''
        for end_ch in range(len(self)-1, len(self)//2-1, -1):
            starting_half += self[start_ch]
            ending_half += self[end_ch]
            start_ch += 1
        starting_half.lower()
        ending_half.lower()
        return starting_half == ending_half or self == ''

