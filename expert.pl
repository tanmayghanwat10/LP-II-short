symptom(cold, sneezing).
symptom(cold, runny_nose).
symptom(cold, sore_throat).
symptom(cold, cough).
symptom(cold, mild_fever).
symptom(flu, high_fever).
symptom(flu, body_aches).
symptom(flu, headache).
symptom(flu, dry_cough).
symptom(flu, sore_throat).
symptom(strep_throat, sore_throat).
symptom(strep_throat, swollen_lymph_nodes).
symptom(strep_throat, fever).
symptom(strep_throat, rash).
symptom(allergies, sneezing).
symptom(allergies, itchy_eyes).
symptom(allergies, runny_nose).
symptom(allergies, watery_eyes).
% Predicate to diagnose an illness based on symptoms
diagnose(Illness, Symptoms) :-
 findall(I, (symptom(I, S), member(S, Symptoms)), PossibleIllnesses),
 list_to_set(PossibleIllnesses, UniqueIllnesses),
 member(Illness, UniqueIllnesses).
% Sample Query to Find a Possible Illness
sample_query :-
 Symptoms = [sneezing, runny_nose, sore_throat],
 diagnose(Illness, Symptoms),
 write('Based on the given symptoms, the likely illness is: '),
 writeln(Illness).
% Custom Diagnosis Query
test_diagnosis(Symptoms) :-
 diagnose(Illness, Symptoms),
 write('Based on the given symptoms, the likely illness is: '),
 writeln(Illness).

% how to run the code ?? 

% open cmd & type - swipl 
% next, type - [expert].

% Output:
% test_diagnosis([high_fever, body_aches, dry_cough]).
% Based on the given symptoms, the likely illness is: flu
% 1true
% sample_query
% Based on the given symptoms, the likely illness is: cold
% 1true
% Based on the given symptoms, the likely illness is: flu
% Based on the given symptoms, the likely illness is: strep_throat
% Based on the given symptoms, the likely illness is: allergies
% 2true
% 3true
% 4true
% test_diagnosis([fever, rash, sore_throat]).
% Based on the given symptoms, the likely illness is: cold
% 1true


