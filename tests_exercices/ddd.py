mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."


if len(mdp) == 0:
    print (mdp_trop_court.upper())

elif  len(mdp) < 8:
    print (mdp_trop_court.capitalize())

elif mdp.isnumeric() is True:
    print ("Votre mot de passe ne contient que des nombres.")

else: 
    print("Inscription terminée")
