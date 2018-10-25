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

