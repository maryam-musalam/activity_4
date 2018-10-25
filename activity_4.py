from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler , HTTPServer

memory = {}
form = '''<!DOCTYPE html>
    <title>Udacian</title>
    <form method="POST" action="http://localhost:8000/">
    <textarea name="name" placeholder="Enter the name"></textarea>
    <br>
    <textarea name="city" placeholder="Enter city"></textarea>
    <br>
    <textarea name="enrollment" placeholder="Enter the enrollment (ex:enrollment / didn't enroll)"></textarea>
    <br>
    <textarea name="nanodegree" placeholder="Enter the nanodegree(ex: FSND in sat with Ms. elham ):"></textarea>
    <br>
    <textarea name="status" placeholder="Enter status(ex:ontrack - not in track):"></textarea>
    <br>
    <button type="submit">Post it!</button>
    </form>
    <pre>
    {}
    </pre>
    '''

class ShowInfo(BaseHTTPRequestHandler):
    def do_POST(self):
        #Submit the form
        length = int(self.headers.get('Content-length', 0))
        info = self.rfile.read(length).decode()
        param = parse_qs(info)
        
        
        
        if "name" in param and "city" in param and "enrollment" in param and "nanodegree" in param and "status" in param:
            
            name = param["name"][0]
            city= param["city"][0]
            enrollment = param["enrollment"][0]
            nanodegree= param["nanodegree"][0]
            status= param["status"][0]
            
            self.send_response(300)
            self.send_header('Location' , '/')
            self.end_headers()
            
            known = "'{}' is '{}' in '{}' studying '{}'. he/she is '{}' ".format(name ,enrollment,  city, nanodegree , status)
            self.wfile.write(form.format(known).encode())
        
        else:
            self.send_response(400)
            self.send_header('content-type' , 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("you can't leave empty feilds".encode())



