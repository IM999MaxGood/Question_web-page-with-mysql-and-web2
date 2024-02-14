import web
from web import form
import model

urls = ("/", "Index", "/del/(\d+)", "Delete", "/add", "Add", "/edit/(\d+)", "Edit")
#urls = ("/", "Index", "/del", "Delete")

render = web.template.render("templates", base="base")

class Index:
    def GET(self):
        items = model.getItems()
        return render.index(items)

class Delete:
    def POST(self, id):
        model.delItem(id)
        items = model.getItems()
        return render.index(items)
     
    def GET(self, id):   
        model.delItem(id)
        items = model.getItems()
        return render.index(items)

class Add:
    form = form.Form(
        form.Textbox("title", form.notnull, description="title"),
        form.Button("add")
    )

    def GET(self):
        f = self.form()
        return render.add(f)
    
    def POST(self):
        f = self.form()
 
        if f.validates():
            model.addItem(f.d.title)
        else:
            return render.add(f)
 
        items = model.getItems()
        return render.index(items)

class Edit:
    form = form.Form(
        form.Textbox("title", form.notnull, description="title"),
        form.Button("Edit")
    )

    def GET(self, id):
        item = model.getItem(id)
        f = self.form()
        #f.inputs[0].value = item.title
        f.fill(item)
        return render.edit(f, item)
    
    def POST(self, id):
        f = self.form()

        if f.validates():
            model.updateItem(id, f.d.title)
        else:
            item = model.getItem(id)
            #f.inputs[0].value = item.title
            f.fill(item)
            return render.edit(f, item)

        items = model.getItems()
        return render.index(items)


app = web.application(urls,globals())

if __name__ == "__main__":
    app.run()