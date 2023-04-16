# ask user number of choice
# generate multiplication table from 1 to 10
# award points when answerd correctly
# show user their score after 10
print("Math Game!")
print()
score=0
multiples=int(input("Name your multiples: "))
print()
for i in range (1,11):
  answer=int(input(f"{i} x {multiples} = "))
  working=i*multiples
  if working==answer and score==1:
    score+=1
    print("Awesome!")
    print()
  elif working==answer and score==5:
    score+=1
    print("You're on a winning streak!")
    print()
  elif working==answer:
    score+=1
    print("Great work!")
    print()
  elif working!=multiples:
    print(f"Nope. The answer was {working}")
    print()
print(f"You scored {score} out of 10")