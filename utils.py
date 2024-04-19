# v2 with some simple logic
# !!!It looks like it's the best!!!
# speed: 0.0001 on 10 repeats
def split_to_sentences_simple(text:str) -> list:
    '''
    Split text into sentences.
    input: text with multiple rows.
    output: list of sentences.
    '''
    sentences = []
    n = len(text)
    i_start = 0
    i_end = n
    sentence_end = ".!?"
    not_end = ":-"
    for i in range(n):
        if text[i] in sentence_end:
            # if text[i-4:i+1].startswith(" "):
            if text[i-3:i+1].startswith(" "):    # i-4 controls the length of the shortest word. assume it is 3 symbols at least to handle words like some "etc.", "ape." and others
                continue
            elif text[i-3:i+1].startswith(" ") and not any([
                text[i-3:i+1].lower() == " ai."   # I forgot what that magic do... 
            ]):
                # print('\n')
                # print(f"<{text[i-3:i+1]}>")
                # print('\n')
                continue
            elif text[i-2:i+1].startswith(" "):
                continue
            # If text starts from "Mr. Smith" don't do anything
            elif text[i:i+1] and len(text[:i])<4:
                continue
            elif text[i+1:i+2].isalpha():
                continue
            elif text[i+2:i+3] == "—":
                continue
            else:
                i_end = i + 1
                sentences.append(text[i_start:i_end].strip())
                i_start = i_end
    # If sentence finishes on anything except sentence_end, then add last one to the list
    if text[n - 1] not in sentence_end:
        sentences.append(text[i_start:].strip())
    return sentences