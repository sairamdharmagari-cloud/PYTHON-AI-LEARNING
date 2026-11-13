# Prior probabilities
p_spam = 0.50
p_not_spam= 0.30

# Likelihood probabilities

p_offer_given_spam = 0.80
p_offer_given_not_spam =0.20

#Calculate total probability of offer

p_offer =(
    p_offer_given_spam*p_spam
    +p_offer_given_not_spam*p_not_spam
)

#Apply bayes ' Theorem
p_spam_given_offer =(
    p_offer_given_spam*p_spam
) / p_offer

print ("Probability of Offer:",p_offer)

print(
    "Probability of Sapm given Offer:",
    round(p_spam_given_offer * 100 ,2),"%"
)

#Code	Purpose
#_spam -	Stores prior spam probability
#p_offer_given_spam -	Stores likelihood
#p_offer-	Calculates total evidence probability
#p_spam_given_offer-	Calculates posterior probability
#round()-	Rounds the result

#This is useful when you want to understand
#  how probability-based classification works internally.