from django.db import models
from django.contrib.auth.models import User

from random import randint


#class User(models.Model):
#    username = models.CharField(max_length=50)
#    password = models.CharField(max_length=255)

class Attributes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll1 = models.IntegerField(default=7)
    roll2 = models.IntegerField(default=7)
    roll3 = models.IntegerField(default=7)
    roll4 = models.IntegerField(default=7)
    roll5 = models.IntegerField(default=7)
    roll6 = models.IntegerField(default=7)

    def __str__(self):        
        return "user:" + self.user.username + ", roll 1:" + str(self.roll1) + ", roll 2:" + str(self.roll2) + ", roll 3:" + str(self.roll3) + ", roll 4:" + str(self.roll4) + ", roll 5:" + str(self.roll5) + ", roll 6:" + str(self.roll6)

    def get_rolls(self):
        return [ self.roll1, self.roll2, self.roll3, self.roll4, self.roll5, self.roll6 ]

    def roll(self):
        lowcount = 0
        highcount = 0

        rolls = [0, 0, 0, 0, 0, 0]
        accumulated = 0

        min = 6
        max = 18

        results = Attributes.modify_roll(lowcount, highcount, randint(min, max))
        lowcount = results['low']
        highcount = results['high']
        rolls[0] = results['roll']
        accumulated += rolls[0]

        if accumulated > 17:
            min = 3

        results = Attributes.modify_roll(lowcount, highcount, randint(min, max))
        lowcount = results['low']
        highcount = results['high']
        rolls[1] = results['roll']
        accumulated += rolls[1]

        if accumulated > 34:
            min = 3
        else:
            min = 6

        results = Attributes.modify_roll(lowcount, highcount, randint(min, max))
        lowcount = results['low']
        highcount = results['high']
        rolls[2] = results['roll']
        accumulated += rolls[2]

        if accumulated > 55:
            min = 3
            max = 16
        elif accumulated <= 30:
            min = 13
            max = 18
        elif accumulated > 40:
            min = 3

        results = Attributes.modify_roll(lowcount, highcount, randint(min, max))
        lowcount = results['low']
        highcount = results['high']
        rolls[3] = results['roll']
        accumulated += rolls[3]

        if accumulated > 70:
            min = 3
            max = 16
        elif accumulated > 55:        
            min = 3
        elif accumulated <= 40:
            min = 13
            max = 18
        else:
            min = 6
            max = 18

        results = Attributes.modify_roll(lowcount, highcount, randint(min, max))
        lowcount = results['low']
        highcount = results['high']
        rolls[4] = results['roll']
        accumulated += rolls[4]

        if accumulated > 85:
            min = 3
            max = 16
        elif accumulated > 65:
            min = 3
        elif accumulated <= 50:
            min = 13
            max = 18
        else:
            min = 6
            max = 18

        results = Attributes.modify_roll(lowcount, highcount, randint(min, max))
        lowcount = results['low']
        highcount = results['high']
        rolls[5] = results['roll']
        accumulated += rolls[5]

        if accumulated > 95:
            min = 3
            max = 16
        elif accumulated > 75:
            min = 3
        elif accumulated <= 60:
            min = 13
            max = 18
        else:
            min = 6
            max = 18

        Attributes.modify_roll(lowcount, highcount, randint(min, max))
        extraroll = results['roll']

        temprolls = rolls
        temprolls.sort()
        minvalue = temprolls[0]
        maxvalue = temprolls[5]
        if maxvalue < 13 or (accumulated/6) <= 11:
            extraroll = 18

        for index, item in enumerate(rolls):
            if rolls[index] == minvalue and extraroll > minvalue:
                rolls[index] = extraroll
                break
        
        self.roll1 = rolls[0]
        self.roll2 = rolls[1]
        self.roll3 = rolls[2]
        self.roll4 = rolls[3]
        self.roll5 = rolls[4]
        self.roll6 = rolls[5]
    
    def modify_roll(low, high, roll):
        minroll = 8
        maxroll = 18
        reroll = False
        if roll < 7:
            roll = 7

        if roll < 9:
            if low == 0:#keep the roll, increment low
                low = low + 1
            elif low < 2:
                test = randint(1, 100)
                if test > 30:
                    minroll = 9
                    reroll = True
                else:
                    low = low + 1
            elif low == 2:
                minroll = 9
                maxroll = 17
                reroll = True

        if roll >= 16:
            if high < 1:
                high = high + 1
            elif high <= 3:
                test = randint(1, 100)
                if test > 60:
                    maxroll = 16
                    reroll = True
                else:
                    high = high + 1
            else:
                test = randint(1, 100)
                if test > 10:
                    maxroll = 16
                    reroll = True
        
        if reroll:
            roll = randint(minroll, maxroll)

        return { 'low': low, 'high': high, 'roll': roll }


        
        
        