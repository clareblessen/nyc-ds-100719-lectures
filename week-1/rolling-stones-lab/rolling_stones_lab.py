# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
with open('/Users/cblessen/Documents/FlatironSchool/lecture_notes/nyc-ds-100719-lectures/week-1/rolling-stones-lab/data.csv') as f:
    reader = csv.DictReader(f)
    a = list(reader)
    album_data = a
        
#class Albums():
    
    #for album in album_data:
        #album = Albums(album_data[0]['number'], album_data[0]['year'], album_data[0]['album'], album_data[0]['artist'], album_data[0]['genre'],album_data[0]['subgenre'])
        #album = +-1

    #def __init__(self, number, year, album, artist, genre, subgenre):
        #self.number = number
        #self.year = year
        #self.album = album
        #self.artist = artist
        #self.genre = genre
        #self.subgere = genre
    
    for album in album_data:
        album['year'] = int(album['year'])
        
    for album in album_data:
        album['number'] = int(album['number'])
    
    def find_by_name(string):
        for album in album_data:
            if string == album['album']:
                return album
            
    def find_by_rank(num):
        for album in album_data:
            if num == album['number']:
                return album
            
    def find_by_year(num):
        albums_in_year = []
        for album in album_data:
            if num == album['year']:
                albums_in_year.append(album)
        return albums_in_year
    
    def find_by_years(start,end):
        albums_in_years = []
        for album in album_data:
            if start <= album['year'] and end >= album['year']:
                    albums_in_years.append(album)
        return albums_in_years
    
    def find_by_ranks(start,end):
        albums_by_ranks = []
        for album in album_data:
            if start <= album['number'] and end >= album['number']:
                    albums_by_ranks.append(album)
        return albums_by_ranks
    
    def all_titles():
        titles = []
        for album in album_data:
            titles.append(album['album'])
        return titles
    
    def all_artists():
        artists = []
        for album in album_data:
            artists.append(album['artist'])
        return artists
    
    #def artists_most_albums():
        #artist_count = {}
        #for album in album_data:
            #if album['artist'] not in artist_count:
                #artist_count['artist'] = 1
            #else artist_count['artist'] = album['artist']
                #artist_count['count'] = += 1
                
    def most_albums():
        answer= []
        list_artists = all_artists()
        counter_dict = Counter(list_artists)
        list_values= list(counter_dict.values())
        list_keys = list(counter_dict.keys())
        for index in range(len(list_keys)):
            if int(list_values[index])== max(list_values):
                answer.append(list_keys[index])
                return answer
                
    def most_popular_word():
        words = []
        for album in album_data:
            all_words = album['album'].split(" ")
            for word in all_words:
                words.append(word)
        answer= []
        list_words = words
        counter_dict = Counter(list_words)
        list_values= list(counter_dict.values())
        list_keys = list(counter_dict.keys())
        for index in range(len(list_keys)):
            if int(list_values[index])== max(list_values):
                answer.append(list_keys[index])
                return answer
            
        return words
    
    
    print(most_popular_word())
                

    
   
