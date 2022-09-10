answer_yes=["Yes","yes","Y","y"]
answer_no=["No","no","N","n"]

print("""WELCOME! LET'S START THE ADVENTURE
You are going to home by your car when see a women in dirty clothes running towards you and asking a ride for home.
Will you give her ride for home? (Yes/No)
""")

ans1=input(">>")

if ans1 in answer_yes:
    print("\n after 5 minuts police, you are stopped at checkpoint and police asks you if you seen a  suspecious women. Will you say? (Yes/No)\n")
    ans2=input(">>")
    if ans2 in answer_yes:
        print("You are a honest person. She was a murderer & you won the game")
    elif ans2 in answer_no:
        print("You helped a murderer. Now, go to jail. GAME OVER!")
    else:
        print("\nYou typed a wrong input. GOODBYE!")

if ans1 in  answer_no:
    print("\nNow, she will trying kill you. Will you knock her down?(Yes/No)\n")
    ans3=input(">>")
    if ans3 in answer_yes:
        print("\nCongrats! She was a murderer & You helped the police to catch her with your bravery")
    elif ans3 in answer_no:
        print("\nSorry!, your are dead. She was a murderer & She killed you. GAME OVER")
    else:
        print("\nYou typed a wrong input. GOODBYE!")

else:
    print("\n you typed wrong input.GOODBYE!")