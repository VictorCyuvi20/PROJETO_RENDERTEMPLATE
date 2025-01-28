from flask import Flask, render_template
import random

app = Flask(__name__)

Lista_falas = ["Eu luto até que o sangue tire a lança do meu alcance, até que eu só consiga rastejar. E mesmo assim, você não vai me derrotar, mesmo assim, eu vou cuspir na sua cara!", "Os céus não me temem porque sou um deus, eles me temem porque sou um homem!",  "Seguir em frente não é o mesmo que fugir dos seus erros.", "Avante! A lança aponta apenas para uma direção.", ]
lista_cores = ["red", "blue", "purple", "violet", "orange"]

lista_imagens = ["pantheon.png", "pantheon-noxus.jpg", "pantheon_galaxia.jpg", "pantheon-destruido.jpg", "patheon-reidosmares.jpg"]

@app.route("/sobre")
def pag_sobre():
    cor_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_fundo_html = cor_fundo)
    
# TODA AS ROTAS

@app.route("/")
def pag_inicial():
    imagens = random.choice(lista_imagens)
    cor_fundo = random.choice(lista_cores)
    falas_pantheon = random.choice(Lista_falas)
    return render_template("inicial.html", cor_fundo_html = cor_fundo, falas_pantheon_html = falas_pantheon, lista_imagens_html = imagens)

app.run(debug= True)