# -*- coding: utf-8 -*-
"""
@author: Erin Canada
"""
#Movies_tables.txt to populate movies table and has_genre table
path ="C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/movies.txt"
f = open(path, 'r', errors='ignore')
titles = []
ids = []
genres = []
years = []

line = f.readline()
run = True
while(run):
    line = line.replace(': ', '; ')
    line = line.replace('\n', '')
    l = line.split(':')
            
    id = l[0]
    genre = l[2]
    
    string = l[1]
    string.replace(';', ':')
    year = string[-6:]
    year = year.replace('(', '')
    year = year.replace(')', '')
    
    title = string[:-7]
    
    ids.append(id)
    titles.append(title)
    years.append(year + "\n")
    genres.append(genre)
    
   
    line = f.readline()
    if line == '':
        run = False
    


movie_table = []
for i in range(len(ids)):
    movie_table.append(ids[i])
    movie_table.append('|')
    movie_table.append(titles[i])
    movie_table.append('|')
    movie_table.append(years[i])
    

    
movies = open("C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/movie_tables.txt","w+")
for i in range(len(movie_table)):
    movies.write(movie_table[i])
movies.close()

##Has_genre.txt

has_genre = []

for i in range(len(ids)):
    string = genres[i]
    g = string.split("|")
    for j in range(len(g)):
        has_genre.append(ids[i])
        has_genre.append('|')
        has_genre.append(g[j]+ "\n")
        


has_genres = open("C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/has_genres.txt","w+")
for i in range(len(has_genre)):
    has_genres.write(has_genre[i])
has_genres.close()


#tags_table.txt to populate tags table and users table

f = open("C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/tags.txt", "r")
lines = f.readlines()
tags = []
for line in lines:
	user = line.split(':')[0]
	movie = line.split(':')[1]
	time = line.split(':')[-1]
	n = len(line.split(':'))
	tag = line.split(':')[2:n-1]
	tag = ''.join(tag)
	# need to remove ':' symbols
	# from tags so the demiliter is not confused
	tag = tag.replace(':','')
	tags.append(user+':'+movie+':'+tag+':'+time)


outfile = ("C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/tags_table.txt")
f = open(outfile, 'w+')
for tag in tags:
	f.write(tag)

f.close()
    
#using ratings.txt to populate users table
#rate = open("C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/ratings.txt", "r")
#user = []
#line = rate.readline()

#run = True

#while(run):
 #  line = line.replace('\n', '')
  # if not line.split(":")[0] in user:
   #    user.append(line.split(":")[0])
 
   #line = rate.readline()
    
   #if line == '':
    #   run = False


#for i in range(len(userid)):
 #   if not userid[i] in user:
  #      user.append(userid[i])
       
#users = open("C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/users.txt", "w+")
#for i in range(len(user)):
 #   users.write(user[i])
#users.close()
    

    



    



