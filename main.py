SUPPORTED_LANGUAGES = ["es"]


class LatexDocument:
    def __init__(self,*, name="", language = "es") -> None:
        self.name = name
        self.language = language
        self.filename = self.get_filename(name)
        self.content = ""
        self.start_content()
    
    def get_filename(self,name):
        name = name.lower()
        namesplit = name.split(" ")
        name = ""
        for n in namesplit:
            n = n.replace(":", "")
            name += n[0].upper() + n[1:]
        name += ".tex"
        return name
    
    def start_content(self):
        file = open(f"misc/start-{self.language}.tex", "r")
        lines = file.readlines()
        for line in lines:
            self.content += line
        self.content = self.content.replace("RECNAME001", self.name)
    
    def end_content(self):
        self.content +="\n\t\end{enumerate}\n\end{document}"

    def add_questions(self, enunciate, sub, image):
        self.content += "\t\t\item " + enunciate + "\n"

        self.content += image.data

        if len(sub) != 0:
            self.content += "\t\t\\begin{enumerate}\n"
            for subs in sub:
                self.content += "\t\t\t\item " + subs + "\n"
            self.content += "\t\t\\end{enumerate}\n"
    
    def save(self):
        self.end_content()
        savingfile = open("data/examples/"+self.filename, "w", encoding="utf-8")
        print(self.content, file=savingfile)
        savingfile.close()
    
class Image:
    def __init__(self,*, path = "") -> None:
        self.path = ""
        self.data = ""

class Question:
    def __init__(self,id=0) -> None:
        self.id = id

def main():

    # Example
    Latex = LatexDocument(name="Algebra y Trigonometría: Guía 1", language="es")
    print(Latex.filename)
    Latex.add_questions("Hola", ["Sí", "No"], Image(path=""))
    Latex.add_questions("Hola", ["Sí", "No"], Image(path=""))
    Latex.add_questions("Hola", ["Sí", "No"], Image(path=""))
    Latex.save()
if __name__ == "__main__":
    main()