# Write a function called my_mp3_playlist defined as follows:
# def my_mp3_playlist(file_path):

# The function accepts as a parameter a path to the file (string).
# The file represents a playlist of songs and has a fixed format consisting of the name of the song, the name of the performer 
# (singer/band) and the length of the song, separated by a semicolon (;) without spaces.

# An example of an input file called songs.txt:

# Tudo Bom; Static and Ben El Tavori; 5:13;
# I Gotta Feeling; The Black Eyed Peas; 4:05;
# Instrumental; Unknown; 4:15;
# Paradise; Coldplay; 4:23;
# Where is the love?; The Black Eyed Peas; 4:13;
# The function returns a tuple in which:

# The first member is a string representing the name of the longest song in the file 
# (it means the longest song, assume all lengths are different).
# The second member is a number representing the number of songs the file contains.
# The third member is a string representing the name of the operation that appears in the file the largest number of times 
# (assume there is only one).
# An example of running the my_mp3_playlist function on the songs.txt file
# >>> print(my_mp3_playlist(r"c:\my_files\songs.txt"))
# ("Tudo Bom", 5, "The black Eyed Peas")

# My solution
def my_mp3_playlist(file_path):
    with open(file_path, 'r') as file:
        main_list= []
        main_dict_artists= {}
        main_dict_songs= {}
        content_of_file= file.read().split('\n')
        for elem in content_of_file:
            test_list= elem.split(';')
            for item in test_list:
                if item == '':
                    test_list.remove(item)
                else:
                    continue
            main_list.append(test_list)
        for list in main_list:
            if list[1] not in main_dict_artists.keys():
                main_dict_artists[list[1]]= [list[0]]
                continue
            else:
                main_dict_artists[list[1]].append(list[0])
        for list in main_list:
                main_dict_songs[list[0]]= float(list[2].replace(':','.'))
        return (max(main_dict_songs,key=main_dict_songs.get),len(main_list),max(main_dict_artists,key=lambda x: len(set(main_dict_artists[x]))))