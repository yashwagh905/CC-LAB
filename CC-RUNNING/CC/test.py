import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("<b>Hello, World!</b><br>CC Assignment Accomplished<br><b>Yash Wagh</b><br>12111124<br>AIDS-C-B3-74")


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
