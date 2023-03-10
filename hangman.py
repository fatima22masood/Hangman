categories= ["name", "country", "movies", "sports"]
hangman= ["H", "A", "N", "G", "M", "A", "N"]
print(categories)
choice= input("chose category")
if (choice== categories[0]):
    name= "Alexander Graham Bell"
    
    for i in range(7):
        user_name= input("founder of Telephone")
        if (user_name==name):
            print("congratulations your answer is correct, You have saved the man")
            break
        else:
            print(f"{hangman[i]} is marked, try again, you have {6-i}more tries ")
    print("Game Over! Man is hanged")       
elif (choice== categories[1]):
    country= "Paalestine"
    for i in range(7):
        user_country= input("Removed from google maps")
        if (user_country==country):
            print("congratulations your answer is correct, You have saved the man")
            break
        else:
            print(f"{hangman[i]} is marked, try again, you have {6-i}more tries ")
    print("Game Over! Man is hanged")
elif (choice== categories[2]):
    movies= "Titanic"
    for i in range(7):
        user_movie= input("English Movie related to ship")
        if (user_movie==movies):
            print("congratulations your answer is correct, You have saved the man")
            break
        else:
            print(f"{hangman[i]} is marked, try again, you have {6-i}more tries ")
    print("Game Over! Man is hanged")  
elif (choice== categories[3]):
    sport= "basketball"
    for i in range(7):
        user_sport= input("played with ball")
        if (user_sport==sport):
            print("congratulations your answer is correct, You have saved the man")
            break
        else:
            print(f"{hangman[i]} is marked, try again, you have {6-i}more tries ")
    print("Game Over! Man is hanged") 
else:
    print("you entered wrong choice")    