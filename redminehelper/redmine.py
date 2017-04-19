#!/usr/bin/env python3
# -.- coding: utf-8 -.-

import json
import http.client
import urllib.parse

class RedmineError(RuntimeError):
    def __init__(self, message, details=None):
        self.message = message
        self.details = details

class Redmine():
    def __init__(self, key, domain="127.0.0.1"):
        self.key = key
        self.domain = domain

    def get_projects_page(self, offset=0):
        conn = http.client.HTTPSConnection(self.domain)
        conn.request("GET", "/projects.json?limit=100&offset={}&key={}".format(offset, self.key))

        req = conn.getresponse()
        data = req.read().decode("utf-8")

        if req.status != 200:
            raise RedmineError("can't receive response: {} {}".format(req.status, req.reason))

        page = None
        try:
            page = json.loads(data)
        except ValueError as e:
            raise RedmineError("can't parse JSON in response", str(e))
        finally:
            conn.close()

        return page

    def get_projects(self):
        projects = []
        is_done = False
        offset = 0
        while not is_done:
            page = self.get_projects_page(offset)
            projects += page["projects"]
            if page["total_count"] <= offset + 100:
                is_done = True
            offset += 100

        return projects

