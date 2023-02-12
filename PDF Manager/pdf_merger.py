import os
import string as s
import PyPDF2 as pdf


class pdf_merge:

    path_ = ''
    file_list = []

    @classmethod
    def __init__(cls, p):
        cls.path_ = p
        for x in os.listdir(cls.path_):
            cls.file_list.append(x)

    @classmethod
    def content(cls):
        print(f"\n{'_'*55}\n\n{'C O N T E N T S'.center(55,' ')}\n")
        for x, y in enumerate(cls.file_list, start=1):
            print(f" {x}. {y}")
        print(f"\n{'-'*55}\n")

    @classmethod
    def info(cls):
        print(f"{'_'*55}\n\n{'F I L E  I N F O R M A T I O N'.center(55,' ')}\n")
        for x, y in enumerate(cls.file_list, start=1):
            print(f" {x}. {y}\n")
            f = pdf.PdfReader(f'{cls.path_}/{y}')  # Reader object
            data = str(f.metadata).lstrip('{')
            data = data.rstrip('}')
            data = data.split(',')
            for x in data:
                data_ = x.split(': ')
                print(f" {data_[0][2:-1].lstrip('/')} : {data_[1]}")
            print(f" Pages : {len(f.pages)}\n")
        print(f"{'-'*55}\n")

    @classmethod
    def merge(cls, name='merged_PDF'):
        merger = pdf.PdfMerger()

        for x in cls.file_list:
            merger.append(f'{cls.path_}/{x}')

        with open(f'{cls.path_}/{name}.pdf', 'wb') as f:
            merger.write(f)

        cls.file_list.append(f'{name}.pdf')  # updating the file list

        print(
            f"\n PDFs merged successfully!\n\n Path : {cls.path_}/{name}.pdf")

    @classmethod
    def rotate(cls):
        n = input('\n Enter file name : ')

        orig = pdf.PdfReader(f'{cls.path_}/{n}.pdf')
        edit = pdf.PdfWriter()

        deg = int(input(
            "\n Enter the angle of rotation : \n (must be in int() multiples of 90)\n\n >>> "))

        edit.add_page(orig.pages[0])
        edit.pages[0].rotate(deg)

        with open(f'{cls.path_}/{n}.pdf', 'wb') as f:
            edit.write(f)

        print('\n Editing complete!')


if __name__ == "__main__":  # Driver

    p = input(
        f"\n{'P D F  M E R G E R'.center(55, ' ')}\n{'_'*55}\n\n Enter the folder path : ")

    while True:
        try:
            ch = input(
                f"\n{'-'*55}\n{'M A I N  M E N U'.center(55,' ')}\n{'-'*55} \n\n [1] Display PDFs\n [2] Display PDF info\n [3] Merge PDFs\n [4] Edit PDFs \n [5] Exit\n\n Enter your choice : ")
            if ch not in s.digits:
                raise BaseException('\n Please select a valid option!')
            match int(ch):
                case 1:
                    pdf_merge.content()
                case 2:
                    pdf_merge.info()
                case 3:
                    name = input('\n Enter a name for the merged PDF : ')
                    pdf_merge.merge(name)
                case 4:
                    edit = int(input(
                        f"\n{' M E N U '.center(55,'-')}\n\n [1] Rotate PDF\n [2] Exit\n\n >>> "))
                    match edit:
                        case 1:
                            pdf_merge.rotate()
                        case 2:
                            pass
                case 5:
                    print(f'''\n{"Goodbye! 😁".center(55)}\n''')
                    break
                case _:
                    print('\n Please select a valid option!')
        except BaseException as e:
            print(e.args[0])
