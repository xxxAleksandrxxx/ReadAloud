# It works!
# extract text from epub and save as .txt with each sentence on separate row.
# Probably better to use it as Jupyter Notebook as each book
# would probably have different styles so different ways 
# should be applied to prepare and clean them



from epub_reader import *
import utils

if __name__ == "__main__":
    file_book = 'books/test.epub'
    b = BookEpub(file_book)
    book_parts = b.epub_get_part_names()
    for i in range(len(book_parts)):
        if "index" not in book_parts[i]:
            del book_parts[i]
    book_parts = book_parts[2:]
    # check the result
    # print(book_parts)

    book_text = b.epub_get_book_txt("books/test", book_parts)
    # check the result
    # print(book_text[-1000:])

    book_text = book_text.replace("’ ‘", " ")
    book_text = book_text.replace("”’ ‘“", " ")
    book_text = book_text.replace("‘“", "")
    book_text = book_text.replace("”’", "")
    book_text = book_text.replace("”“", "")
    book_text = book_text.replace("” ", " ")
    book_text = book_text.replace("’ ", " ")





    book_text = utils.split_to_sentences_simple(book_text)

    # check that we have nice splitted sentences
    # for sentence in book_text[:50]:
    #     print(sentence)

    book_txt_name = b.file_name_no_ext
    book_folder_path = b.folder_path
    book_txt_path = book_folder_path + "/" + book_txt_name + ".txt"
    with open(book_txt_path, "w") as f:
        for sentence in book_text:
            # s = sentence.replace("")
            if sentence.startswith("‘"):
                f.write(sentence[1:] + '\n')
            else:
                f.write(sentence + '\n')
    print("Done")
    # print(book_txt_name)
