% Diet suggestions
diet(diabetes, 'Low sugar foods').
diet(obesity, 'Low calorie foods').
diet(anemia, 'Iron rich foods').
diet(hypertension, 'Low salt foods').
diet(fever, 'Fluids and nutritious foods').

% Rule
suggest_diet(Disease) :-
    diet(Disease, Food),
    write('Suggested diet: '),
    write(Food), nl.