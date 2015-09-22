import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(image={}, name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        
        imageFile = open(form.image.filename, 'wb')
        imageFile.write(form.image.value)
        imageFile.close()
       
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
