from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle


# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)



def index(request):
    

    return render(request, 'index.html')

def hola_mundo(request):
    

    return render(request, 'hola_mundo.html')

def contacto(request):
    

    return render(request, 'contacto.html')


def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )    
    articulo.save()

    return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )    
        articulo.save()

        return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:
        return HttpResponse("No se ha podido crear el artículo!!, intentalo mas tarde")



def create_article(request):
    
    
    return render(request, 'create-article.html')

def create_full_article(request):

    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')

            articulo = Article(
            title = title,
            content = content,
            public = public
            )    
            articulo.save()

            return redirect('articulos')

            #return HttpResponse(articulo.title + '' + articulo.content + '' + str(articulo.public))


    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form' : formulario
    })

def articulo(request):

    try:
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Artículo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "Este artículo no existe"

    return HttpResponse(response)


def articulos(request):

   

    articulos = Article.objects.filter(title__contains="art")

    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE public=True")

    articulos = Article.objects.filter(
        Q(title__contains="2") | Q(title__contains="9")
    )

    articulos = Article.objects.all()[:100]

    return render(request, 'articulos.html', {
        'articulos' : articulos

    })

def editar_articulo(request, id, title):

    articulo = Article.objects.get(pk=id)

    
    articulo.title = title

    articulo.save()

    return HttpResponse(f"Artículo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.delete()
    
    return redirect('articulos')



    




    
