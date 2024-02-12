def build_prompt(sentence, index_propmt):
    """
    Given a sentence and the index of the prompt, it returns the prompt to be used for NER.
    args:
    sentence: str, sentence to be annotated
    index_propmt: int, index of the prompt to be used
    return:
    prompt: str, prompt to be used for NER
    """
    prompt_1 = '''I need to perform a named entity recognition task on a  text related with inclusion criteria in clinical trials.
    The entities you need to recognize are: Condition, Value, Drug, Procedure, Measurement, Temporal, Observation, Person, Mood, Device and Pregnancy_considerations.
    Particularly you have to produce the ouput in the BIO format. I will show you an example of the expected output.
    Input text: Patients with symptomatic CNS metastases or leptomeningeal involvement
    Output:
    Patients O
    with O
    symptomatic O
    CNS B-Condition
    metastases I-Condition
    or O
    leptomeningeal B-Condition
    involvement I-Condition

    You can see that tokens without any entity are labeled as O, and the tokens that are part of an entity are labeled as B-<entity> or I-<entity> depending on if they are the beginning or the inside of the entity.
    Please, just answer the question for this specific example and stop writting after that.
    Input text: '''
    promt_2 = '''I am working on a named entity recognition problem, in the context of clinical
    trials eligibility criteria. I will show you the list of entities:
    - Condition
    - Value
    - Drug
    - Procedure
    - Measurement
    - Temporal
    - Observation
    - Person
    - Mood
    - Device

    Your task consists in annotate the named entities in a given sentence in the format I will explain you.
    I will explain you with some examples:

    Example 1:
    Input: Patients who have received prior chemotherapy for unresectable disease.
    Output: Patients who have received prior <Procedure>chemotherapy</Procedure> for <Condition>unresectable disease</Condition>.

    Example 2:
    Input: Patients with any other severe concurrent disease, which in the judgment of the investigator, would make the patient inappropriate for entry into this study.
    Ouput: Patients with any other severe <Condition>concurrent disease</Condition>, which in the judgment of the investigator, would make the patient <Mood>inappropriate for <Observation>entry into this study</Observation>.

    As you can see, in each example, the extracted entities are enclosed using the sintax: <ENT>text of the entity</ENT>.

    Please now annotate as explained before the following sentence:

    Input: '''

    if index_propmt == 1:
        prompt = prompt_1 + sentence
    else:
        prompt = promt_2 + sentence
    return prompt

