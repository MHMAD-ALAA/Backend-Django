from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    task= {"<style>"
             "h2{color:red;}"
             "ol{color:blue;}"
             "</style>"
           " <p>Hello my friend, I am sorry for the late reply, and I am also sorry for not showing</p>"
         "<p> you any pictures to show you more information about Django, because I only learned how views work,</p>"
          "<p>  but I didnt delve into templates or models to show you pictures and html pages</p>"
          "<h4>Now I'm going to take you on a tour of Django framwork</h4>"
          " <h2>Django structure</h2>"
          "<ol>"
               "<li>views responsible for logic of all process and conect each part in cycle of web</li> "
               "<li> model is the datalink layer and responsible of interact with database</li>"
               "<li> template is the presentation layer and responsible for show html pages </li> "
            "</ol>"
           "<h2> Django Advantages</h2>"
             "<ol>"
                 "<li>Django is very powerful framwork to interact with big data</li>"
                 "<li> Django is very scable so it can work easily with maintance website</li>"
                 "<li> Django is very secure </li>"
                 "<li> Django chances are very balanced</li>"
              "</ol>"
            "<h2> Django business need</h2>"
               "<ol>"
                   "<p>Now, after enumerating the characteristics and benefits of Django, we find that Django is very important and useful for any site</p>"
                    "<p> regardless of the size of its data, the frequency of dealing with it, or the desire to protect it.</p>"
                     "<p> Django is very balanced and always an ideal choice</p>"}
          
    return HttpResponse(task)
    
