# The frequency table for each note, in each octave, is given:
    # La	  55	  110	 220	 440	  880
    # Si	61.74	123.48	246.96	493.92	987.84
    # Do	65.41	130.82	261.64	523.28	1046.56
    # Re	73.42	146.84	293.68	587.36	1174.72
    # Mi	82.41	164.82	329.64	659.28	1318.56
    # Fa	87.31	174.62	349.24	698.48	1396.96
    # Sol	 98	     196     392     784	 1568

# Write a new MusicNotes class that will implement the iterator protocol, and in each call to next will return the frequency of the next note in the note scale.
# Note that in each octave (column), the frequency is multiplied by 2 from the previous column.
# Think about the stopping condition of the iterator you are building.

# The code below should print the following result:

# notes_iter = iter(MusicNotes())
# for freq in notes_iter:
#      print(freq)
# 55
# 61.74
# 65.41
# 73.42
# 82.41
# 87.31
# 98
# 110
# 123.48
# 130.82
# 146.84
# 164.82
# 174.62
# 196
# 220
# 246.96
# 261.64
# 293.68
# 329.64
# 349.24
# 392
# 440
# 493.92
# 523.28
# 587.36
# 659.28
# 698.48
# 784
# 880
# 987.84
# 1046.56
# 1174.72
# 1318.56
# 1396.96
# 1568

# My solution
import os,time
clear= lambda: os.system('cls')
clear()

class MusicNotes:
    def __init__(self) -> None:
        self.notes= [55,61.74,65.41,73.42,82.41,87.31,98]
        self.list_iter= -1
        self.multi_val= 1
    def __iter__(self):
        return self
    def __next__(self):
        self.list_iter+=1
        if self.notes[len(self.notes)-1] == 1568:
            raise StopIteration
        if self.list_iter >= len(self.notes):
            self.list_iter= 0
        value_to_return= self.notes[self.list_iter]*self.multi_val
        self.notes[self.list_iter]= value_to_return
        if value_to_return == 98:
            self.multi_val=2
        return value_to_return
notes_iter = iter(MusicNotes())
for freq in notes_iter:
    time.sleep(1)
    print(freq)