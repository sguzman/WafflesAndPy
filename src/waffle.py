import l33t
from splinter import Browser
import time
import sys


problems = l33t.leet()

with Browser() as b:
    b.visit("https://waffle.io/")
    b.find_by_text("Login").click()
    b.find_by_text(" Public Repos Only").click()
    b.fill("login", sys.argv[1])
    b.fill("password", sys.argv[2])
    b.find_by_value("Sign in").click()
    project = b.find_by_text("sguzman/LeetCodeScala")
    oath = b.find_by_id("js-oauth-authorize-btn")
    if len(project) is 0 and len(oath) is not 0:
        oath.click()

    b.find_by_text("sguzman/LeetCodeScala").click()

    for p in problems:
        issue = None
        while True:
            try:
                issue = b.find_by_text("Add Issue")
                if len(issue) is 0:
                    continue
                else:
                    issue.click()
                    b.fill("title", p)
                    b.find_by_text("Add").click()
                    time.sleep(2)
                    break
            except:
                continue
