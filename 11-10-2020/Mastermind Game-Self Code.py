import random
colors = ['R','B', 'O', 'G', 'Y', 'P']

# print(generated)
# print(user_guess)

#Checks if they guess letters are in the computer generated list
def guess_in_truth(truth, guess):
  # for i in guess:
    # if
  guess_similarity = ["White" if i in truth else i for i in guess]
  return guess_similarity


# print(guess_in_truth(generated, user_input))

#check for positional consistency

def position_compare(truth, guess):
  guess_position = ["Black" if guess[i] == truth[i] else guess[i] for i in range(4)]
  return guess_position

# print(position_compare(generated, user_input))


total_guess = 0
generated = random.sample(colors, 4)
while total_guess != 10:
# print(generated)
  user_input = input("Make a guess ")
  result = position_compare(generated,user_input)
  if result == ['Black', 'Black','Black','Black']:
    total_guess +=10
    print('Congrats, you are correct!')
    break
  elif result != ['Black', 'Black','Black','Black']:
    final = guess_in_truth(generated, result)
    total_guess +=1
    tries_left = "{} more tries".format(10-total_guess)
    print(final)
    print(tries_left)



