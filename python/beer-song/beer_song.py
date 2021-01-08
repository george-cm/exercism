def recite(start, take=1):
    bottles = Bottles(start, take)
    return bottles.recite()


class Bottles(object):
    def __init__(self, start, take=1):
        self.start = start
        self.take = take

    def _recite_verse(self, num):
        if num == 0:
            verse1 = "No more bottles of beer on the wall, no more bottles of beer."
            verse2 = "Go to the store and buy some more, 99 bottles of beer on the wall."
        elif num == 1:
            verse1 = f"{num} bottle of beer on the wall, {num} bottle of beer."
            verse2 = f"Take it down and pass it around, no more bottles of beer on the wall."
        else:
            verse1 = f"{num} bottles of beer on the wall, {num} bottles of beer."
            noun2 = "bottles" if num - 1 > 1 else "bottle"
            verse2 = f"Take one down and pass it around, {num-1} {noun2} of beer on the wall."

        return [verse1, verse2]

    def recite(self):
        out = []
        for i in range(self.take):
            out.extend(self._recite_verse(self.start - i))
            out.append('')
        return out[:-1]
