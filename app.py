from flask import Flask, render_template, request, redirect 
import random


app = Flask(__name__)

Lista_falas = ["Eu luto até que o sangue tire a lança do meu alcance, até que eu só consiga rastejar. E mesmo assim, você não vai me derrotar, mesmo assim, eu vou cuspir na sua cara!", "Os céus não me temem porque sou um deus, eles me temem porque sou um homem!",  "Seguir em frente não é o mesmo que fugir dos seus erros.", "Avante! A lança aponta apenas para uma direção.", ]
lista_cores = ["red", "blue", "purple", "violet", "orange"]

lista_imagens = ["pantheon.png", "pantheon-noxus.jpg", "pantheon-galaxia.jpg", "pantheon-destruido.jpg", "pantheon-reidosmares.jpg"]

Cadastro_cores = []

@app.route("/sobre")
def pag_sobre():
    cor_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_fundo_html = cor_fundo)
    
# TODA AS ROTAS

@app.route("/", methods=["GET"])
def pag_inicial():
    imagens = random.choice(lista_imagens)
    cor_fundo = random.choice(lista_cores)
    falas_pantheon = random.choice(Lista_falas)
    return render_template("inicial.html", cor_fundo_html = cor_fundo, falas_pantheon_html = falas_pantheon, lista_imagens_html = imagens)


@app.route("/cadastro", methods=["GET"])
def pag_cadastro():
    return render_template("cadastro.html", lista_frases_html = Lista_falas)

@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarfrase():
    frase_vinda_html = request.form.get("frase")
    Lista_falas.append(frase_vinda_html)
    return redirect ("/cadastro")

@app.route("/cadastro-cores", methods=["GET"])
def pag_cores():
    return render_template("lista-cores.html", lista_cores_cadastradas_html = Cadastro_cores)

@app.route("/post/cadastrarcor", methods=["POST"])
def post_cadastrarcor():
    cor_vinda_html = request.form.get("cores")
    Cadastro_cores.append(cor_vinda_html)
    return redirect("/cadastro-cores")

app.run(debug= True)