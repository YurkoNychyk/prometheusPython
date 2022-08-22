class CombStr(object):
    text = ''

    def __init__(self, text=''):
        self.text = text

    def count_substrings(self, length=0):
        subs = set()

        if length == 0:
            return 0
        else:
            for index in range(0, len(self.text) + 1):
                if index + length < len(self.text) + 1:
                    subs.add(self.text[index:index+length])
        #print subs
        return len(subs)
