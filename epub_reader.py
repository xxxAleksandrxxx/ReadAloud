import zipfile
import os
from bs4 import BeautifulSoup
import re


class BookEpub:
    def __init__(self, filename):
        # Check the filename for existence.
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        self.file_path = filename
        self.folder_path = os.path.dirname(self.file_path)
        self.file_name_ext = os.path.basename(self.file_path)
        self.file_name_no_ext = os.path.splitext(self.file_name_ext)[0]
        self.extracted_path = None
        self.book_parts = []
    

    # Done
    def epub_print_content(self):
        """
        Prints the list of files it the EPUB archive.
        """
        with zipfile.ZipFile(self.file_path, 'r') as zf:
            for f in zf.namelist():
                print(f)


    # Done
    def epub_get_content(self):
        """
        Returns unsorted list of files in the EPUB archive.
        """
        content = list()
        with zipfile.ZipFile(self.file_path, 'r') as zf:
            for f in zf.namelist():
                content.append(f)
        return content


    # Done
    def epub_get_xhtml_names(self):
        """
        Returns sorted list of .xhtml files it the EPUB archive.
        """
        content = []
        with zipfile.ZipFile(self.file_path, 'r') as zf:
            for f in zf.namelist():
                if "xhtml" in f:
                    content.append(f)
        return sorted(content)


    # Done
    def epub_unpack(self, b_path=None, b_pwd=None):
        """
        Unpacks the EPUB file into folder named as EPUB file located in parent folder "books" by default.
        b_path - folder to where extract book. by default its the same place where book is located and it assumed to be "books" folder.
        b_pwd - password if any and if applicapabel at all.
        """
        if b_path != None:
            b_path = os.path.dirname(self.file_path)
        b_name = os.path.splitext(os.path.basename(self.file_path))[0]
        self.extracted_path = b_path + '/' + b_name
        with zipfile.ZipFile(self.file_path, 'r') as zf:
            for f in zf.namelist():
                zf.extract(f, self.extracted_path, b_pwd)

    
    def epub_get_part_names(self):
        """
        Gets list of book part names.
        """
        with zipfile.ZipFile(self.file_path, 'r') as zf:
            for f in zf.namelist():
                if ".xhtml" in str(f):
                    self.book_parts.append(str(f))
        self.book_parts = sorted(self.book_parts)
        return self.book_parts


    def epub_get_text_from_parts(self, part_name=None):
        """
        Opens part of extracted epub, extract text, clean it from html code and return cleaned text
        """
        if part_name == None:
            part_name = input("Enter full path to the file you need:\n")
        # Check the filename for existence.
        if not os.path.exists(part_name):
            raise FileNotFoundError(f"File {part_name} not found")
        with open(part_name, "r", encoding="utf-8") as f:
            text = BeautifulSoup(f.read(), "html.parser").get_text(separator=" ", strip=True)
        text = re.sub(r"\[\d+\]", "", text)  # clean text from links like [123]
        text = re.sub(r"\{\d+\}", "", text)  # clean text from links like {123}
        text = text.replace(" . ", ". ")    # with such simple replacement it works faster then with re.sub
        text = text.replace(" , ", ", ")    # with such simple replacement it works faster then with re.sub
        return(text)
    

    def epub_print_text_from_parts(self, part_name=None):
        """
        Opens part of extracted epud, extract text, clean it from html code and print cleaned text
        """
        if part_name == None:
            part_name = input("Enter full path to the file you need:\n")
        # Check the filename for existence.
        if not os.path.exists(part_name):
            raise FileNotFoundError(f"File {part_name} not found")
        with open(part_name, 'r', encoding='utf-8') as f:
            # for text that will be splitted later for one sentence per row:
            text = BeautifulSoup(f.read(), "html.parser").get_text(separator=" ", strip=True)

            # for text expected to be printed out later as paragraphs
            # text = BeautifulSoup(f.read(), "html.parser").get_text(separator="\n", strip=True)
        # text = text.replace(" . ", ". ")    # for nice printout of text
        # text = text.replace(" \n. ", ". ")  # for nice printout of text
        # text = text.replace("\n. ", ". ")   # for nice printout of text
        # text = text.replace(" \n, ", ", ")  # for nice printout of text
        # text = text.replace("\n, ", ",")    # for nice printout of text
            
        text = re.sub(r"\[\d+\]", "", text)  # clean text from links like [123]
        print(text)
    

    def epub_get_book_txt(self, book_extracted_path=None, book_parts_list=None):
        if self.extracted_path != None and book_extracted_path == None:
            book_extracted_path == self.extracted_path
        elif self.extracted_path == None and book_extracted_path == None:
            book_extracted_path = input("Enter folder path for the place where the book is located:\n")
        # Check the folder path for existence.
        if not os.path.exists(book_extracted_path):
            raise FileNotFoundError(f"Folder {book_extracted_path} not found")
        book_text = list()
        if book_parts_list == None:
            book_parts_list = self.epub_get_xhtml_names()
        
        for name in book_parts_list:
            # Check the part name for existence.
            book_part_path = book_extracted_path + "/" + name
            if not os.path.exists(book_part_path):
                raise FileNotFoundError(f"File {book_part_path} not found")
            book_text.append(self.epub_get_text_from_parts(book_part_path))
        return " ".join(book_text)


# if __name__ == "__main__":
#     file_book = 'books/test.epub'
#     b = BookEpub(file_book)
#     # b.epub_print_content()
#     # b.epub_unpack(file_book)
#     # b.epub_get_part_names()
#     # b.epub_get_text_from_parts("books/test/index_split_001.xhtml")
#     # b.epub_print_text_from_parts("books/test/index_split_002.xhtml")
#     book = b.epub_get_book_txt("books/test")
#     # print(book[:5000])