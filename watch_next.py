
# --- Libraries ---

import spacy

nlp = spacy.load('en_core_web_md')

# --- Functions ---

# tokenise the function argument & declare empty dictionary for movies
def movie_similarity(description):
    desc_doc = nlp(description)
    similarity_dict = {}

    # iterate through movies.txt file contents, spliting titles from respective descriptions, tokenising the latter & calculating similarity
    with open("movies.txt", "r", encoding = "utf-8") as movies:
        contents = movies.readlines()

    for entry in contents:
        title, text = entry.split(" :")
        text_doc = nlp(text)
        similarity_dict[title] = text_doc.similarity(desc_doc)
    
    # isolate the maximum dict value & identify its corresponding key 
    max_value = max(similarity_dict.values())

    for key, value in similarity_dict.items():
        if value == max_value:
            max_key = key

    print(f"The film most similar to the inputed description is {max_key}. It has a {round(max_value,2)}% similarity")

# --- Main body ---

planet_hulk = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator"""

movie_similarity(planet_hulk)
