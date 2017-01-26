class All_cards(object):
    def __init__(self,nums,pict):
        self.nums = nums
        self.pict = pict
    def __str__(self):
        return("Nums: {}, Pict: {}".format(self.nums,self.pict)) 
    def making(self):
        all_cards = []
        for p in self.pict:
            for n in self.nums:
                all_cards.append(p+n)
        return all_cards
class Count_points(object):
    def __init__(self,card):
        self.card = card
    def __str__(self):
        return ("Your card is: {}".format(self.card))
    def points(self):
        if self.card[1] in "KQJT":
            return 10
        elif self.card[1] in " A23456789":
            return " A23456789".index(self.card[1])

