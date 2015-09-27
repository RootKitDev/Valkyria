% les faits :
epouse(alice,luk). % alice est l'epouse de luc
pere(luk,jean). % luc est le pere de jean
            
% les regles :
mere(M,E):-pere(P,E),epouse(M,P). % M est la mere de E si P est le pere de E et si M est l'epouse de P
                    
                    






