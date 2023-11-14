import os
import shutil

image = (".jpeg", ".JPEG", ".JPG", ".png", ".PNG", ".jpg", ".jfif", ".svg", ".gif", "pjpeg",
         ".webp", ".pjp", ".apng", ".avif", ".ico")

audio = (".mp3", ".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape",
         ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mpga", ".oga",
         ".ogg", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")

videos = (".mp4", ".webm", ".MTS", ".M2TS", ".TS", ".mov", ".m4p", ".m4v", ".mxf")

text = (".txt", ".md")
database_files = (".sql", ".mdb")
executables = (".exe", ".msi", ".apk")
documents = (".docx", ".xlsx", ".csv", ".pptx", ".xls", ".xlsm")
web_docs = (".php", ".html", ".htm", ".css")
pdf = (".pdf")
zip_files = (".zip", ".7z")
iso = (".iso", ".md4")


def is_image(file):
    return os.path.splitext(file)[1] in image


def is_audio(file):
    return os.path.splitext(file)[1] in audio


def is_video(file):
    return os.path.splitext(file)[1] in videos


def is_text(file):
    return os.path.splitext(file)[1] in text


def is_database(file):
    return os.path.splitext(file)[1] in database_files


def is_html(file):
    return os.path.splitext(file)[1] in web_docs


def is_exec(file):
    return os.path.splitext(file)[1] in executables


def is_zip(file):
    return os.path.splitext(file)[1] in zip_files


def is_document(file):
    return os.path.splitext(file)[1] in documents


def is_pdf(file):
    return os.path.splitext(file)[1] in pdf


def is_iso(file):
    return os.path.splitext(file)[1] in iso


os.chdir('C:\\Users\\MUTIA\\Downloads')

for file in os.listdir():
    if is_audio(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Audio')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Audio')
    elif is_pdf(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\PDF')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\PDF')
    elif is_zip(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\ZIP_FILES')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\ZIP_FILES')
    elif is_document(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Documents')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Documents')
    elif is_exec(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Executables')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Executables')
    elif is_html(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Web_files')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Web_files')
    elif is_database(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Database_files')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Database_files')
    elif is_text(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Text_files')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Text_files')
    elif is_video(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Videos')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Videos')
    elif is_iso(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\ISO_FILES')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\ISO_FILES')
    elif is_image(file):
        print("Moving: " + file + " " + "to: " + 'D:\\BlueSky IT Solutions\\files_from_downloads\\Images')
        shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Images')
    else:
        # shutil.move(file, 'D:\\BlueSky IT Solutions\\files_from_downloads\\Unknown_files')
        print("File exists")

