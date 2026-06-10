# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:38:06 2026

@author: LENOVO
"""


class Movie:
    def __init__(self, name, genre, age_rating):
        self.name = name
        self.genre = genre
        self.age_rating = age_rating

    def __str__(self):
        return "{} ({}, {}+)".format(self.name, self.genre, self.age_rating)


class User:
    def __init__(self, name, age, preferred_genre):
        self.name = name
        self.age = age
        self.preferred_genre = preferred_genre


class RecommendationSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def recommend(self, user):
        matching_movies = []

        for movie in self.movies:
            if movie.age_rating <= user.age and movie.genre == user.preferred_genre:
                matching_movies.append(movie)

        return matching_movies


# System setup
system = RecommendationSystem()

system.add_movie(Movie("Hannibal", "Horror", 18))
system.add_movie(Movie("Inception", "SciFi", 13))
system.add_movie(Movie("Frankenweenie", "Animation", 7))
system.add_movie(Movie("Edward Scissorhands", "SciFi", 13))

print("Welcome to the Movie Recommendation System")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
choice = input("Enter your preferred movie genre: ")

user = User(name, age, choice)

while True:
    print("\n--- Menu ---")
    print("1. Get movie recommendations")
    print("2. Add new movie")
    print("3. Exit")

    choice_menu = input("Choose an option (1/2/3): ")

    if choice_menu == "1":
        recommended_movies = system.recommend(user)

        if recommended_movies:
            print("\nRecommended Movies:")
            for movie in recommended_movies:
                print(f"- {movie.name} ({movie.genre}, Age {movie.age_rating}+)")
        else:
            print("\nNo suitable movies found.")

    elif choice_menu == "2":
        movie_name = input("Movie name: ")
        movie_genre = input("Movie genre: ")
        movie_age = int(input("Age rating: "))

        new_movie = Movie(movie_name, movie_genre, movie_age)
        system.add_movie(new_movie)

        print("Movie successfully added.")

    elif choice_menu == "3":
        print("\nExiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        