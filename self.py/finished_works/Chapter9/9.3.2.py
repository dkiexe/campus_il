# Following the previous exercise, write a function called my_mp4_playlist defined as follows:

# def my_mp4_playlist(file_path, new_song):
# The function accepts as parameters:

# Path to the file (string).
# Just like in the previous exercise, the file represents a playlist of songs and has a fixed format built from the name of the song, 
# the name of the performer (singer/band) and the length of the song, separated by a semicolon (;) without spaces.

# An example of an input file called songs.txt:
# Tudo Bom; Static and Ben El Tavori; 5:13;
# I Gotta Feeling; The Black Eyed Peas; 4:05;
# Instrumental; Unknown; 4:15;
# Paradise; Coldplay; 4:23;
# Where is the love?; The Black Eyed Peas; 4:13;
# A string representing the name of a new song.
# The operation of the function my_mp4_playlist:

# The function writes to the file the string representing the name of a new song (new_song)
#  instead of the name of the song that appears in the third line of the file 
# (if the file contains less than three lines, write empty lines to the file so that the name of the song is written in the third line).
# The function prints the contents of the file after the change has been made.
# An example of running the my_mp4_playlist function on the songs.txt file\

# >>> my_mp4_playlist(r"c:\my_files\songs.txt", "Python Love Story")
# Tudo Bom; Static and Ben El Tavori; 5:13;
# I Gotta Feeling; The Black Eyed Peas; 4:05;
# Python Love Story;Unknown;4:15;
# Paradise; Coldplay; 4:23;
# Where is the love?; The Black Eyed Peas; 4:13;

# The contents of the songs.txt file after running the my_mp4_playlist function
# Tudo Bom; Static and Ben El Tavori; 5:13;
# I Gotta Feeling; The Black Eyed Peas; 4:05;
# Python Love Story;Unknown;4:15;
# Paradise; Coldplay; 4:23;
# Where is the love?; The Black Eyed Peas; 4:13;

# My solution
def my_mp4_playlist(file_path, new_song):
    file= open(file_path, 'r')
    file_lines= file.readlines()
    file.close()
    if len(file_lines) >= 3:
        file= open(file_path, 'w')
        opp_list=[]
        final_list= []
        for line in file_lines:
            opp_list.append(line.split(';'))
        opp_list[2][0]= new_song
        for _list in opp_list:
            final_list.append(";".join(_list))
        file.write("".join(final_list))
        file.close()
        file= open(file_path, 'r')
        print(file.read())
        file.close()
        return None
    else:
        with open(file_path, 'r') as file:
            reader= file.readlines()
            new_list=[]
            for elem in reader:
                new_list.append(elem.strip())
        while len(new_list) <= 2:
            new_list.append(' ')
        else:
            new_list[2]= new_song
        with open(file_path, 'w') as writing_file:
            writing_file.write('\n'.join(new_list))
        with open(file_path, 'r') as read_file:
            print(read_file.read())
        return None